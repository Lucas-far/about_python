// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\split.js]

function stringParaLista(texto, separador) {
  let tipoTexto = String(typeof texto)
  let tipoSeparador = String(typeof separador)

  if (tipoTexto == 'string' && tipoSeparador == 'string') {
    let textoLista = texto.split(separador)
    return textoLista
  } else {
    return 'O texto/separador especificados não são uma string'
  }
}

console.log('[1] ', stringParaLista((texto = 'Javascript'), (separador = 'a')))
console.log(
  '[2] ',
  stringParaLista((texto = ['Javascript']), (separador = 'a'))
) // 1    problema com par 1
console.log('[3] ', stringParaLista((texto = 'Javascript'), (separador = 1))) // 2    problema com par 2
console.log('\n')

const nome = 'Anã Banana Lamanda'
let frases = [
  'Parâmetro vazio: a string toda torna-se um índice',
  'Parâmetro espaço: o espaço torna-se o separador',
  'Parâmetro letra: a letra torna-se o separador e será excluída',
  'Parâmetro regex: faz o mesmo do parâmetro letra'
]

console.log(`${frases[0]}    ${nome}    ->    `, nome.split())
console.log(`${frases[1]}    ${nome}    ->    `, nome.split(' '))
console.log(`${frases[2]}    ${nome}    ->    `, nome.split('n'))
console.log(`${frases[3]}    ${nome}    ->    `, nome.split(/n/))
