

// Módulo: aula_19_Number:_Alguns_Cuidados.js
// Aula: 19. Number: Alguns Cuidados

console.log(1 / 0)       // divisões por 0, sempre gerarão: Infinity
console.log('10' / 2)    // classe [ string ] inteiro, funciona para cálculos, o que é estranho
console.log('10.17' / 2) // ................. não inteiro, ....................................
console.log('frase' * 2) // diferente de Python, multiplicar strings não é permitido em JS
console.log(0.7 + 0.1)   // aparentemente, cálculos com valores > 1, não conseguem ser exatos
