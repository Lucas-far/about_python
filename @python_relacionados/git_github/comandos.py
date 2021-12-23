

def comandos():
    """
    ---------------------------------------------------- git add . ----------------------------------------------------
        • adiciona arquivos para a fila de 'commit'
        -> se este arquivo for editado antes do 'commit', ele volta um estágio, precisando ser adicionado novamente

    ---------------------------------------------------- git branch ----------------------------------------------------
        • retorna o(s) 'Branch(es)' existente(s) no repositório local (o branch com * é o que está logado)

    ------------------------------------------------- git branch nome -------------------------------------------------
        • criar um 'Branch' e loga nele

    ------------------------------------------------ git checkout nome ------------------------------------------------
        • logar em um 'Branch' especificado

    -------------------------------------------- git commit -m 'descrição' --------------------------------------------
        • prepara os módulos para serem enviados do repositório local para o remoto, para atualização
        -> pode ser adicionada a sintaxe "a" antes do "m" como atalho para o comando [ git add . ]

    ----------------------------------------------------- git log -----------------------------------------------------
        • listar COMMITs de um repositório local (todos os autores)

    ------------------------------------------- git log --author='nome_user' -------------------------------------------
        • listar COMMITS de um autor especificado

    ------------------------------------------------ git log --decorate ------------------------------------------------
        • não sei, mas parece idêntico ao comando [ git log ]

    ------------------------------------------------- git log --graph -------------------------------------------------
        • listar COMMITs de um repositório local (todos os autores) + o desenho do 'Branch' na lateral esquerda

    ----------------------------------------------------- git push -----------------------------------------------------
        • envia módulos do repositório local para o remoto, para atualização

    --------------------------------------------------- git shortlog ---------------------------------------------------
        • listar a quantidade de COMMITs e o seu autor (ordem alfabética) e a descrição

    ------------------------------------------------- git shortlog -sn -------------------------------------------------
        • listar a quantidade de COMMITs e o seu autor (ordem alfabética)

    ---------------------------------------------- git show código_commit ----------------------------------------------
        • exibir detalhes mais específicos de um COMMIT, através de seu código
        -> para saber o código de um COMMIT, usa-se o comando [ git log ]

    ---------------------------------------------------- git status ----------------------------------------------------
        • retorna módulos que foram alterados após o último 'commit'
    """
