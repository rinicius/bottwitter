import tweepy
from bot.authbot import getauth


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        from bot.authbot import login
        api = login()
        texto = status.text

        #se for reply
        ntexto = ''
        if texto[0] == '@':
            stringl = list(texto)
            index = stringl.index('!')
            ntexto = texto[index + 4::]
        else:
            ntexto = texto[4::]
        #reply

        print(status.text)
        api.update_status(ntexto)

        return True

    def on_error(self, status):
        print(status)


auth = getauth()

twitterStream = MyStreamListener()
twitterStream = tweepy.Stream(auth, listener=MyStreamListener())
twitterStream.filter(track=['!vg'])
