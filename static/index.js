document.addEventListener('DOMContentLoaded', function() {
    fetchUserData();
});

document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this); 
    var userData = {
        username: formData.get('username'),
        email: formData.get('email')
    };
    console.log("Sending", userData)
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify(userData),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('User info submitted successfully!');
    })
});
