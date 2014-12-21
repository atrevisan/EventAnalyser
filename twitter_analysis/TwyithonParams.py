from twython import Twython

APP_KEY = 'SZcWKO9few3q7PWCUQJ4Tz2lZ'
APP_SECRET = 'KAN4FXH89fWcBFb7wO3iQPoYdfXrMbAcarqAWQjH3R3SGrnncM'

api = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = api.obtain_access_token()