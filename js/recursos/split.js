

// Módulo: split.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: converter uma classe [ string ] para [ array ]

const nome = 'Juvêncio Eugênio Saraiva Costa'

console.log(nome.split(' ')) // o parâmetro string é o separador (nesse exemplo = espaço)
console.log(nome.split('ê')) // se o separador for um char, este é eliminado na separação

// pode ser usado [ regex ], que possui a mesma ideia da [ '' ]
console.log(nome.split(/a/))
