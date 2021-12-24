/*
!@# recursos

------- AULA -------
O curso foi modificado. Aula não identificada

------- DETALHE -------
Encontrar a posição de um caractere numa classe [ string ] e retornar seu código inteiro

------- LEGENDAS -------
1. Se o índice é excedente, o retorno = NaN
2. Uso em dados literais é permitido
*/

const palavra = '_@^L2' // essa constante têm 4 índices (contagem de índice inicia do zero)

console.log(`Caractere: _ possui código = ${palavra.charCodeAt(0)}`)
console.log(`Caractere: @ possui código = ${palavra.charCodeAt(1)}`)
console.log(`Caractere: ^ possui código = ${palavra.charCodeAt(2)}`)
console.log(`Caractere: L possui código = ${palavra.charCodeAt(3)}`)
console.log(`Caractere: 2 possui código = ${palavra.charCodeAt(4)}`)
console.log(`Caractere:   possui código = ${palavra.charCodeAt(5)}`) // 1
console.log('Pamonha'.charCodeAt(2)) // 2
