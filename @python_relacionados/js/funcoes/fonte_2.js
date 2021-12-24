/*
!@#

------- FONTE -------
50. Exemplos Básicos de Funções #01

------- LEGENDAS -------
1.  Função sem retorno
2.  Impressão interna à função, não fora dela
3.  Função com retorno
4.  Impressão externa à função, não dentro dela
5.  Parâmetros ausentes (não funciona, a não ser que os valores sejam pré-definidos na função)
6.  Parâmetros insuficientes (não funciona, a não ser que os valores sejam pré-definidos na função)
7.  Parâmetros corretos
8.  Parâmetros excessivos (os excedentes são ignorados)
9.  Parâmetros ausentes (não funciona, a não ser que os valores sejam pré-definidos na função)
10. Parâmetros insuficientes (não funciona, a não ser que os valores sejam pré-definidos na função)
11. Parâmetros corretos
12. Parâmetros excessivos (os excedentes são ignorados)
*/

// 1 e 2
function imprimirSoma(a, b) {
  console.log(a + b)
}

// 3 e 4
function soma(a, b) {
  return a + b
}

imprimirSoma() // 5
imprimirSoma(1) // 6
imprimirSoma(1, 2) // 7
imprimirSoma(1, 2, 3) // 8

console.log('[1] ' + soma()) // 9
console.log('[2] ' + soma(1)) // 10
console.log('[3] ' + soma(1, 2)) // 11
console.log('[4] ' + soma(1, 2, 3)) // 12
