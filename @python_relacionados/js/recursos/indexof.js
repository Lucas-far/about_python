/*
!@# recursos

------- AULA -------
O curso foi modificado. Aula não identificada

------- DETALHE -------
Retornar o índice de um caractere em uma classe [ string ]

------- LEGENDAS -------
1. Em caso de caractere repetido, o retorno é o da primeira ocorrência, da esquerda para a direita
2. Retorno -1 caso o caractere procurado, não exista
*/

const palavra = '_Cod3r_'
const bloco = ' |índice| '

console.log(palavra.charAt(0) + bloco + palavra.indexOf('_')) // 1
console.log(palavra.charAt(1) + bloco + palavra.indexOf('C'))
console.log(palavra.charAt(2) + bloco + palavra.indexOf('o'))
console.log(palavra.charAt(3) + bloco + palavra.indexOf('d'))
console.log(palavra.charAt(4) + bloco + palavra.indexOf('3'))
console.log(palavra.charAt(5) + bloco + palavra.indexOf('r'))
console.log(palavra.indexOf('*')) // 2
