
document.getElementById('username').addEventListener('blur', function () {
    let username = this.value;

    fetch(`/check-username?username=${encodeURIComponent(username)}`)
        .then(response => response.json())
        .then(data => {
            let feedback = document.getElementById('username-feedback');
            if (data.exists) {
                feedback.textContent = 'Username is already taken.';
                feedback.style.color = 'red';
            } else {
                feedback.textContent = 'Username is available.';
                feedback.style.color = 'green';
            }
        });
});

document.getElementById('create-account-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission to handle via JavaScript

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    // Optional: Add client-side password strength validation
    if (password.length < 8) {
        document.getElementById('password-feedback').textContent = 'Password is too short.';
        return;
    }

    // Submit form data to the server
    fetch('/create-account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Account created successfully!');
                // Redirect or clear form
            } else {
                alert(data.message); // Show server response if account creation fails
            }
        });
});

