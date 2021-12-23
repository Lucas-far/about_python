

import pyautogui                                            # importação global
import pyautogui as auto                                    # importação global apelidada
from pyautogui import *                                     # importação global com sintaxe de importação específica
from pyautogui import click                                 # importação específica
from pyautogui import click as clk                          # importação específica apelidada
from pyautogui import click, drag, hotkey, moveTo           # importações específicas múltiplas
from pyautogui import hotkey as htk, position as pst        # importações específicas múltiplas apelidadas
from pyautogui import (click, drag, hotkey)                 # importações específicas múltiplas em tupla
from pyautogui import (click as c, drag as d, hotkey as k)  # importações específicas múltiplas apelidadas em tupla
from PYTHON import print_vs_return                          # importação modular
from PYTHON.a import alt_codes                              # importação diretório modular

def infos():
    """
    Objetivos
         importar métodos, módulos, bibliotecas

    Observações
        1. Em importações modular e importações diretório modular, evoca-se algo pelo: módulo.dado (var, função, etc...)
    """

pyautogui.hotkey()                     # importação global (chamada de um método)
auto.hotkey()                          # importação global apelidada (chamada de um método)
hotkey()                               # importação específica (chamada de um método)
htk()                                  # importação específica apelidada (chamada de um método)
print_vs_return.f_print(28, 11, 2020)  # importação modular (chamada da variável)
print(alt_codes.l)                     # importação diretório modular (chamada de variável)
