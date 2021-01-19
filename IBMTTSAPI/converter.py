from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey, url = "Dpwt0BnR3wB0iy-VFtfn5EJ6d3I4DfbOntkUDalx5Y3H", "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/fd23b693-eb2b-4707-acba-7b1696329a9d"
apikey_click, url_click = "jOe5jzW_pnESNaIGOKF3uU4kSly_A85bo4gRMT6P000u", "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/947c5234-7a8b-49d9-9682-9e80299b457f"

authenticator = IAMAuthenticator(f'{apikey_click}')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(f'{url_click}')

def txtToSpeech(vc, txt):

    with open('corr.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                txt,
                voice=vc,
                accept='audio/mp3'        
            ).get_result().content)

with open('new 2.txt') as f:
    txt = f.read()
    txtToSpeech('en-US_MichaelV3Voice', txt)