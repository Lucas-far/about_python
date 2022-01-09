// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\aulas\secao_3\aula_30.js]
// Relacionado com: [_1.js] [_2.js]

// Função da aula
function trocarValor_v3(value1, value2) {
  let temp = value1
  value1 = value2
  value2 = temp

  return [value1, value2]
}
// Objeto da aula
const objeto3 = trocarValor_v3((value1 = 1), (value2 = 99))
console.log(objeto3)
