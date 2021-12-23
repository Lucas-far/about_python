

// Módulo: number.isinteger.js
// Aparição: aula_18_Tipos_em_JavaScript:_Number.js
// Objetivo: verificar se uma var é da classe [ number ], tendo como retorno, um booleano

let unidade = '1'
console.log([1], unidade, Number.isInteger(unidade))  // não é
unidade = Number(unidade)                             // conversão
console.log([2], unidade, Number.isInteger(unidade))  // agora é
unidade = 1.1
console.log([3], unidade, Number.isInteger(unidade))  // se casa decimal != .0, será [ false ]
