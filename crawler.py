from twitter import *
from sets import Set
from db import *
from data iport *


class Crawler:

    def __init__(self):
        self.idSet = Set()
        self.twitter = Twitter(APP_KEY, APP_SECRET)
        self.db = DB()
        self.cache = Cache()


    def crawlUserInfo(self, userId):
        pass


    def crawl(self, seed):
        self.idSet.add(seed)
        if not self.db.containsUser(seed):
            self.crawlUserInfo(seed)

        while 
