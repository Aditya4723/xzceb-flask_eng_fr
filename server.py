from flask import Flask, request, jsonify
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    """
    Endpoint to translate text from English to French.
    Expects JSON data with the 'text' key containing the English text to be translated.
    Returns a JSON response with the translated French text.
    """
    try:
        data = request.get_json()
        english_text = data.get('text', '')

        if not english_text:
            return jsonify({'error': 'No text provided for translation.'}), 400

        french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
        return jsonify({'french_text': french_text}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred during translation.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
