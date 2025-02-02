from http.server import BaseHTTPRequestHandler
import json
import os
from flask_cors import CORS

CORS(app)

# Load the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')
with open(json_file_path, 'r') as file:
    student_data = json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_string = self.path.split('?')[-1]
        query_params = {k: v for k, v in [param.split('=') for param in query_string.split('&')] if k == 'name'}

        # Extract requested names
        requested_names = query_params.get('name', [])
        if isinstance(requested_names, str):  # If only one name is provided
            requested_names = [requested_names]

        # Fetch marks for requested names
        marks = [student_data.get(name, None) for name in requested_names]

        # Prepare response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):  # Handle preflight requests for CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
