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
        return self.getJson(GET_USER_URL, 
                            {'user_id': userId})


    def getUserList(self, userIdList):
        return self.getJson(BATCH_GET_USER_URL, 
                            {'user_id' : ','.join(userIdList)})


    def getFriendList(self, userId, cursor = -1):
        return self.getJson(FRIEND_LIST_URL,
                            {'user_id' : userId,
                             'cursor'  : cursor,
                             'count'   : 5000})


    def getRemainingUserListRequestCount(self):
        return int(self.getRemaining()['resources']['users']['/users/lookup']['remaining'])


    def getRemaining(self):
        return self.getJson(LIMITATION_URL, 
                            {'resources' : 'users'})


    def getJson(self, url, param):
        headers = {'Authorization' : 'Bearer ' + self.token}

        r = requests.get(url, params = param, headers = headers)
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
