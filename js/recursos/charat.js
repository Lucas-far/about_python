

// Módulo: charat.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: retornar a posição de um caractere numa classe [ string ]

const palavra = 'Ecma' // 0123456 índices (contagem iniciada do zero)

console.log(`O índice 0 é = ${palavra.charAt(0)}`)
console.log(`O índice 1 é = ${palavra.charAt(1)}`)
console.log(`O índice 2 é = ${palavra.charAt(2)}`)
console.log(`O índice 3 é = ${palavra.charAt(3)}`)

// se o índice for excedente, o retorno = vazio
console.log(`O índice 4 é = ${palavra.charAt(4)}`)

// uso do método em dados literais é permitido
console.log('Lucas'.charAt(0))
