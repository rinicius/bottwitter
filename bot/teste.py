string = '@testebot15 !vg oi'

if string[0] == '@':
    stringl = list(string)
    index = stringl.index('!')
    ntexto = string[index+4::]

print(ntexto)

