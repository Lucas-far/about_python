// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\aulas\secao_3\aula_30.js]
// 1. Função comum
// 2. Objeto da função

// 1
function trocarValor_v1(value1, value2) {
  let values = [value2, value1]
  value1 = values[0]
  value2 = values[1]

  return [value1, value2]
}
// 2
const objeto = trocarValor_v1((value1 = 1), (value2 = 99))
console.log(objeto)
