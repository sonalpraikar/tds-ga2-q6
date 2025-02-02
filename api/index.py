from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the app
CORS(app)

# Load the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')
with open(json_file_path, 'r') as file:
    student_data = json.load(file)

@app.route("/api", methods=["GET"])
def get_marks():
    # Parse query parameters
    requested_names = request.args.getlist('name')  # Get names from the query parameters
    
    # Fetch marks for requested names
    marks = [student_data.get(name, None) for name in requested_names]

    # Return JSON response with marks
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
