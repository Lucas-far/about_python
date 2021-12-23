

"""
Módulo: script_aulas_git.py
Palavra chave: tutorial sobre git
"""


# Configurações iniciais para o Git
def aula_6():
    """
    1 - git config --global user.name "seu_user"
    2 - git config --global user.email "seu_email"
    3 - git config user.name
    4 - git config user.email
    5 - git config --list

    1 - configugração do nome vinculado ao seu Git (preferencialmente seu nome de usuário do Github)
    2 - configugração do email vinculado ao seu Git (preferencialmente seu email vinculado ao Github)
    3 - consultar seu nome de usuário (relevante para o comando: git log)
    4 - consultar seu email (relevante para o comando: git log)
    5 - informações gerais sobre o seu Git
    """


# Criando um repositório local (passos iniciais)
def aula_7():
    """
    1 - mkdir nome_pasta
    2 - cd nome_pasta
    3 - git init
    4 - ls -la
    5 - cd .git
    6 - cd ..

    1 - criação da pasta que receberá o repositório Git
    2 - entrada na pasta recentemente criada
    3 - criar um repositório e torná-lo visível ao Git
    4 - comando que torna possível a visualização do diretório [ .git ]
    5 - adentrar o diretório [ .git ] e verificar seus arquivos
    6 - retornar a pasta matriz
    """


# Adição de conteúdo em um repositório, e uso dos comandos básicos de gerenciamento até a ação de COMMIT
def aula_9():
    """
    ls -----------------------------------> no contexto da aula, não há pastas ou arquivos visíveis, somente o [ .git ]
    git status ------------------------------------> verificar se há algo criado no repositório alvo (vazio no momento)
    touch a.txt ------------------------------------------------------------------------------> um arquivo é adicionado
    git status ----------------------------------------------------------> agora há 1 arquivo com o status [ modified ]
    git add a.txt -------------------------> se o arquivo é recem criado, passa do status [ untracked ] para [ staged ]
                  * caso contrário, passa do status [ modified ] para [ staged ]
    alteração em [ a.txt ]
    git status ---------------> arquivo não mais recem criado modificado, saindo do status [ staged ] para [ modified ]
    git commit -am 'msg' ------------------------------> o arquivo já foi adicionado antes, então não precisa novamente
                         * o que acontece aqui, é o resumo do comando [ git add . ] em 1 letra [ a ]
                         * sendo assim, a letra [ a ] vai para [ git commit -m 'msg' ]
    git status -------------------------------------------> Como o COMMIT acaba de ser efetuado, não há o que adicionar
               * qualquer alteração, retorna o ciclo para gerar um novo COMMIT
    alteração em [ a.txt ]
    git status --------------------------------------------------------------> o arquivo retorna ao status [ modified ]
    git commit -am 'msg' ----------------------------------> adição e COMMIT do arquivo de uma vez, economizando código
    """


# Comandos usados após COMMIT
def aula_10_e_11():
    """
    AULA 10

    git shortlog -sn ------------------------------> listar COMMITs por ordem alfabética de autor e sua qtd. de COMMITs
    git shortlog ---------------> listar COMMITs por ordem alfabética de autor, sua qtd. de COMMITs, e descrição destes
    git log --author='nome_user' -----------------------------------------------> listar COMMITs de um autor especifico
    git log -------------------------------------------------------------------> listar COMMITs de um repositório local
    git log --decorate ---------------------------> listar COMMITs de um repositório local, com detalhes do branch dono
    git log --graph ------------> listar COMMITs de um repositório local, com detalhes gráficos da relação dos branches
    git show código_commit ---------------> exibir as informações de um COMMIT especifico, e destacando suas alterações

    AULA 11

    git status --------------------------------------------------> não há arquivos de status [ modified ] neste momento
    alteração em [ a.txt ]
    git diff -----------------> com o arquivo sendo alterado, esse comando exibe alterações, neste, e em qualquer outro
    git diff --name-only ---------------> ou ao invés de mostrar as alterações, mostrar somente o nome do(s) arquivo(s)
    git commit -am "msg" --------------------> o arquivo já existe, então pode ser adicionado e comitado ao mesmo tempo
    """

