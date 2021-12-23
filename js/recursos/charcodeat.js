

// Módulo: charcodeat.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: encontrar a posição de um caractere numa classe [ string ] e retornar seu inteiro

const palavra = '_@^L2' // essa constante têm 4 índices (contagem de índice inicia do zero)

console.log(`Caractere: _ possui código = ${palavra.charCodeAt(0)}`)
console.log(`Caractere: @ possui código = ${palavra.charCodeAt(1)}`)
console.log(`Caractere: ^ possui código = ${palavra.charCodeAt(2)}`)
console.log(`Caractere: L possui código = ${palavra.charCodeAt(3)}`)
console.log(`Caractere: 2 possui código = ${palavra.charCodeAt(4)}`)

// se o índice é excedente, o retorno = NaN
console.log(`Caractere:   possui código = ${palavra.charCodeAt(5)}`)

// uso em dados literais é permitido
console.log('Pamonha'.charCodeAt(2))
