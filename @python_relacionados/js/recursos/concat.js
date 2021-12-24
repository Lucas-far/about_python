/*
!@# recursos

------- AULA -------
O curso foi modificado. Aula não identificada

------- DETALHE -------
Mesclar caracteres entre variáveis [ strings ]

------- LEGENDAS -------
1. Forma padrão de concatenar
2. Forma de concatenar por método
3. Uso do método de forma múltipla em linha
4. Caso de concatenação com tipos diferentes (No Javascript, é permitido)
*/

const nome = 'Ana'
const sobrenome = 'Banana'
const complemento = 'é doida'

console.log('[1] ' + nome + ' ' + sobrenome) // 1
console.log('[2] ' + nome.concat(' ', sobrenome)) // 2
console.log('[3] ' + nome.concat(' ', sobrenome).concat(' ', complemento)) // 3
console.log('3' + 2) // 4
