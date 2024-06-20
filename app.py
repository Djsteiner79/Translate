from flask import Flask, request, jsonify, render_template
import configparser
import openai
import logging

app = Flask(__name__)

# Læs API-nøglen fra config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['openai']['api_key']

# Indstil OpenAI API-nøgle
openai.api_key = api_key

# Konfigurer logning
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        input_text = data.get('text', '')
        
        if not input_text:
            raise ValueError("Ingen tekst at oversætte")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a translator that translates Danish to English."},
                {"role": "user", "content": input_text}
            ],
        )

        translated_text = response['choices'][0]['message']['content'].strip()
        return jsonify({'translatedText': translated_text})

    except Exception as e:
        app.logger.error(f"Fejl i oversættelsesruten: {e}")
        return jsonify({'error': str(e)}), 500

# Optional: Handle favicon.ico requests to remove the 404 error
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
