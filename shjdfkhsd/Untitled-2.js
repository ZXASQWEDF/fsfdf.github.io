const loginButton = document.getElementById('login')
const accountInput = document.getElementById('account')
const passwordInput = document.getElementById('password')
const resultOutput = document.getElementById('result')

function login() {
    resultOutput.style.color = '#00f'
    resultOutput.innerText = 'Login..'
    setTimeout(function() {
        const accountValue = accountInput.value
        passwordValue = passwordInput.value
        if (accountValue === 's123456' &&
            passwordValue === '123456') {
            resultOutput.style.color = '#0f0'
            window.location.href = 'https://jackyhoi.github.io/fsfdf.github.io/shjdfkhsd/clock.html';
        } else {
            resultOutput.style.color = '#f00'
            resultOutput.innerText = '請用戶帳號是否正確'
        }
    }, 2000)
}
loginButton.addEventListener('click', login) // JavaScript Document