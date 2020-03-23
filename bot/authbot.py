#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import random


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


def papagaio(api, status):
    texto = status.text
    # se for reply
    ntexto = ''
    if texto[0] == '@':
        stringl = list(texto)
        index = stringl.index('!')
        ntexto = texto[index + 4::]
    else:
        ntexto = texto[4::]
    # reply
    print(status.text)
    print(status.user.name)
    api.update_status(ntexto)


def acharpalavra():
    # letrai = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'x', 'z']
    letrai = ['4', '5', '6', '7', '8', '9']

    letra = random.choice(letrai)

    page = requests.get(f'https://www.dicio.com.br/palavras-com-{letra}-letras/')

    soup = BeautifulSoup(page.text, 'html.parser')

    """last_links = soup.find(class_='AlphaNav')
    last_links.decompose()"""

    palavra_list = soup.find(class_='col-xs-12 col-sm-7 col-md-8 card')
    palavra_list_items = palavra_list.find_all('p')

    lista = list()

    # Usar .contents para pegar as tags <a> filhas
    for palavras in palavra_list_items:
        names = palavras.contents
        lista.append(names)

    lista.pop(0)
    listan = list()

    for i in range(len(lista[0])):
        if i % 2 != 0:
            pass
        else:
            listan.append(lista[0][i])

    return random.choice(listan)


def acharfraseaprender(palavra):
    file1 = open('C:/Users/VINICIUSROCHADASILVA/Desktop/tweepy-bots/pdf/frases.txt', encoding="utf-8")

    nlinha = random.randint(1, 541)

    for i in range(nlinha):
        linha = file1.readline()
    file1.close()

    f = open("C:/Users/VINICIUSROCHADASILVA/Desktop/tweepy-bots/pdf/palavras.txt", "a")
    f.write(f'{palavra}\n')
    f.close()

    print(palavra)
    print(linha)

    linha = linha.replace('Deus', palavra)
    cont = 0
    for i in linha:
        if i == '-':
            linha = linha[:cont:]
        else:
            cont += 1

    return linha


def acharfrasesemaprender():
    file1 = open('C:/Users/VINICIUSROCHADASILVA/Desktop/tweepy-bots/pdf/frases.txt', encoding="utf-8")

    nlinha = random.randint(1, 541)
    for i in range(nlinha):
        linha = file1.readline()

    file1.close()

    palavra = acharpalavra()
    palavra = palavra.capitalize()

    print(palavra)
    print(linha)

    linha = linha.replace('Deus', palavra)
    cont = 0
    for i in linha:
        if i == '-':
            linha = linha[:cont:]
        else:
            cont += 1

    return linha








