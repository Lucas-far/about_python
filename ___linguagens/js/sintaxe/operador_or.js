

// Módulo: operador_or.js
// Aparição: aula_23_Tipos_em_JavaScript:_Boolean.js
// Objetivo: comparar condições

const falso = !!0
const verdadeiro = !!1

// ----------------------------------------- LÓGICAS POSSÍVEIS -----------------------------------------
// Com o operador [ or = || ], há 25% de change de gerar um resultado falso

console.log(falso || falso)           // false
console.log(falso || verdadeiro)      // true
console.log(verdadeiro || falso)      // true
console.log(verdadeiro || verdadeiro) // true

console.log('Se nenhum dos dados for verdadeiro, então =', !!null || !!undefined || !!'')    // false
console.log('Se há pelo menos um valor verdadeiro, então =', !!null || !!undefined || !!' ') // true
