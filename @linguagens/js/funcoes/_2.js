// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\aulas\secao_3\aula_30.js]
// Relacionado com: [_1.js]

// Função dentro de variável
const trocarValor_v2 = function (value1, value2) {
  let values = [value2, value1]
  value1 = values[0]
  value2 = values[1]

  return [value1, value2]
}
// Objeto da segunda função
const objeto2 = trocarValor_v2((value1 = 1), (value2 = 99))
console.log(objeto2)
