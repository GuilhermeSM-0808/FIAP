function getName() {
    let name = "Foobar"
    return name
}

function showName(UserName, NickName) {
    UserName
    let result = getName()
    console.log(result)
}

showName("Foobar", "Qux")

function sumTwoNumbers(firstNumber = 0, SecondNumber = 0) {
    return firstNumber + SecondNumber
}

console.log(sumTwoNumbers(5, 17))
console.log(sumTwoNumbers(47))

const sumNumbers = (num1, num2) => num1 + num2

const sumNumb = (num1) => console.log(num1)