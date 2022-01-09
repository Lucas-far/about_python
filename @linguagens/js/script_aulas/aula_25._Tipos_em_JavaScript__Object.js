

// Módulo: aula_25._Tipos_em_JavaScript:_Object.js
// Aula: 25. Tipos em JavaScript: Object

// --------------------------------------- DECLARAÇÃO DE OBJETO ---------------------------------------
// classe [ Object ] em Javascript parece ser o equivalente a [ dict ] no Python
let obj = {}
console.log(obj)
 
// -------------------------------- CRIAÇÃO DE CHAVE POR NOTAÇÃO PONTO --------------------------------
// SINTAXE: var.chave = valor
// OBS: variáveis do tipo [ Object ] aparentemente não podem ser postas em [ template string ] 
obj.nome = 'Alfredo'
obj.sobrenome = 'Henrique'
console.log(obj)

// ----------------------------------- CRIAÇÃO DE CHAVE POR ÍNDICE -----------------------------------

// OBS: sintaxe igual a do Python, porém foi recomendado que fosse evitada
// OBS: No Python: criar chave/valor e editar chave/valor
// OBS: No Javascript: criar chave/valor
obj['idade'] = 41
console.log(obj)

// ----------------------------------- CRIAÇÃO DE CHAVE EM ESCOPO -----------------------------------
let obj2 = {
    nome: 'Alfredo',
    sobrenome: 'Henrique'
}
console.log(obj2)

// --------------------------- CRIAÇÃO DE CHAVE EM ESCOPO (OBJETO ANINHADO) ---------------------------
// OBS: Parece que cria-se chaves sempre sem especificar um tipo
// OBS: Talvez o motivo seja diminuir a complexidade de distinção entre chave e valor
let this_obj = {
    obj1: {
        título: 'objeto aninhado 1',
        obj2: {
            título: 'objeto aninhado 2',
            obj3: 'fim'
        }
    }
}

// extraindo os dados em Javascripts
console.log('====================')
console.log([1], this_obj)
console.log([2], this_obj.obj1)
console.log([3], this_obj.obj1.obj2)
console.log([4], this_obj.obj1.obj2.obj3)
console.log([5], this_obj.obj1.título)
console.log([6], this_obj.obj1.obj2.título)
