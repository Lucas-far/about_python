// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\pop.js]

function removerUltimo(lista) {
  let verificacao = String(typeof lista)

  if (verificacao == 'object') {
    let mensagem = `Da lista [${lista}], foi removido o item ['${lista.pop()}']`
    let resultado = ` .Tornando-se [${lista}]`
    return mensagem + resultado
  } else {
    return 'Parâmetro informado não é uma lista.'
  }
}

console.log(
  removerUltimo((lista = [true, false, NaN, null, undefined, Infinity]))
)
console.log(removerUltimo((lista = 'javascript')))
console.log('Uso do método fora de uma função:', ['', ' ', 'a'].pop())
