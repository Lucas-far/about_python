// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\replace.js]
// 1. Se o caractere está no texto, ele retorna o índice (qualquer valor igual ou acima de 0), caso contrário, ele retorna -1
// 2. O caractere passado pode ser numérico, contanto que ele existe no texto alvo

function trocarCaractere(texto, caractere, caractereNovo) {
  let tipo = String(typeof texto)
  let caractereExiste = texto.indexOf(caractere) // 1

  if (tipo == 'string' && caractereExiste != -1) {
    let novoTexto = texto.replace(caractere, caractereNovo)
    return novoTexto
  } else {
    return 'Seu texto não é uma string, ou o caractere informado não existe no texto'
  }
}

console.log(
  trocarCaractere(
    (texto = 'Javascript'),
    (caractere = 's'),
    (caractereNovo = 'x')
  )
)

console.log(
  trocarCaractere(
    (texto = 'Javascript'),
    (caractere = '*'),
    (caractereNovo = 'x')
  )
)

console.log(
  trocarCaractere(
    (texto = ['Javascript']),
    (caractere = '*'),
    (caractereNovo = 'x')
  )
)

// 2
console.log(
  trocarCaractere(
    (texto = 'Javascript7'),
    (caractere = 7),
    (caractereNovo = '_____')
  )
)

let nome = 'Henrique'
const nome2 = 'Henrique1234'
let frases = [
  'Substituir algo que não existe:',
  'Substituir o primeiro dígito pelo [par2]:',
  'Substituir todo e qualquer dígito pelo [par2]:',
  'Substituir o primeiro índice pelo [par2]:',
  'Substituir todos os índices pelo [par2]:'
]

// Executar o arquivo para saber as funções de cada código
console.log(`${frases[0]} ${nome} / ${nome.replace('c', 'v')}`)
console.log(`${frases[1]} ${nome2} / ${nome2.replace(/\d/, '*')}`)
console.log(`${frases[2]} ${nome2} / ${nome2.replace(/\d/g, '*')}`)
console.log(`${frases[3]} ${nome2} / ${nome2.replace(/\w/, '*')}`)
console.log(`${frases[4]} ${nome2} / ${nome2.replace(/\w/g, '*')}`)
