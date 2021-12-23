

def objetivo():
    """
    - Retornar a posição do índice de um objeto de classe string, tomando como referência o lado direito
    - O método só faz sentido se há repetição do dado
    - O método possui relação com [ find ], mas este busca da forma normal, da esquerda para a direita
    """


string = '007007'
print([1], string.rfind('7'))      # Informa a posição do índice (contagem a partir do 0)
print([2], string.rfind('7') + 1)  # Informa a posição normal (contagem a partir do 1)

# ----------------------------------------------- [ rfind ] vs [ find ] -----------------------------------------------
print([3], string.find('7'))
print([4], string.find('7') + 1)
