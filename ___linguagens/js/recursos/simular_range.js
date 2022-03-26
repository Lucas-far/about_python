// Criar valores aleatórios não inteiros
// Valores variam de acordo com os valores multiplicados ao "Math.random()"
// O exemplo abaixo mostrar valores entre: -2 até 2

let box = []

for (let i = 0; i < 50; i++) {
  box.push(Math.random() * 4 - 2)
}

console.log(box)
console.log('--------------- BLOCO ---------------')

// Os valores podem ser restringidos

let box2 = []

for (let i = 0; i < 50; i++) {
  let value = Math.random() * 4 - 2
  if (value > 1) {
    box2.push(value)
  }
}

console.log(box2)
