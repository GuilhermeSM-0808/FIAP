const btnClicar = document.getElementById("btnClicar")

const form = document.getElementById("form")
const inputNome = document.getElementById("nome")
const inputEmail = document.getElementById("email")
const inputAssunto = document.getElementById("assunto")
const inputMensagem = document.getElementById("mensagem")
const btnEnviar = document.getElementById("btnEnviar")
const msgErro = document.getElementById("msgErro")
const cadastro = document.getElementById("cadastros")

//Multiplas maneiras de escrever a mesma função:

// btnClicar.addEventListener("click",function clicar(){
//     alert("Clicou!")
// })

// btnClicar.addEventListener("click",function (){
//     alert("Clicou pelo Javascript!")
// })

// btnClicar.addEventListener("click", () => {
//     alert("Clicou pelo Javascript!")
// })

// btnClicar.addEventListener("click",function (){
//     paragrafo.textContent = "Foobar Qux"
// })

btnClicar.addEventListener("click", function () {
    paragrafo.textContent = `${paragrafo.textContent === 'Guilherme S.M.' ? 'Foobar Qux' : 'Guilherme S.M.'}`
})


//Form section

btnEnviar.addEventListener("click", function (event) {

    event.preventDefault()
    let nome = inputNome.value
    let email = inputEmail.value
    let assunto = inputAssunto.value
    let mensagem = inputMensagem.value

    if (nome === '' || email === '' || mensagem === '') {
        msgErro.textContent = "Preencha os campos vazios!"
        msgErro.style.color = "#ff0000"
        // msgErro.classList.add('msgVermelha') //<-- adicionar style definido no arquivo CSS ao texto
        // msgErro.setAttribute("src","'link da imagem'") // <-- Alterar 'src' do elemento
        // msgErro.src = "link"
        return
    }

    // alert(`Nome: ${nome}\nE-mail: ${email}\nAssunto: ${assunto}\nMensagem: ${mensagem}`)


    const cardUsuario = document.createElement('div')
    cardUsuario.innerHTML = `
    <h3> Nome: ${nome} </h3>
    <p> E-mail: ${email} </p>
    <p> Assunto: ${assunto} </p>
    <p> Mensagem: ${mensagem} </p>
    <hr>
    `

    cadastro.append(cardUsuario)


    form.reset()

})