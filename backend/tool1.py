from flask import Flask, request, jsonify
import json
import os
import logging
from flask_cors import CORS  # Import CORS

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/search', methods=['POST'])
def search():
    try:
        # Log the incoming request
        logging.debug('Received request data: %s', request.data)
        
        # Parse JSON data from the request
        data = request.json
        if not data:
            raise ValueError('No JSON data received or invalid JSON format')

        search_query = data.get('query', '')
        location = data.get('location', '')

        # Log the extracted data
        logging.debug('Extracted search query: %s', search_query)
        logging.debug('Extracted location: %s', location)

        # Prepare the data to be saved
        data_to_save = {
            'query': search_query,
            'location': location
        }

        # Path to save the JSON file
        file_path = 'backend/data.json'
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save data to JSON file
        with open(file_path, 'w') as json_file:
            json.dump(data_to_save, json_file, indent=4)
        
        # Log the successful save
        logging.info('Data successfully saved to %s', file_path)
        
        response_message = f'Search Query: "{search_query}", Location: "{location}"'
        return jsonify({'message': response_message})
    
    except Exception as e:
        # Log the error
        logging.error('Error occurred: %s', str(e))
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/api/results', methods=['GET'])
def get_results():
    try:
        # Corrected the file path to match your folder structure
        file_path = os.path.join('backend', 'results.json')
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'{file_path} not found')

        with open(file_path, 'r') as json_file:
            results_data = json.load(json_file)
        
        return jsonify(results_data)

    except Exception as e:
        logging.error('Error occurred while fetching results: %s', str(e))
        return jsonify({'error': 'Failed to fetch results'}), 500


if __name__ == '__main__':
    app.run(port=5000)
