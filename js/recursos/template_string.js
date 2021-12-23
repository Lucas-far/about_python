

// Módulo: template_string.js
// Aparição: aula_22._Usando_Template_Strings.js
// Objetivo: inserir dados externos dentro de uma classe [ string ] (como f'' do Python)

// Declaração de constantes, que funcionarão como dados externos
const hoje = '05/02/2020'
const nome = 'Euclides'
const lugar = 'lanchonete'
const comida = 'sorvete'

// Declaração de uma contante, que servirá como receptora dos dados externos
const frase =
`
Hoje são ${hoje}
Oi, eu me chamo ${nome}
eu gosto muito de ir à ${lugar}
pois eu gosto de comer ${comida}
`
console.log(frase)

// Template string não recebe somente declarações, pode receber métodos também
const valor = 7
console.log(`Você sabia que 7 x 7 é ${Math.pow(valor, 2)}?`)
