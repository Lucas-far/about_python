/*
!@#

------- AULA -------
28. Desafio Área da Circunferência - Resposta

------- LEGENDAS -------
1. Suposição de valor para um raio
2. PI com casas decimais abreviadas (nesse contexto: 2)
3. Cáclulo de raio de uma circunferência de forma mais dinâmica
4. Cáclulo de raio de uma circunferência de forma mais crua
*/

let raio = 10 // 1
const piValor = Math.PI.toFixed(2) // 2
let calculo = piValor * Math.pow(raio, 2) // 3
let calculo2 = piValor * raio * raio // 4

console.log('[1] ' + piValor)
console.log('[2] ' + calculo)
console.log('[3] ' + calculo2)
