import pyautogui as ptg
from bd import inserirCotacao
from buscarCotacao import buscarCotacao
import tkinter as tk

def consultarAtivo(codAtivo, acoesMonitoradas, guiaAtual):
    if codAtivo in acoesMonitoradas:
        if acoesMonitoradas.index(codAtivo) > guiaAtual:
            return alterarGuiaApos(codAtivo, acoesMonitoradas, guiaAtual)
        else:
            return alterarGuiaAnterior(codAtivo, acoesMonitoradas, guiaAtual)
    return atualizarGuiaAtual(guiaAtual)

def alterarGuiaApos(codAtivo, acoesMonitoradas, guiaAtual):
    x = 0
    while x < acoesMonitoradas.index(codAtivo) - guiaAtual:
        ptg.hotkey('ctrl', 'tab')
        x += 1
    ptg.sleep(0.2)
    try:
        inserirCotacao(codAtivo, buscarCotacao())
    except ValueError:
        inserirCotacao(codAtivo, buscarCotacao())
    except tk.TclError:
        inserirCotacao(codAtivo, buscarCotacao())
    return atualizarGuiaAtual(acoesMonitoradas.index(codAtivo))

def alterarGuiaAnterior(codAtivo,acoesMonitoradas, guiaAtual):
    x = 0
    while x < guiaAtual - acoesMonitoradas.index(codAtivo):
        ptg.hotkey('ctrl', 'shift', 'tab')
        x += 1
    ptg.sleep(0.2)
    try:
        inserirCotacao(codAtivo, buscarCotacao())
    except ValueError:
        inserirCotacao(codAtivo, buscarCotacao())
    except tk.TclError:
        inserirCotacao(codAtivo, buscarCotacao())
    return atualizarGuiaAtual(acoesMonitoradas.index(codAtivo))

def atualizarGuiaAtual(guia, modo = 0):
    #Valor enviado deve ser tamanho da lista de ações - 1, devido ao index começar do 0.
    if modo == 1:
        return guia
    return guia