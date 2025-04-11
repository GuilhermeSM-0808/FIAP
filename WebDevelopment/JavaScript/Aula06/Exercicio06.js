let name_input = prompt("Insert your username: ")
let pass_input = prompt("Insert your password: ")

// if (name_input === "1234" && pass_input === "1234") {
//     alert("Login Sucesseful!")
// }
// else {
//     alert("Username or password are incorrect.")
// }

if ((name_input === "Foobar" && pass_input === "Qux") || (name_input === "Gui" && pass_input === "8888") || (name_input === "Mario" && pass_input === "Yippie")) {
    alert("Login Successful!")
}
else {
    alert("Username or password are incorrect.")
}

// IGUAL A LINHA DE CIMA
// if (
//     (name_input === "Foobar" && pass_input === "Qux") || 
//     (name_input === "Gui" && pass_input === "8888") || 
//     (name_input === "Mario" && pass_input === "Yippie")
// ) {
//     alert("Login Successful!")
// }
// else {
//     alert("Username or password are incorrect.")
// }

let nomeFinal = nome || "Visitante"