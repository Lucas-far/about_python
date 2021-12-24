

// Módulo: tostring.js
// Aparição: aula_18_Tipos_em_JavaScript:_Number.js
// Objetivo: converter um dado de classe [ number ] para sua versão binária
// Objetivo2: converter um dado de classe [ qualquer ] para classe [ string ]

let valor_qualquer = 1_234_567
console.log([1], valor_qualquer.toString(2))
valor_qualquer = 1_234_567.891011
console.log([2], valor_qualquer.toString(2))
valor_qualquer = [valor_qualquer]
console.log([3], valor_qualquer, typeof valor_qualquer)
valor_qualquer = valor_qualquer.toString() // conversão para string
console.log([4], valor_qualquer, typeof valor_qualquer)
