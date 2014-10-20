from twitter import *
import time
from data import *
import random
import sys

def hit(worker, userIdList):
    time.sleep(1)

    try:
        while worker.getRemainingUserListRequestCount() > 0:
            return worker.getUserList(userIdList)
        else:
            print 'reach limitation...'
            time.sleep(60)
    except Exception, e:
        print e
        time.sleep(60)
        return []


def search(worker, startId, maxId):
    tid = startId
    f = open('id.log', 'w')

    while True:
        f.write('Searching From %d To %d...\n' % (tid,  maxId))
        f.flush()
        userIdList = []
        while len(userIdList) < 100:
            tidStr = str(random.randint(tid, maxId))
            userIdList.append(tidStr)

        print userIdList

        userList = hit(worker, userIdList)
        if len(userList) > 0:
            userList = [int(u['id']) for u in userList]
            userList.sort()
            tid = userList[-1]

    f.close()
