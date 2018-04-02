# Google's CLOUD TEXT-TO-SPEECH https://cloud.google.com/text-to-speech/

from google.cloud import texttospeech
import os

# auth setup https://cloud.google.com/docs/authentication/getting-started
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\temp\text-to-speech-service-account.json'

# Instantiates client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(
    text="This Synthesized speech is read in from text within the application. "
         "Synthesized speech can be created by concatenating pieces of "
         "recorded speech that are stored in a database. Systems differ "
         "in the size of the stored speech units; a system that stores "
         "phones or diphones provides the largest output range, but may "
         "lack clarity. For specific usage domains, the storage of entire "
         "words or sentences allows for high-quality output. Alternatively, "
         "a synthesizer can incorporate a model of the vocal tract and other "
         "human voice characteristics to create a completely synthetic voice output."
         "The quality of a speech synthesizer is judged by its similarity to "
         "the human voice and by its ability to be understood clearly. "
         "An intelligible text-to-speech program allows people with visual "
         "impairments or reading disabilities to listen to written words on "
         "a home computer. Many computer operating systems have included "
         "speech synthesizers since the early 1990s.")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('text_output_speech.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)