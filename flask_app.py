from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Get the transcription text from the POST request
    transcription = request.form['text']

    # Translate the transcription from Arabic to English
    translated_text = translator.translate(transcription, src='ar', dest='en').text

    # Return the translated text as a JSON response
    return jsonify({"translated": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
