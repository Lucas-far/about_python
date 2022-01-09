// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\number.isinteger.js]

function verificarSeInteiro(dado) {
  let verificacao = Number.isInteger(dado)
  if (verificacao == true) {
    return `Sim, ${dado} é inteiro    TIPO: [${typeof dado}]`
  } else {
    return `Não, ${dado} não é inteiro    TIPO: [${typeof dado}]`
  }
}

console.log(verificarSeInteiro((dado = 0)))
console.log(verificarSeInteiro((dado = 0.7)))
console.log(verificarSeInteiro((dado = '1')))
console.log(verificarSeInteiro((dado = null)))
console.log(verificarSeInteiro((dado = NaN)))
console.log(verificarSeInteiro((dado = true)))
console.log(verificarSeInteiro((dado = false)))
console.log(verificarSeInteiro((dado = undefined)))
console.log(verificarSeInteiro((dado = Infinity)))
console.log('\n')
console.log('Uso do método fora da função:', Number.isInteger(1))
console.log('Uso do método fora da função:', Number.isInteger(1.1))