# Outros comandos úteis após COMMIT
def aula_12():
    """
    alteração em [ a.txt ]
    git checkout nome_arquivo.formato --------------------> comando usado quando um arquivo está no status [ modified ]
                                      * esse comando retorna para a última alteração
                                      * mensagem de retorno: [ Updated 1 path from the index ]
                                      * quando o inteiro zerar, o comando perde sua função
                                      * se o COMMIT acabou de ser feito, e esse comando usado, não funcionará

    git reset HEAD nome_arquivo.formato ----------> retorna qualquer elemento do repositório para o status [ modified ]
                                        * comando não funcional logo após um COMMIT

    git reset --soft -------------------------------------> cancela um COMMIT, mantendo arquivo(s) no status [ staged ]
    git reset --mixed ----------------------------------> cancela um COMMIT, mantendo arquivo(s) no status [ modified ]
    git reset --hard ------------------------------------> comando mais complexo, mas vou explicar da forma que entendi
                     * o comando fica entre 2 COMMITS
                     * cancela o último COMMIT feito, e qualquer alteração em arquivo(s) deste
                     * até o momento de penúltimo COMMIT

    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    OBS: Nos 3 tipos de reset, deve haver pelo menos 2 COMMITS feitos
    OBS: Nos 3 tipos de reset, ao usá-los, lembrar de pegar, não o código do COMMIT alvo, mas do abaixo dele
    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    """

# Vinculação do repositório local (OS) ao remoto (Github)
def aula_13():
    """
    1 - Criar uma chave SSH (caso não tenha uma, ver arquivo: [ tutorial_gerar_chave_ssh.py ])
    2 - Criar repositório Github -> [ avatar ] [ your repositories ] [ new ] [ seguir os passos ] [ salvar ]
    3 - Ao criar, tutoriais são exibidos na página, observe aquele que fala sobre PUSH
    4 - [ ctrl + c ] no código SSH na área de PUSH
    4 - EXEMPLO: git remote add origin git@github.com:Lucas-far/git.git
    5 - Voltar ao repositório local, e no seu terminal, fazer os códigos:

        - git remote --------------------------------------------------------------------------> não deve haver retorno
        - git remote add origin git@github.com:Lucas-far/git.git -----------------------> criação do repositório remoto
        - git remote (retorno: origin) -----------------------------------------> verificar se há um repositório remoto

        - git branch -M main ------------------------------------------------> mudar o nome do branch local para: main
                             * para que funcione, deve haver 1 COMMIT existente

        - git push -u origin main -------------------------------> comando de vinculação de repositório local ao remoto

        OBS: no próximo PUSH, talvez somente [ git push ] seja o suficiente
    """

# Clonagem pelo Github
def aula_17():
    """
    - Ir ao website Github, em uma página de um repositório alvo
    - Ir ao botão [ code ], escolher [ SSH ]
    - EXEMPLO: [ git clone git@github.com:codingforentrepreneurs/eCommerce.git one_repository ]

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBSERVAÇÕES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - comando: git clone
    - parâmetro 1: link SSH
    - parâmetro 2: nome_repositório
    """

# Informações sobre o recurso Git: BRANCH
def aula_19():
    """
    SOBRE BRANCH

    - É como um ponteiro móvel que leva/aponta a um COMMIT
    - O nome padrão do primeiro branch local, chama-se [ master ]
    - Pode ser criado de formas múltiplas, apontados para vários COMMITs simultâneos

    MOTIVOS

    * É usado para trabalhos em grupo sob um mesmo repositório
    * É usado para trabalhos simultâneos, sem interferência de pessoas no mesmo local
    * É usado para modificar, sem alterar o branch local principal (master)
    * É uma opção de fácil gerenciamento (criação e deletamento)
    * É usado para evitar conflitos
    """

# Gerenciamento de BRANCH
def aula_20_e_21():
    """
    git checkout -b nome_branch --------------> (criação) OBS: um branch novo criado, sempre desativa o branch anterior
    git branch --------------------------------------------> (listagem) OBS: o brach atual é destacado por um asterísco
    git branch --all --------------------------------------------------------> (listagem) OBS: branches locais e remoto
    git branch -m nome_novo ---------------------------------> (renomeação) OBS: precisa ativar o branch alvo, primeiro
    git checkout nome_branch -----------------------> (transição) mudança do branch atual ativo, para outro branch alvo
    git branch -D nome_branch ----------------> (deletamento) OBS: o branch alvo não pode ser deletado com este ativado

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONTEXTO PARA USAR BRANCH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1 - Inicialmente, qualquer repositório iniciado, possui um branch local padrão [ master ]
    2 - Vamos criar um segundo branch local
    3 - git checkout -b master2
    4 - touch parte_2.py
    5 - Adicionando conteúdo ao arquivo:

    def greet(name='person') -> str:
        return f'Hello, world, {name} speaking xD!'

    if __name__ == '__main__':
        print(greet('Lucas'))

    6 - git add .
    7 - git commit -m 'added: parte_2.py'
    8 - git checkout master -----------------> é possível ver que o arquivo [ parte_2.py ], irá sumir do branch [ master ]
                            * ao executar COMMIT no branch local [ master2 ], é assegurado sua posse ao arquivo
                            * portante, ao logar em um outro branch, arquivos de outros branches, somem
    9 - git checkout master2 -----------------------------> ao retornar ao branch criador, o arquivo volta a reaparecer
    """

