from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
SPREADSHEET_ID = "1ibydxbggPyfpfAhbvlYGmov3f_GZdzaONTV7oRwODzE"
spreadsheet = client.open_by_key(SPREADSHEET_ID)
sheet = spreadsheet.sheet1


# Initialize Sheet: Check and create header if not present
def initialize_sheet():
    try:
        # Get all values to check if sheet is empty
        existing_data = sheet.get_all_values()
        
        if not existing_data:  # Only initialize if sheet is completely empty
            # Set up the headers
            headers = ['timestamp', 'mood', 'note']
            sheet.append_row(headers)
            
            # Format header row
            header_format = {
                "backgroundColor": {"red": 0.8, "green": 0.8, "blue": 0.8},
                "textFormat": {"bold": True}
            }
            sheet.format('A1:C1', header_format)
            
            # Adjust column widths
            sheet.columns_auto_resize(0, 3)  # Resize columns A through C
            
            print("Sheet initialized with headers!")
        else:
            print("Sheet already contains data - preserving existing content")
        
    except Exception as e:
        print(f"Error initializing sheet: {e}")


@app.route('/log_mood', methods=['POST'])
def log_mood():
    data = request.get_json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood = data.get('mood')
    note = data.get('note', '')
    sheet.append_row([timestamp, mood, note])
    return jsonify({'status': 'success'}), 200

@app.route('/get_moods', methods=['GET'])
def get_moods():
    records = sheet.get_all_records()
    return jsonify(records), 200

if __name__ == "__main__":
    print("Initializing sheet...")
    initialize_sheet()  # Call initialize_sheet when server starts
    print("Starting Flask server...")
    app.run(port=5000, debug=True)
