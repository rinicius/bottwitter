import requests
from bs4 import BeautifulSoup
import random


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
    """
    palavra = random.choice(lista)
    
    palavra = random.choice(lista)
    while len(palavra) < 2:
        palavra = random.choice(lista)
    """
    for i in range(len(lista[0])):
        if i % 2 != 0:
            pass
        else:
            listan.append(lista[0][i])

    return random.choice(listan)


def acharfrase():
    file1 = open('C:/Users/VINICIUSROCHADASILVA/Desktop/tweepy-bots/pdf/frases.txt', encoding="utf-8")

    nlinha = random.randint(1, 541)
    for i in range(nlinha):
        linha = file1.readline()

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


print(acharpalavra())
