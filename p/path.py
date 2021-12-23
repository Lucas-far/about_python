

"""
Objetivo:
    tratamento de rotas, alterando-as ou consultando-as

Observação:
    1. No OS Ubuntu, rota:  /
    2. No OS Windows, rota: \\
"""

from os import path

# Usando alguns métodos
print([1], path.exists('/home/lucas/Desktop/x'))  # verificar se a rota especificada existe, se não: False
print([2], path.exists('/home/lucas/Desktop/'))   # verificar se a rota especificada existe, se sim: True
print([3], path.join('/home/lucas/Pictures/', 'gradientes'))  # concatenar rota existente com um pedaço de outra
print([4], path.isabs('/home/lucas/Pictures/gradientes'))     # verificar se uma rota é absoluta

def acesso():
    """
    python / from os import path / dir(path)

    '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
    '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix',
    'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath',
    'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists',
    'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat',
    'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys'
    """
