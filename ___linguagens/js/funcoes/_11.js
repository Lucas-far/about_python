// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\indexof.js]
// 1. No caso de caractere repetido, o retorno é o da primeira ocorrência, da esquerda para a direita
// 2. Quando o caractere não está no alvo procurado, o retorno é -1, mas neste contexto, ele foi tratado

function qualIndice(texto, caractere) {
  let retorno = texto.indexOf(caractere)
  if (retorno == -1) {
    let campo1 = 'texto:'.toUpperCase()
    let campo2 = 'caractere:'.toUpperCase()
    let campo3 = 'status:'.toUpperCase()
    let status = 'não encontrado'
    return `( ${campo1} ${texto} )    ( ${campo2} ${caractere} )    ( ${campo3} ${status} )`
  } else {
    return `( ${caractere} ) foi encontra na posição [${retorno}]`
  }
}

const palavra = '#Javascript@dev#'
console.log(qualIndice((texto = palavra), (caractere = '#'))) // 1
console.log(qualIndice((texto = palavra), (caractere = '.'))) // 2
