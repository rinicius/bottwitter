import tweepy
import requests
import os
from pathlib import Path


def getauth():
    consumer_key = "jSvESQ7k6usjt3ljnAs2Fm375"
    consumer_secret = "Pxy29nzTA4RI6nK1DGMpRrlOlI4XZXprPUNAoYHQMBn03RKPj4"
    acces_token = "1241302550768431106-m2JUmvo6Yvnv497Ek9RzlobKjzvTsB"
    access_token_secret = "PI07con9giscNOTqHRFDLFPRLHEwI5QZeW9aaQ4fTZEIy"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acces_token, access_token_secret)

    return auth


def login():
    consumer_key = "jSvESQ7k6usjt3ljnAs2Fm375"
    consumer_secret = "Pxy29nzTA4RI6nK1DGMpRrlOlI4XZXprPUNAoYHQMBn03RKPj4"
    acces_token = "1241302550768431106-m2JUmvo6Yvnv497Ek9RzlobKjzvTsB"
    access_token_secret = "PI07con9giscNOTqHRFDLFPRLHEwI5QZeW9aaQ4fTZEIy"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acces_token, access_token_secret)

    apel = tweepy.API(auth)
    return apel


def upimagemporlink(api, url, status):
    filename = "imagem.jpg"
    rq = requests.get(url, stream=True)
    if rq.status_code == 200:
            with open(filename, 'wb') as image:
                for chunks in rq:
                    image.write(chunks)

            api.update_with_media(filename, status)
            os.remove(filename)
    else:
        print('deu erro!')


def upimagem(api, filename, status):
    api.update_with_media(filename, status)










