

import pyautogui


class Pyautogui:

    # Instalar
    @staticmethod
    def instalar():
        """
        Windows
            pip install pyautogui pillow

        Ubuntu
            https://pyautogui.readthedocs.io/en/latest/install.html
            pip3 install pyautogui
            sudo apt-get install scrot
            sudo apt-get install python3-tk
            sudo apt-get install python3-dev
        """

    # Tirar foto da tela constantemente
    @staticmethod
    def f_screenshot():
        """
        p1 = distância da esquerda
        p2 = distância do topo
        p3 = largura (usar Iobit screen recorder)
        p4 = altura (usar Iobit screen recorder)
        """
        index = 1
        while True:

            pyautogui.screenshot(f'nome do arquivo{index}.png',
                                 region=(1107, 545, 106, 155))
            index += 1

    # Clicar onde o mouse estiver ou onde for determinado
    @staticmethod
    def f_click():
        """
        p1 = onde na horizontal
        p2 = onde na vertical
        p3 = quantidade de cliques
        p4 = intervalo do clique
        p5 = se quiser usar um botão do mouse
        """
        pyautogui.click(500, -200, 2, 1, button='left')
        pyautogui.click(500, -200, 2, 1, button='right')

    # Ver posição do mouse, cores na tela
    @staticmethod
    def f_displaymouseposition():
        """
        Função não parece funcionar em IDE, mas funciona no terminal
        python -> import pyautogui -> pyautogui.displayMousePosition()
        """
        pyautogui.displayMousePosition()

    # Mover mouse a partir da sua última posição
    @staticmethod
    def f_drag():
        """
        OBS: usar "displayMousePosition()" para ajudar na localização
        p1 = mover quanto horizontal
        p2 = mover quanto vertical
        p3 = duração da ação do movimento
        """
        pyautogui.drag(100, 0, 0.5)
        pyautogui.drag(0, 100, 0.5)
        pyautogui.drag(-100, 0, 0.5)
        pyautogui.drag(0, -100, 0.5)
        # Se x e y forem informados ao mesmo tempo: movimento \ ou /
        pyautogui.drag(20, 70, 0.5)
        pyautogui.drag(70, 20, 0.5)

    # Performar ação de teclado (não funciona em tela fora do desktop)
    @staticmethod
    def f_hotkey():
        # Exemplo de entrada única
        pyautogui.hotkey('enter')
        # Entradas combinadas [ exibição do desktop no Windows ]
        pyautogui.hotkey('win', 'd')
        # Entradas combinadas [ maximização de janelas no Windows e navegadores ]
        pyautogui.hotkey('alt', 'space', 'x')

    # Mover o mouse para um local desejado
    @staticmethod
    def f_moveto():
        """
        p1 = onde na horizontal
        p2 = onde na vertical
        p3 = tempo para fazer a transição
        """

        pyautogui.moveTo(300, 700, 5)

    # Informar a posição do mouse atual
    @staticmethod
    def f_position():
        # while True:
        #     print(pyautogui.position()[0], pyautogui.position()[1])
        print(pyautogui.position())
        print(pyautogui.position()[0])
        print(pyautogui.position()[1])
        print(pyautogui.position().x)
        print(pyautogui.position().y)

    # Digitar algo em locais onde é permitido (não sei fazer letras coma centuação)
    @staticmethod
    def f_typewrite():
        pyautogui.typewrite('Python é uma linguagem de programação', 0.1)

        key_table = [
            '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z',
            '{', '|', '}', '~',
            'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
            'browserback', 'browserfavorites', 'browserforward', 'browserhome',
            'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
            'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
            'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute',
            'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
            'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
            'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
            'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
            'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
            'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
            'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
            'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
            'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
            'command', 'option', 'optionleft', 'optionright']

    # Exemplo de algoritmo (leitura de conteúdo de página) (usado para ler ebook Unopar)
    @staticmethod
    def scroll_down_content():
        top_right_scroll_bar = (1333, 100)
        pyautogui.hotkey('win', 'd')
        pyautogui.moveTo(top_right_scroll_bar[0], top_right_scroll_bar[1])
        pyautogui.click(top_right_scroll_bar[0], top_right_scroll_bar[1])

        while True:
            pyautogui.hotkey('down')


if __name__ == '__main__':
    pyautogui_ = Pyautogui()
