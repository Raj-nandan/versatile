from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS  # Add this import
import os  # Add this import for environment variables

app = Flask(__name__)
CORS(app)  # Update this line to use CORS in Flask
translator = Translator()

# Set the configuration from environment variables
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')  # Set environment
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'  # Set debug mode

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text_to_translate = data.get('text')
    
    # Translate from English to Gujarati
    translation = translator.translate(text_to_translate, src='en', dest='gu')
    
    return jsonify({"translated_text": translation.text})

if __name__ == '__main__':
    # Use Gunicorn or another WSGI server in production
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=app.config['DEBUG'])  # Update to run on all interfaces