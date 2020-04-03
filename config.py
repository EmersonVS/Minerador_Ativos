#Configuração buscar

print("Configuração de Imagens")

from pyautogui import position

arqBuscar = open('modelos/modeloBuscar.txt', 'r')
arqConfigurado = open('buscarCotacao.py', 'w')

linhas = arqBuscar.readlines()

print("\nAbra o navegador chrome e siga os passos.")
input("\nPosicione o mouse no vértice inferior direito do símbolo de Recarregar.\nPressione Enter.")
v1 = position()
print("\nAbra o site < https://www.tradingview.com/symbols/BMFBOVESPA-PETR4/ > e aperte Ctrl + Shift + I")
input("\nPosicione o mouse no vértice superior esquerdo do símbolo D em laranja.\nPressione Enter.")
v2 = position()

linhas[7] = "    while(validarTela('imagens/atualizar.png', 0, 0, {}, {}) != None):\n".format(v1[0], v1[1])
linhas[9] = "    while(validarTela('imagens/valor.png', {}, {}, 138, 43) == None):\n".format(v2[0], v2[1])
linhas[11] = "    posicaoValor = validarTela('imagens/valor.png', {}, {}, 138, 43)\n".format(v2[0], v2[1])

for item in linhas:
    arqConfigurado.write(item)

arqConfigurado.close()
arqBuscar.close()

#Configuração Monitorar

arqMonitorar = open('modelos/modeloMonitorar.txt', 'r')
arqConfigurado = open('monitorarAtivos.py', 'w')

linhas = arqMonitorar.readlines()

input("\nPosicione o mouse sobre o icone do navegador Google Chrome na barra de tarefas.\nPressione Enter.")
v3 = position()

linhas[9] = "    ptg.click({},{})\n".format(v3[0], v3[1])
linhas[16] = "    while(validarTela('imagens/atualizar.png', 0, 0, {}, {}) != None):\n".format(v1[0], v1[1])

diretorio = input("\nDigite o diretório do arquivo ciclo.py.")
linhas[37] = "    ptg.write('{}/ciclo.py')\n".format(diretorio.replace('\\', '/'))

for item in linhas:
    arqConfigurado.write(item)

arqConfigurado.close()
arqMonitorar.close()

#Configuração BD

print("\nConfigurando o Banco de Dados MySQL.")

arqBD = open('modelos/modeloBD.txt', 'r')
arqConfigurado = open('bd.py', 'w')

linhas = arqBD.readlines()

servidor = input("\nHost: ")
user = input("Usuário: ")
senha = input("Senha: ")
banco = input("Banco de dados: ")
charset = input("Charset(UTF-8): ")

linhas[5] = linhas[5].replace('v1', servidor)
linhas[6] = linhas[6].replace('v2', user)
linhas[7] = linhas[7].replace('v3', senha)
linhas[8] = linhas[8].replace('v4', banco)
linhas[9] = linhas[9].replace('v5', charset)

for item in linhas:
    arqConfigurado.write(item)

arqBD.close()
arqConfigurado.close()

from bd import conectarBD
from bd import criarTabelas

try:
    conectarBD()
    print("\nConexão realizada com sucesso!\n")
    criar = input("Deseja criar as tabelas? S/N ")
    if criar.upper() == 'S':
        criarTabelas()
except:
    print("\nFalha ao conectar com o banco, configure novamente.")

input("\nConfigurações finalizadas. \nPressione enter para sair.")