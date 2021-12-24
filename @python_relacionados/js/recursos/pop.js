

// Módulo:   pop.js
// Aparição: aula_24._Tipos_em_JavaScript:_Array.js
// Objetivo: remover último índice a direita, em uma classe [ array ]

let l = [3, 2, 1, 0]
console.log(`Antes: ${l}`)
l.pop()
console.log(`Depois: ${l}`)

// deletar por [ delete ]
delete l[0]
delete l[1] // eu tentei repetir o comando acima deste, mas não surtiu o efeito esperado
console.log(`Agora: ${l}`)
