

from urllib.request import urlopen
from bs4 import BeautifulSoup
# Dependência: pip install beautifulsoup4 / pip install lxml
# Dependência: apt-get install python3-bs4 / apt-get install python-lxml
# Importação: from bs4 import BeautifulSoup

# url = 'https://pt.wikipedia.org/wiki/Brasil'
# html_code = urlopen(url=url).read().decode("utf-8")
# soup = BeautifulSoup(html_code, 'lxml')

_ = '-------------------------------------------------------'

html_string = """
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    
        <title>Boostrap standard template</title>
      </head>
      <body>
        <h1>Hello, world!</h1>
        <i class="i1">Itálico</i>
        <b id="teste">Texto em negrito</b>
        <b class="teste2">Texto em negrito 2</b>
        <p class="par1 par2">Parágrafo</p>
        <img src="C:\\Users\\Conta secundária\\PycharmProjects\\python_resources\\@python_relacionados\\neural_nine_youtube_channel\\mapa.png" alt="Mapa do Brasil">
    
        <span>vazio</span>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">First name</th>
              <th scope="col">Last name</th>
              <th scope="col">Age</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Mark</td>
              <td>Otto</td>
              <td>18</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Jacob</td>
              <td>Thornton</td>
              <td>19</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td colspan="2">Larry the Bird</td>
              <td>20</td>
            </tr>
          </tbody>
        </table>
        
        <div>
          <span>1</span>
            <div>
              <span>2</span>
                <div>
                  <span>3</span>
                </div>
            </div>
        </div>
        <!-- Optional JavaScript; choose one of the two! -->
    
        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
    
        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!--
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
        -->
      </body>
    </html>
    """

soup = BeautifulSoup(html_string, 'lxml')


# print(soup)
print([_, 1, _], '\n', soup.prettify())          # Organizar o esqueleto da página
tag_b = soup.b
print([_, 2, _], '\n', tag_b)                    # Se há uma tag <b></b> no esqueleto, será retornada a primeira (com a tag inclusa)
print([_, 3, _], '\n', tag_b.string)             # Idem (sem a tag inclusa)
tag_b_all = soup.find_all('b')  # Se a tag argumento exister no esqueleto, retornar todas, em lista
print([_, 4, _], '\n', tag_b_all)
print([_, 5, _], '\n', tag_b.name)               # Retorno o tipo da tag em um variável que chama uma tag (nesse caso, a tag 'b')
print([_, 6, _], '\n', tag_b)
tag_b.name = 'vazio'
print([_, 7, _], '\n', tag_b)             # modificando o nome de uma tag extraída de uma var por reatribuição
print([_, 8, _], '\n', tag_b['id'])       # Se nessa var há uma tag com esse tipo, ele será retornado
print([_, 9, _], '\n', tag_b.attrs)       # Se nessa var há uma tag com esse tipo, um dicionário {atrib: valor} é criado
tag_b['class'] = 'novo'  # Novo atributo adicionado
print([_, 10, _], '\n', tag_b)             # <vazio class="novo" id="teste">Texto em negrito</vazio>
del tag_b['class']       # atributo removido
print([_, 11, _], '\n', tag_b)             # <vazio id="teste">Texto em negrito</vazio>
print([_, 12, _], '\n', soup.i['class'])   # Retorna da primeira tag 'p' que tenha atributo 'class', o seu valor, ou valores
print([_, 13, _], '\n', soup.p['class'])   # Retorna da primeira tag 'p' que tenha atributo 'class', o seu valor, ou valores
tag_images_all = soup.find_all('img')
print([_, 14, _], '\n', tag_images_all[0])         # Acessando tags do método [ find_all() ] por indexação
print([_, 15, _], '\n', tag_images_all[0]['src'])  # Acessando tags do método [ find_all() ] por indexação e sintaxe de dicionário
print([_, 16, _], '\n', tag_images_all[0]['alt'])  # Acessando tags do método [ find_all() ] por indexação e sintaxe de dicionário
tag_i = soup.i
print([_, 17, _], '\n', tag_i)
tag_i_edited = tag_i.string.replace_with('Itálico'.upper())  # Substituição de conteúdo de uma tag
print([_, 18, _], '\n', tag_i)
print([_, 19, _], '\n', tag_i_edited.string, type(tag_i_edited.string))
print([_, 20, _], '\n', str(tag_i_edited.string), type(str(tag_i_edited.string)))  # Conversão de um elemento para texto puro
print([_, 21, _], '\n', soup.title)
print([_, 22, _], '\n', soup.head)
print([_, 23, _], '\n', soup.body)
print([_, 24, _], '\n', soup.body.span)
print([_, 25, _], '\n', soup.body.table.td.contents)

for index, tag in enumerate(soup.body.children):
    print([_, 'n', index, _])
    print(tag)

print([_, 26, _], '\n',)
print(len(list(soup.body.children)))
print(list(soup.body.children))

print([_, 27, _], '\n',)  # Mostrar o conteúdo textual de um html (nesse contexto, espaços foram descartados)
for string in soup.strings:
    if string == '\n':
        string.replace(string, '')
    else:
        print(repr(string))

print([_, 28, _], '\n',)  # Idêntico ao item 27
for string in soup.stripped_strings:
    if string == '\n':
        string.replace(string, '')
    else:
        print(repr(string))

print([_, 29, _], '\n', soup.html)  # Outra forma de mostrar um esqueleto html

for parent in soup.div.parents:  # Não sei a utilidade (mostrar tags de escopos acima)
    print(parent.name)

# for index, tag in enumerate(soup.body.descendant):
#     print([_, 'n', index, _])
#     print(tag)


# first_table = soup.find_all('table')
# print(first_table[0])
# rows = first_table.findAll('tr')[1:]
# print(rows)

# for link in all_tags_link:
#     print(link.get('href'))

# print(str(soup.get_text()).replace('\n\n', ''))