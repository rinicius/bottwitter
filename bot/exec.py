#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import time
from bot.authbot import getauth
from bot.authbot import acharfraseaprender, login, acharfrasesemaprender


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        api = login()
        texto = status.text

        # reply
        ntexto = ''

        if texto[0] == '@':
            stringl = list(texto)
            index = stringl.index('!')
            ntexto = texto[index + 4::]
        else:
            ntexto = texto[4::]

        api = login()
        api.update_status(acharfraseaprender(ntexto))

        return True

    def on_connect(self):
        api = login()
        while True:
            api.update_status(acharfrasesemaprender())
            time.sleep(120)

    def on_error(self, status):
        print(status)


auth = getauth()

twitterStream = MyStreamListener()
twitterStream = tweepy.Stream(auth, listener=MyStreamListener())
twitterStream.filter(track=['!vg'])
