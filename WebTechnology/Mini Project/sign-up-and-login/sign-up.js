const form = document.querySelector('#signup-form');


form.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = form.querySelector('#email').value;
    const password = form.querySelector('#password').value;

    const data = {
        email,
        password
    };

    fetch('http://127.0.0.1:5001/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if(data.registered === 'True'){
                alert("Registration Successful!")
                window.location.href = 'index.html';
            }
            else{
                alert(data.result);
                throw new Error('Wrong Credentials Entered!');
            }
        })
        .catch(error => {
            console.error(error);
        });
});