# Informações sobre o recurso Git: MERGE
def aula_22():
    """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBSERVAÇÕES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - Conforme um branch novo é criado, este aponta para o seu anterior
    - Se dados do branch anterior forem deletados, os do branch atual não são afetados
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    O QUE É MERGE?
        -> é uma união entre dois branches

    VANTAGEM?
        -> os 2 COMMITS, para serem mesclados, precisam de um terceiro, onde os outros dois, não deixam de existir

    DESVANTAGEM?
        -> criação de um commit extra (o terceiro), para poder juntar outros dois existentes
        -> poluição no histórico
    """

# Informações sobre o recurso Git: REBASE
def aula_23():
    """
    O QUE É REBASE?
        -> é a união entre dois branches

    VANTAGEM?
        -> evita um terceiro COMMIT
        -> manutenção de histórico como linear

    DESVANTAGEM?
        -> perda de ordem cronológica
    """

# Diferença entre MERGE e REBASE
def aulas_22_e_23():
    """
    - Qual a diferença, segundo o professor?
        MERGE  cria um COMMIT para juntar diferenças entre COMMITS anteriores
        REBASE joga as mudanças para o início da fila
    """

# Exemplificação do recurso Git: MERGE
def aula_24():
    """
    mkdir merge
    cd merge
    git init
    touch a.txt -------------------------------------------------------------------------------> (branch_dono = master)
    git add .
    git commit -m '1'
    git checkout -B master2 ------------------------------------------------------------------> (branch_novo = master2)
    touch b.txt --------------------------------------------------------------------------------> (branch_dono = teste)
    git add .
    git commit -m '2'
    git checkout master --------------------------------------------------------------------> (retorno_branch = master)

    MERGE
        git merge master2

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBSERVAÇÕES SOBRE MERGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1 - Estando logado no branch herdeiro [ master ], faz-se [ git merge nome_branch_doador ]
    2 - A lógica, é que, pelo MERGE, o branch [ master ] recebe do branch [ master2 ], o arquivo [ b.txt ]

    3 - pode ser que ao executar esse comando, seja aberto um [ console Nano ], se for o caso, fazer o seguinte:

        * digitar a mensagem de COMMIT, depois [ ctrl + x ], [ ctrl + y ] e [ ENTER ]
        * retorno de sucesso após primeiro MERGE: [ Merge made by the 'recursive' strategy. ]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    git log --graph
    """

# Exemplificação do recurso Git: REBASE
def aula_24_parte2():
    """
    - Continuando a partir do final do exemplo da criação de MERGE
    - Atualmente, há dois branches: [ master ] & [ master2 ]
    - O branch local atual é [ master ]
    - touch c.txt -----------------------------------------------------------------------------> (branch_dono = master)
    - git add .
    - git commit -m '3'
    - git checkout -B master3 ----------------------------------------------------------------> (branch_novo = master3)
    - touch d.txt ----------------------------------------------------------------------------> (branch_dono = master3)
    - git add .
    - git commit -m '4'
    - git checkout master

    REBASE
        git rebase master3

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBSERVAÇÕES SOBRE REBASE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1 - Estando logado no branch herdeiro [ master ], faz-se [ git merge nome_branch_doador ]
    2 - A lógica, é que, pelo MERGE, o branch [ master ] recebe do branch [ master3 ], o arquivo [ d.txt ]

    3 - pode ser que ao executar esse comando, seja aberto um [ console Nano ], se for o caso, fazer o seguinte:

        * digitar a mensagem de COMMIT, depois [ ctrl + x ], [ ctrl + y ] e [ ENTER ]
        * retorno de sucesso após primeiro REBASE: [ Merge made by the 'recursive' strategy. ]
    """

