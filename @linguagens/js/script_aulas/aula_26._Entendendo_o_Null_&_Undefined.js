

// Módulo: aula_26._Entendendo_o_Null_&_Undefined.js
// Aula: 26. Entendendo o Null & Undefined

let dados = {nome: 'Carlos'} // ao declarar uma variável, é criado um endereço de memória para ela
console.log('A', dados)
let dados2 = dados           // esse tipo de declaração faz com que variáveis de nomes != ocupem o mesmo endereço 
console.log('B', dados2)


dados2.nome = 'Alfredo' // mas como essa variável é um clone, alterações nela afetam a outra também
console.log('A', dados)
console.log('B', dados2)

// O lógica aplicada acima não funciona para classe [ number ]
let numero = 0
let numero2 = numero
console.log(`A variável chamada [numero2] têm valor atual de: ${numero2}`)
numero2++ // incrementação
console.log(`A variável chamada [numero2] têm valor atual de: ${numero2}`)
console.log(`A variável chamada [numero] têm valor atual de: ${numero}`)
