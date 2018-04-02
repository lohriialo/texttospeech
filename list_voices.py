# Google's CLOUD TEXT-TO-SPEECH https://cloud.google.com/text-to-speech/

from google.cloud import texttospeech
import os

# auth setup https://cloud.google.com/docs/authentication/getting-started
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\temp\text-to-speech-service-account.json'

# Instantiates client
client = texttospeech.TextToSpeechClient()

# Performs the list voices request
voices = client.list_voices()

for voice in voices.voices:
    # Display the voice's name. Example: tpc-vocoded
    print('Name: {}'.format(voice.name))

    # Display the supported language codes for this voice. Example: "en-US"
    for language_code in voice.language_codes:
        print('Supported language: {}'.format(language_code))

    # SSML Voice Gender values from google.cloud.texttospeech.enums
    ssml_voice_genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE',
                          'FEMALE', 'NEUTRAL']

    # Display the SSML Voice Gender
    print('SSML Voice Gender: {}'.format(
        ssml_voice_genders[voice.ssml_gender]))

    # Display the natural sample rate hertz for this voice. Example: 24000
    print('Natural Sample Rate Hertz: {}\n'.format(
        voice.natural_sample_rate_hertz))