

def scroll_down_content():
    from pyautogui import moveTo, click, hotkey

    top_right_scroll_bar = (1333, 100)
    hotkey('win', 'd')
    moveTo(top_right_scroll_bar[0], top_right_scroll_bar[1])
    click(top_right_scroll_bar[0], top_right_scroll_bar[1])

    while True:
        hotkey('down')


if __name__ == '__main__':
    scroll_down_content()
