// !@# exemplo
// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\substring.js]
// 1. Parâmetros corretos para testar o escopo de [if]
// 2. Parâmetro [texto] incorreto para testar o escopo de [else]
// 3. Parâmetro [inicio] incorreto para testar o escopo de [else]
// 4. Parâmetro [fim] incorreto para testar o escopo de [else]
// [OBS] Com 1 parâmetro, o método entende que é desejado do 0 até o índice no [par1]
// [OBS] Com 2 parâmetros, o método entende que é desejado do 0 até o índice no [par2] - 1
// [OBS] Por exemplo: Javascript -> Javascript.substring(4) = Java
// [OBS] Por exemplo: Javascript -> Javascript.substring(0, 4) = Java

function filtrarString(texto, inicio, fim) {
  // Variáveis de verificação
  let tipo = String(typeof texto)
  let tipoIndiceUm = Number.isInteger(inicio)
  let tipoIndiceDois = Number.isInteger(fim)

  if (tipo == 'string' && tipoIndiceUm == true && tipoIndiceDois == true) {
    return texto.substring(inicio, fim)
  } else {
    return 'O texto não é uma string, ou os índices não são números inteiros'
  }
}

console.log(filtrarString((texto = 'Javascript'), (inicio = 0), (fim = 4))) // 1
console.log(filtrarString((texto = ['Javascript']), (inicio = 0), (fim = 4))) // 2
console.log(filtrarString((texto = 'Javascript'), (inicio = '0'), (fim = 4))) // 3
console.log(filtrarString((texto = 'Javascript'), (inicio = 0), (fim = '4'))) // 4

const caracteres = '0123'

console.log(caracteres.substring(0))
console.log(caracteres.substring(1))
console.log(caracteres.substring(2))
console.log(caracteres.substring(1, 3))
