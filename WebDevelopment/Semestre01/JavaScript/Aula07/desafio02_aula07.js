//Calculate age based on given birth year

const currentDate = new Date()

function calculateAge(){
    let birth_year = prompt("Insert your birthyear: ")
    let current_year = currentDate.getFullYear()
    age = current_year - birth_year
    return age
}

alert(`You are or will be ${calculateAge()} this year!`)