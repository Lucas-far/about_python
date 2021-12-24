// Aparição: 24. Tipos em JavaScript: Array

// Declaração de um array (contagem de índice do 0)
const lista = [1, 2, 3]

console.log(`Índice 0: ${lista[0]}`)
console.log(`Índice 1: ${lista[1]}`)
console.log(`Índice 2: ${lista[2]}`)
console.log(`Índice 3: ${lista[3]}`) // índice inexistente gera = undefined

// Alteração de um índice
lista[0] = 'um'

// Adição de um índice
lista[3] = 'quatro'

// Adição de um índice (quando o índice especificado têm + de 1 de distância do último índice)
// É gerado: <empty items>
lista[5] = 'seis'

// Resultado
console.log(lista)

// ------- Arquivos relacionados à ARRAY -------
// ver [recursos/length.js ]
// ver [recursos/push.js ]
// ver [recursos/pop.js ]
