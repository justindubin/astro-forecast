import os

DOTENV_PATH = os.path.join(os.getcwd(), '.env')
ENV_VAR_NAMES = [
    'ASTRO_API_KEY',
    'TWILIO_ACCOUNT_SID',
    'TWILIO_AUTH_TOKEN',
    'TWILIO_PHONE_NUMBER',
    'TARGET_PHONE_NUMBER',
    'LATITUDE',
    'LONGITUDE',
]