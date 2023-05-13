const form = document.querySelector('#login-form');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = form.querySelector('#email').value;
    const password = form.querySelector('#password').value;

    const data = {
        email,
        password
    };

    fetch('http://127.0.0.1:5001/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if(data.status === 'True'){
                alert("Login Successful!");
                window.location.href = 'index.html';
            }
            else{
                alert("Login failed! Check your details and try again.");
                throw new Error('Wrong Credentials Entered!');
            }
        })
        .catch(error => {
            console.error(error);
        });
});