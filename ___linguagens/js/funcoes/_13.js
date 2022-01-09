// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\mathpi.js]
// 1. Forma de verificar se o tipo de casa decimal é a permitida (devendo ser um número)
// 2. Tratamentos com condições mistas
// 3. Aparentemente, com casa decimal não inteira, o javascript consegue ignorar a parte flutuante

function retornarPi(reduzido, casas) {
  let tipoCasa = String(typeof casas) // 1

  // 2
  if (reduzido == true && tipoCasa == 'number') {
    return Math.PI.toFixed(casas)
  }
  if (reduzido == true && tipoCasa != 'number') {
    return 'Não foi fornecida uma casa decimal válida'
  } else {
    return Math.PI
  }
}

console.log(retornarPi((reduzido = true), (casas = 2)))
console.log(retornarPi((reduzido = true), (casas = '')))
console.log(retornarPi((reduzido = false), (casas = 2)))
console.log(retornarPi((reduzido = true), (casas = 2.7))) // 3
console.log('Uso comum do método:', Math.PI)
