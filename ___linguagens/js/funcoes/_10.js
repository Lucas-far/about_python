// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\concat.js]
// 1. Referência para o loop, até onde ele pode ir
// 2. Elemento de condição que pergunta se o [p2] é uma classe [lista]
// 3. Container que recebe todas as frases definidas no [p2]
// 4. PROBLEMA: Não consigo eliminar a vírgula que acontece na conversão de lista para string
// 5. Uso genérico da função

function mesclarFrases(alvo, complemento) {
  let tamanho = complemento.length // 1
  let tipo = String(typeof complemento) == 'object' // 2
  let caixa = [] // 3

  if (tipo == true) {
    // let caixa = alvo

    for (let i = 0; i < tamanho; i++) {
      caixa.push(complemento[i])
    }
    let resultado = `${alvo} ${String(caixa)}` // 4
    return resultado
  } else {
    return alvo.concat(' ', complemento)
  }
}

let nome = 'Javascript'
let frase = 'é uma linguagem de programação'
let frase2 = ['é uma linguagem de programação', 'popular']

console.log('[1] ', mesclarFrases((alvo = nome), (complemento = frase)))
console.log('[2] ', mesclarFrases((alvo = nome), (complemento = frase2)))

// 5
let pessoa = 'Ana'
const sobrenome = 'Banana'
const conclusao = 'é doida'

console.log('[3] ', pessoa.concat(' ', sobrenome, ' ', conclusao))
