

// Módulo: aula_16_o_basico_de_Var,Let_e_Const.js
// Aula: 16. O Básico de Var, Let e Const

const palavras_reservadas = ['var', 'let', 'const']
var linguagem = 'JS' // palavra reservada id = tipo/classe
let nulo = 0         // idem

// PERGUNTA: Qual a diferença entre [ var ] e [ let ]?
// RESPOSTA: [ var ], permite redeclaração, e se isso for tentando em [ let ], gera-se erro

// PERGUNTA: Qual a diferença entre [ var ], [ let ] e [ const ]?
// RESPOSTA: [ const ] não permite, de forma alguma, que uma variável mude, nem classe, nem valor

// ----------------------------------------------- OBS -----------------------------------------------
// Foi apontado que [ var ] e [ let ] são de mesma função, mas é preferencial usar [ let ]'
// [ var ] permite redeclaração, enquanto [ let ] não
// [ var ] ou [ let ] permitem reatribuir valores, após sua declaração
// [ const ] não permite nem redeclarar, muito menos reatribuir
