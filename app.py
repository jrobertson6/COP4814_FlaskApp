
from flask import Flask, render_template, request, send_file, make_response
from config import Config
from forms import PhoneForm
import requests, os, pandas as pd, json, time
from io import StringIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config.from_object(Config)

# Flask-Limiter to control API call frequency
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

@limiter.limit("30 per hour")
def verify_number(number):
    api_key = app.config['NUMVERIFY_API_KEY']
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"valid": False, "error": "API Error"}

@app.route("/", methods=["GET", "POST"])
@limiter.limit("20 per minute")
def index():
    form = PhoneForm()
    results = []

    if request.method == "POST":
        has_text = bool(form.phone_number.data.strip())
        has_file = form.csv_file.data and form.csv_file.data.filename != ""

        if not has_text and not has_file:
            form.phone_number.errors.append("Please enter a phone number or upload a CSV.")
        elif form.validate():
            selected_code = form.country_code.data

            if has_file:
                csv_data = form.csv_file.data.read().decode("utf-8")
                df = pd.read_csv(StringIO(csv_data))
                for num in df['Phone']:
                    full_number = num if num.startswith("+") else selected_code + num
                    res = verify_number(full_number)
                    results.append(res)
                    time.sleep(1)
            else:
                full_number = form.phone_number.data
                if not full_number.startswith("+"):
                    full_number = selected_code + full_number
                res = verify_number(full_number)
                results.append(res)

            return render_template("results.html", results=results)

    return render_template("index.html", form=form)

@app.route("/download", methods=["POST"])
@limiter.limit("10 per minute")
def download():
    try:
        raw_json = request.form.get("csv_data")
        result_list = json.loads(raw_json)
        df = pd.DataFrame(result_list)
        csv_output = df.to_csv(index=False)

        response = make_response(csv_output)
        response.headers["Content-Disposition"] = "attachment; filename=results.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

    except Exception as e:
        return f"An error occurred: {e}", 400

if __name__ == "__main__":
    app.run(debug=True)
