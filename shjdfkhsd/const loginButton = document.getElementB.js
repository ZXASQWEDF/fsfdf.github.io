const loginButton = document.getElementById('login')
const passwordInput = document.getElementById('password')
const resultOutput = document.getElementById('result')

function login() {
    resultOutput.style.color = '#00f'
    resultOutput.innerText = 'Login..'
    setTimeout(function() {
        const passwordInput = accountInput.value

        if (
            passwordValue === '664089') {
            resultOutput.style.color = '#0f0'
            window.location.href = 'https://jackyhoi.github.io/fsfdf.github.io/shjdfkhsd/ppp.html';

        } else {
            resultOutput.style.color = '#f00'
            resultOutput.innerText = '帳號或密碼不正確'
        }
    }, 2000)
}

//防止页面后退
history.pushState(null, null, document.URL);
window.addEventListener('popstate', function() {
    history.pushState(null, null, document.URL);
});



loginButton.addEventListener('click', login) // JavaScript Document