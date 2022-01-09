// !@# [C:\Users\lucasf\PycharmProjects\python_everything\@python_relacionados\js\recursos\mathpow.js]
// 1. Variáveis para verificação em condição
// 2. Variáveis em uso nas condições
// 3. Uso de sintaxe que cumpre o mesmo papel do método
// 4. Uso normal do método

function calcularPotencia(valor, elevarQtd, reduzido, casasQtd) {
  let tipoValor = String(typeof valor) // 1
  let tipoValor2 = String(typeof elevarQtd) // 1
  let tipoCasa = String(typeof casasQtd) // 1

  // 2
  if (
    tipoValor == 'number' &&
    tipoValor2 == 'number' &&
    reduzido == true &&
    tipoCasa == 'number'
  ) {
    return Math.pow(valor, elevarQtd).toFixed(casasQtd)
  } else {
    return 'Os parâmetros 1 e 2 devem ser inteiros ou flutuantes. Deve ser informado se quer uma redução de casas decimais e a quantidade de casas decimais'
  }
}

console.log(
  calcularPotencia(
    (valor = 7.7),
    (elevarQtd = 2),
    (reduzido = true),
    (casasQtd = 2)
  )
)
console.log(
  calcularPotencia(
    (valor = 7.7),
    (elevarQtd = ''),
    (reduzido = false),
    (casasQtd = 2)
  )
)

console.log('Alternativo           ||', 2.7 * 2.7) // 3
console.log('Alternativo           ||', 2.7 * 2.7 * 2.7) // 3
console.log('Método fora de função ||', Math.pow(2.7, 3)) // 4
console.log('Método fora de função ||', Math.pow(2.7, 3.9)) // 4
