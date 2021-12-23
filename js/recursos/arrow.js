

// Módulo:   arrow.js
// Aparição: aula_22._Usando_Template_Strings.js
// Objetivo: criar função com sintaxe do tipo [ flecha ]


// ---------------------------------------------- TUTORIAL ----------------------------------------------
// const = declaração
// cacha_alta           = nome da função
// string               = nome de parâmetro
// =>                   = retorno (como 'return' em Python)
// string.toUpperCase() = ação da função

const cacha_alta = string => string.toUpperCase()          // função arrow
console.log(cacha_alta('string'))                          // chamada da função arrow
console.log(`quero aprender ${cacha_alta('javascript')}!`) // chamada da função arrow em template string
const eu = cacha_alta('Lucas Farias')
const frase = `${eu} é um aprendiz`
console.log(frase)
