

// Módulo: concat.js
// Aparição: aula_21._Tipos_em_JavaScript:_String.js
// Objetivo: mesclar caracteres de vars [ strings ] distintas

const nome = 'Lucas'
const sobrenome = 'Pacheco'
console.log([1], nome.concat(' ', sobrenome)) // é melhor adicionar um espaço
console.log([2], nome + ' ' + sobrenome)      // forma alternativa de concatenar

// Método pode ser usado multiplamente
const complemento = 'Saraiva'
console.log([3], nome.concat(' ', sobrenome).concat(' ', complemento))

// Concatenação estranha
console.log('3' + 2) // mesmo sendo classes diferentes, há a concatenação
