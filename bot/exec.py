#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from bot.authbot import getauth


class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        from bot.authbot import login, papagaio, acharfrase
        import time
        api = login()

        #papagaio(api, status)
        #print(status.text)

        while True:
            api.update_status(acharfrase())
            time.sleep(10)
        return True

    def on_error(self, status):
        print(status)


auth = getauth()

twitterStream = MyStreamListener()
twitterStream = tweepy.Stream(auth, listener=MyStreamListener())
twitterStream.filter(track=['!vg'])