# Dica sobre quando usar MERGE ou REBASE
def aula_24_parte3():
    """
    1 - Sempre que puder, é melhor usar REBASE
    2 - O MERGE é mais usado em contextos de PULL REQUEST, onde torna-se necessário ver o que foi unido
    3 - Para casos de adição de novo recurso, ao final, é recomendável usar MERGE
    4 - Em casos de adição de COMMITS, atualizando branches, é recomendável usar REBASE
    """

# Configuração de um arquivo [ .gitignore ]
def aula_25():
    """ sobre_gitignore.py """

# Sobre Git stash
def aula_26():
    """
    O QUE É?
        responsável por guardar ações que ainda não foram comitadas [ status = modified ]

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DESCRIÇÃO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    alteração em um arquivo
    git status
    git stash ------------------------------------------> criar um WIP (work in progress) de uma alteração não comitada
              * comando funciona somente após o primeiro COMMIT
    git status -----------------------------------------------------> após o comando [ git stash ] o histórico é zerado
    git checkout -B master2
    touch b.txt
    git add .
    git commit -m 'added: b.txt'
    git stash apply ------------------------------------------> aplica a alteração congelada feita por um [ git stash ]
    cat a.txt -------------------------------------------> o conteúdo escrito antes de [ git stash ], estará disponível
    git checkout master
    cat a.txt -------------------------------------------> o conteúdo escrito antes de [ git stash ], estará disponível
    git stash list ----------------------------------------------------> listar as vezes em que [ git stash ] foi usado
    git stash clear -------------------------------------------------------> limpar o histórico de uso do [ git stash ]

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - Ou seja, mesmo estando em um branch onde não ocorreu a alteração [ master2 ], a alteração foi aplicada
    - [ git stash ] congela
    - [ git stash apply ] descongela e aplica
    """

# Atalhos para comandos Git
def aula_27():
    """
    git config --global alias.st status ------------------------------------------------------> encurtar [ git status ]
    git config --global alias.ck checkout --------------------------------------------------> encurtar [ git checkout ]
    git config --global alias.br branch ------------------------------------------------------> encurtar [ git branch ]
    git config --global alias.ct commit ------------------------------------------------------> encurtar [ git commit ]
    """

# Usando tags do Git
def aula_28():
    """
    FUNÇÃO:
        - não sei dizer :(

    USO
        - git tag -a 1.0 -m 'Mensagem' ------------------------------------------------------------> criação de uma tag
        - git push origin main --tags -----------------------------------------> enviar tag para seu repositório remoto
        - git tag --------------------------------------------------------------------------------> listar tags criadas

        COMANDOS USADOS EM CONJUNTO
        - git tag -d versão_tag ------------------------------> deletar uma tag específica, apenas do repositório local
        - git push origin :versão_tag ---------------------------> deletar uma tag específica do seu repositório remoto
                                      * [ origin ] é o nome do branch remoto, podendo o seu ser, diferente

    DICIONÁRIO
        -a    = anotação
        1.0   = versão (eu recomendo ir aumentando de .1 em .1)
        -m    = mensagem

    CRIAÇÃO MANUAL PELA IDE PYCHARM:
        - Pycharm -> Git -> new tag

    INSTRUÇÕES APÓS O EMPURRO DAS TAGS:
        - Ir a página do repositório remoto do projeto
        - Procurar e clicar no link [ tags ] (atualmente logo acima da tabela de arquivos)
        - As tags disponíveis serão listadas
    """

# Usando o recurso Git: revert
def aula_29():
    """
    O QUE É?
        - uma versão alternativa do comando [ git checkout / git reset --soft ]
        - porém, seu uso resulta na criação de um outro COMMIT
        - segundo o professor, o histórico não é perdido, servindo como um rascunho do COMMIT anterior

    Alteração em algum arquivo do seu projeto
    git commit -am 'msg'
    No contexto da aula, vamos supor que esse commit gera um erro relevante
    Talvez, o melhor procedimento seja usar o recurso "revert" do Git
    git log -------------------------------------------------------> consultar o código commit de onde aconteceu o erro
    git revert código commit
    git log -----------------------------------------------------> ao usar [ git revert ], o COMMIT alvo não é desfeito
            * ao invés, outro é criado, com a alteração desfeita
    git show último código commit ----------------------------------------------------> a alteração desfeita é mostrada
    """
