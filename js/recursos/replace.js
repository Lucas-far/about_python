

// Módulo: replace.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: substituir caractere de uma [ string ], sendo par1=dado atual / par2=dado novo

const nome = 'Henrique_7'

console.log(nome.replace('c', 'v'))
console.log(nome.replace(7, 'sete')) // parâmetro numérico pode ser passado sem ser [ string ]

const dado = 'Henrique: 190.299.043-17'
console.log(dado.replace(/\d/, '*'))
console.log(dado.replace(/\d/g, '*')) // substituir todos chars numéricos por 1 char)
console.log(dado.replace(/\w/, '*'))
console.log(dado.replace(/\w/g, '*')) // substituir todos chars não especiais por 1 char)
