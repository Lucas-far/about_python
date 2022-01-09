// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\aulas\secao_3\aula_50.js]
// Relacionado com: [_4.js]
// 1. Função com retorno
// 2. Impressão externa à função, não dentro dela
// 3. Parâmetros ausentes (não funciona, a não ser que os valores sejam pré-definidos na função)
// 4. Parâmetros insuficientes (não funciona, a não ser que os valores sejam pré-definidos na função)
// 5. Parâmetros corretos
// 6. Parâmetros excessivos (os excedentes são ignorados)

// 1
function soma(a, b) {
  return a + b // 2
}

console.log('[1] ' + soma()) // 3
console.log('[2] ' + soma(1)) // 4
console.log('[3] ' + soma(1, 2)) // 5
console.log('[4] ' + soma(1, 2, 3)) // 6
