// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\arrow.js]
// 1. Declaração
// 2. Nome da função
// 3. Nome de parâmetro
// 4. Retorno (como 'return' em Python)
// 5. ação da função

//  1      2         3   4       5
const cacha_alta = texto => texto.toUpperCase()

// Chamada literal da função
console.log('[1] ' + cacha_alta((texto = 'javascript')))

// Chamada da função numa variável
let objeto_ = cacha_alta((texto = 'js é a extensão de javascript'))
console.log('[2] ' + objeto_)
