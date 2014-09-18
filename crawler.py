from twitter import *
from sets import Set
from db import *
from data iport *


class Crawler:

    def __init__(self):
        self.idSet = Set()
        self.idQueue = []
        self.twitter = Twitter(APP_KEY, APP_SECRET)
        self.db = DB()
        self.cache = Cache()


    def crawlUserInfo(self, userId):
        pass


    def crawl(self, seed):
        self.add(seed)

        while not self.top and len(self.idSet) != 0:
            userId = self.getFirstInQueue()
            if not self.db.containsUser(userId):
                self.crawlUserInfo(userId)

            if self.cache.contains(userId):
                friendList = self.cache.get(userId)
            else:
                friendList = []
                friendJson = self.twitter.getFriendList(userId)
                for f in friendJson['ids']:
                    friendList.append(f)



    def add(self, userId):
        self.idSet.add(userId)
        self.idQueue.append(userId)


    def getFirstInQueue(self):
        return self.idQueue.pop(0)