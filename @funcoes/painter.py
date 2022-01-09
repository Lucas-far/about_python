

def mtd_painter(color: str = 'blue', text: str = 'texto'):
    """"""
    # keys = conditions / values = actions of the conditions
    colors = {
        'black': '\033[1:30m' + text + '\033[m',
        'red': '\033[1:31m' + text + '\033[m',
        'green': '\033[1:32m' + text + '\033[m',
        'yellow': '\033[1:33m' + text + '\033[m',
        'blue': '\033[1:34m' + text + '\033[m',
        'purple': '\033[1:35m' + text + '\033[m',
        'cyan': '\033[1:36m' + text + '\033[m',
        'gray': '\033[1:37m' + text + '\033[m',
    }

    for key in colors:
        if color == key:
            return colors[key]


if __name__ == '__main__':
    var = mtd_painter(color='blue', text='Python')
    print(var)
