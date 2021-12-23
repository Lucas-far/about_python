

def scroll_down_content(scrolling_speed):
    from pyautogui import moveTo, click, hotkey, position
    from time import sleep

    top_right_scroll_bar = (1335, 100)
    hotkey('win', 'd')
    moveTo(top_right_scroll_bar[0], top_right_scroll_bar[1])
    click(top_right_scroll_bar[0], top_right_scroll_bar[1])

    while True:
        hotkey('down')
        sleep(scrolling_speed)


if __name__ == '__main__':
    scroll_down_content(scrolling_speed=0)
