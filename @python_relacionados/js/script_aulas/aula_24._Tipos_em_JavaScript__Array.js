

// Módulo: aula_24._Tipos_em_JavaScript:_Array.js
// Aparição: 24. Tipos em JavaScript: Array

const l = [1, 2, 3] // 0, 1, 2... (contagem de índice do 0)

console.log(l[0])
console.log(l[4])   // índice inexistente gera = undefined


// -------------------------------- SINTAXES IGUAIS, FUNÇÕES DIFERENTES --------------------------------
// alteração de um índice
l[0] = 0               
console.log(l)

// adição de um índice 
l[3] = 4               
console.log(l)

// adição de um índice (quando o índice especificado têm + de 1 de distância do último índice)
// l[3] para l[5] é + de 1, então gera-se <empty items>
l[5] = 6                
console.log(l)

// ------------------------------------------------ OBS ------------------------------------------------
// ver [ recursos / length.js ]
// ver [ recursos / push.js ]
// ver [ recursos / pop.js ]
