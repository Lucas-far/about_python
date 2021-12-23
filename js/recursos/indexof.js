

// Módulo: indexof.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: retornar o índice de um caractere em uma classe [ string ]

const palavra = '_Cod3r_'

console.log(palavra.indexOf('_')) // como o caractere [ _ ] aparece +1 vez, o retorno é o do primeiro
console.log(palavra.indexOf('C'))
console.log(palavra.indexOf('o'))
console.log(palavra.indexOf('d'))
console.log(palavra.indexOf('3'))
console.log(palavra.indexOf('r'))
console.log(palavra.indexOf('*')) // retorno -1 caso o caractere procurado, não exista na var [ string ]
