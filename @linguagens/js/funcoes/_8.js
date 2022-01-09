// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\charat.js]
// 1. A contagem de índice em Javascript, inicia do 0, enquanto a contagem em [length] começa pelo 1
// 1. Por essa condição, o cálculo com [length] precisa ter 1 subtraido, para igualar
// 2. Se o índice for excedente, o retorno é [vazio = ''], mas nesse contexto, houve um tratamento
// 3. O uso do método em dados literais é permitido

function dizerLetra(dado, indice) {
  let tamanhoPermitido = dado.length - 1 // 1
  if (indice <= tamanhoPermitido) {
    return dado.charAt(indice)
  } else {
    return `O índice informado é excedente ao do dado fornecido: ${indice}/${tamanhoPermitido}`
  }
}

console.log(dizerLetra((dado = 'Javascript'), (indice = 0)))
console.log(dizerLetra((dado = 'Javascript'), (indice = 9)))
console.log(dizerLetra((dado = 'Javascript'), (indice = 10))) // 2
console.log('javascript'.charAt(2)) // 3
