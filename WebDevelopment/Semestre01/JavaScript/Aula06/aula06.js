prompt("Insert your name: ")

console.log(0 == 0)
console.log("0" == 0)
console.log("0" === 0)

console.log("uva" > "banana")
console.log("Uva" > "banana")

if (nome === "Mario"){
    console.log("It's me!")
}
else if(nome === "Gui"){
    console.log("It's you!")
}
else {
    console.log("Unkown person.")
}

nome === "Mario" ? console.log("Yahooo!") : console.log("Oh noo")

if (nome === "Mario" || nome === null || nome === "Foobar " || nome === "Gui"){
    console.log("VIP logged in")
}