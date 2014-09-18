import requests
import simplejson as json
from data import *
import urllib
import base64

class Twitter:

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

        self.auth()


    def getUser(self, userId):
        headers = {'Authorization' : 'Bearer ' + self.token}

        r = requests.get(GET_USER_URL, params = {'user_id': userId}, headers = headers)
        if r.ok:
            return json.loads(r.text)
        else:
            r.raise_for_status()



    def auth(self):
        code = urllib.quote_plus(self.key) + ':' + urllib.quote_plus(self.secret)
        code = base64.b64encode(code)

        headers = {
            'Authorization' : 'Basic ' + code,
            'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        data = 'grant_type=client_credentials'

        r = requests.post(AUTH_URL, headers = headers, data = data)
        if r.ok:
            self.token = json.loads(r.text)['access_token']
        else:
            r.raise_for_status()



if __name__ == '__main__':
    twitter = Twitter(APP_KEY, APP_SECRET)
    user = twitter.getUser('813286')
    print user
