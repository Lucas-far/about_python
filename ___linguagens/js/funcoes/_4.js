// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\aulas\secao_3\aula_50.js]
// 1.  Função sem retorno
// 2.  Impressão interna à função, não fora dela
// 3.  Parâmetros ausentes (não funciona, a não ser que os valores sejam pré-definidos na função)
// 4.  Parâmetros insuficientes (não funciona, a não ser que os valores sejam pré-definidos na função)
// 5.  Parâmetros corretos
// 6.  Parâmetros excessivos (os excedentes são ignorados)

// 1
function imprimirSoma(a, b) {
  console.log(a + b) // 2
}

imprimirSoma() // 3
imprimirSoma(1) // 4
imprimirSoma(1, 2) // 5
imprimirSoma(1, 2, 3) // 6
