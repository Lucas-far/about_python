// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\length.js]
// [OBS] A contagem com esse método começa do 1, como em Python
// 1. Forma de mostrar os tipos de dados permitidos
// 2. Variável que armazena os tipos de dados permitidos, em forma de string (usados em condição)
// 3. Parâmetro correto que satisfaz a condição da função: [string]
// 4. Parâmetro correto que satisfaz a condição da função: [object]

function retornarTamanho(dado) {
  let permitidos = [String(typeof ''), String(typeof [])] // 1
  let tipo = String(typeof dado) // 2

  if (tipo == 'object' || tipo == 'string') {
    return dado.length
  } else {
    return `Tipo de dado [${tipo}] não possui tamanho. Tipos permitidos: [${permitidos}]`
  }
}

let item1 = 'js'.length
let item2 = [1, 2, 3].length

console.log(retornarTamanho((dado = 0)))
console.log(retornarTamanho((dado = NaN)))
console.log(retornarTamanho((dado = true)))
console.log(retornarTamanho((dado = false)))
console.log(retornarTamanho((dado = 'javascript'))) // 3
console.log(retornarTamanho((dado = ['a', 'b', 'c']))) // 4

console.log('Uso normal do método:', item1)
console.log('Uso normal do método:', item2)
