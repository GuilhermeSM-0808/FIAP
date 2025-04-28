function requestName(){
    let name = prompt("Insert your name: ")
    return name
}

function requestAge(){
    let age = prompt("Insert your age: ")
    return age
}

function Message(name, age){
    alert(`Hello ${name}, you are ${age} years old.`)
}

function startApp(){
    let name = requestName()
    let age = requestAge()
    Message(name, age)
}

startApp()