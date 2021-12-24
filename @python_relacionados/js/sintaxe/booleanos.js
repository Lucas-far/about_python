// Aparição: aula_23_Tipos_em_JavaScript:_Boolean.js
// Objetivo: converter dados para tipo [ booleano ]
// Objetivo2: ser usado em condições (será atualizado mais tarde)

// -------------------------------------- CONVERSÃO PARA BOOLEANO --------------------------------------
let nulo = 0
console.log(`[1] O valor ${nulo} para booleano é = ${!!nulo}`)
nulo = 1
console.log(`[2] O valor ${nulo} em booleano é = ${!!nulo}`)
console.log(`[3] O valor ${nulo} em booleano é = ${!nulo} (reversão)`)

// -------------------------------------------- DADOS = true --------------------------------------------
const lista = [1, -2, ' ', [], {}, Infinity]
console.log(
  `
números positivos = = ${!!lista[0]}
números negativos = = ${!!lista[1]}
string com espaço = = ${!!lista[2]}
lista vazia       = = ${!!lista[3]}
objeto vazio      = = ${!!lista[4]}
infinito          = = ${!!lista[5]}
`
)

// ------------------------------------------- DADOS = false -------------------------------------------
const lista2 = [0, '', null, NaN, undefined]
console.log(
  `
número zero  = ${!!lista2[0]}
string vazia = ${!!lista2[1]}
null         = ${!!lista2[2]}
NaN          = ${!!lista2[3]}
undefined    = ${!!lista2[4]}
`
)
