
Phone Number Verification Web Application
==================================================================

This interactive Flask web application allows users to verify phone numbers
individually or in bulk via CSV upload. It fetches real-time data from the
Numverify public API, providing carrier, location, and line type information.

The application also uses rate limiters to address API restrictions experienced with processing multiple requests using the free version of Numverify's API. Paid versions of the API do not have restrictions so the application can be modified in the event a paid
subscription is used.


------------------------------------------------------------------
How to Run the Application
------------------------------------------------------------------

1. Clone the Repository
------------------------
git clone https://github.com/jrobertson6/COP4814_FlaskApp
cd numverify-flask-app

Place the requirements.txt file in the project root

2. Create a Virtual Environment
-------------------------------
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Place project files in the following structure

	.venv
	  >static
		>syle.css
	  >templates
		>index.html
		>results.html
	  >app.py
	  >config.py
	  >forms.py	

3. Install Dependencies
------------------------
pip install -r requirements.txt

4. Set Up Environment Variables
-------------------------------
Create a `.env` file in the project root with the following content:

NUMVERIFY_API_KEY=your_api_key_here
SECRET_KEY=your_flask_secret_key

You can get a free API key at https://numverify.com

5. Run the Application
------------------------
python app.py

Then open your browser and go to http://127.0.0.1:5000


------------------------------------------------------------------
API Used: Numverify
------------------------------------------------------------------

Purpose: Validates phone numbers and retrieves metadata such as:
- Validity
- Carrier name
- Line type (mobile, landline, VoIP)
- Country and location

Example API Endpoint:
http://apilayer.net/api/validate?access_key=YOUR_API_KEY&number=+18136791009


------------------------------------------------------------------
Features Implemented
------------------------------------------------------------------

- Phone Number Validation
  - Accepts manual input via web form
  - Supports CSV upload for bulk validation using Pandas python framework

- Real-Time Carrier Lookup
  - Uses Numverify to get live info on number type, location, and provider

- Results Display
  - Tabular output of validation results
  - Allows download of results as a CSV

- Form Validation
  - Flask-WTF used for clean input handling

- Error Handling
  - Invalid formats, API failures, and missing data handled gracefully

- Responsive UI
  - Styled with Bootstrap for clean, mobile-friendly design


------------------------------------------------------------------
Example CSV Format
------------------------------------------------------------------

To use the bulk upload feature, provide a CSV file with a column labeled "Phone":

Phone
+18136791009
+442083661177
+919999999999
