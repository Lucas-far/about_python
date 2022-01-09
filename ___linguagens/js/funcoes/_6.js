// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\push.js]
// Minha primeira função envolvendo loop for + uso do método [push] para classe [array]
// 1. É preciso ter um tamanho de referência para saber quantos índices o loop percorrerá
// 2. O [i] é o índice, de valor 0, que alcançará o valor referenciado em 1 (que nesse contexto é: 3)
// 3. O [par1] adiciona em si cada dado do [par2] pelo [i], que assume os valores: 0, 1, 2, 3, e após isso, o loop acaba

function addEmLista(alvo, dado) {
  let tamanhoDado = dado.length // 1
  // 2
  for (let i = 0; i < tamanhoDado; i++) {
    alvo.push(dado[i]) // 3
  }
}

let lista = ['', ' ']
console.log(lista)
addEmLista((alvo = lista), (dado = [0, true, false]))
console.log(lista)
