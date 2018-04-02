# Google's CLOUD TEXT-TO-SPEECH https://cloud.google.com/text-to-speech/

from google.cloud import texttospeech
import os

# auth setup https://cloud.google.com/docs/authentication/getting-started
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\temp\text-to-speech-service-account.json'

# Instantiates client
client = texttospeech.TextToSpeechClient()

file = 'input_text.txt'
with open(file, 'r') as f:
    text = f.read()
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US',
                                                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('file_output_speech.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)