// Função normal
function funcao_normal() {}

// Função dentro de variável
const funcao_normal2 = function () {}

// Função dentro de dados (array)
const lista = [
  function (n1, n2) {
    return n1 / n2
  }
]
console.log(lista[0]((n1 = 7), (n2 = 2)))

// Função dentro de objeto
const objeto = {}
objeto.falar = function (texto) {
  return texto
}
console.log(objeto.falar((texto = 'Javascript')))
