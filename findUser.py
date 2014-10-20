from twitter import *
from data import *
import sys

if __name__ == '__main__':
    twitter = Twitter(APP_KEY, APP_SECRET)
    print twitter.getUser(sys.argv[1])