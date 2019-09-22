### Script Python parta mudar extensão e nomes de arquivos em um diretório
### Creditos: site ufpr3d http://ufpr3d.blogspot.com/2010/05/script-python-parta-mudar-extensao-e.html
#--------------------------------------------------------------------
# renomeia.py
#
# Script Python para modificar a extensao de aquivos em um diretorio
# e mudar o nome
#
# Uso:
# Defina o diretorio, a extensão que quer retirar e a nova extensao, que
# pode ser vazia (" ").
# Por exemplo:
# diretorio = "/home/gildo/imagens"
# extensao = ".*JPEG" (para retirar as extensoes ".dcm", nao esqueca o asterisco)
# novaExtensao = ".jpg" (nesse caso eh vazia, mas poderia ser ".raw", por ex.)
#--------------------------------------------------------------------

import re
import string
import os

# Coloque os seus parametros aqui... C:\Users\ecaet\Documents\Programacao\Python\test
diretorio = "/Users/ecaet/Documents/Programacao/Python/test"
extensao = ".*"
novaExtensao = ".png"  # nesse caso eh vazia
parteQueSai = "IMAGEM-"
parteQueSubstitui = "slice"

# Muda extensao
reg = re.compile(extensao)
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        newExt = re.compile(extensao).match
        if newExt(arquivo):
            c = os.path.splitext(arquivo)
            b = c[0] + novaExtensao
            a = os.path.join(diretorio,arquivo)
            b = os.path.join(diretorio,b)
            os.rename(a,b)

# Modifica nome
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        print(arquivo)
        novoNome = str.replace(arquivo, parteQueSai, parteQueSubstitui)
        fullpathOld = os.path.join(diretorio,arquivo)
        fullpathNew = os.path.join(diretorio,novoNome)
        os.rename(fullpathOld, fullpathNew)
