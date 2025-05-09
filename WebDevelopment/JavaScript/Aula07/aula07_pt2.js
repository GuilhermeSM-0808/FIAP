let nome = "Foobar   "
console.log(nome.length)
console.log(nome.toLocaleUpperCase())
console.log(nome.toLocaleLowerCase())
console.log(nome.includes("f"))
console.log(nome.includes("F"))
console.log(nome)
console.log(nome.trim())

let num = 5.5555555555
console.log(num.toFixed(2))
console.log(isNaN(num)) //Falso para ele "Não ser um numero" (pq ele é um numero)

console.log(Math.random())
console.log(Math.random()*11) //Sortear um numero entre 1 e 10 (arredondar para baixo)
console.log(Math.floor(Math.random()*11)) //Math.floor arredonda para baixo
console.log(Math.ceil(Math.random()*10)) //Math.floor arredonda para baixo
console.log(Math.floor(Math.random()*11)) //Math.ceil arredonda para cima
console.log(Math.round(Math.random()*10)) //Math.round arredonda para o mais perto

const currentDate = new Date()
console.log(currentDate)
console.log(currentDate.getHours())
console.log(currentDate.getMinutes())
console.log(currentDate.getDay())
console.log(currentDate.getMonth())
console.log(currentDate.getFullYear())




