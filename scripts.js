function addTOTP() {
    let secret = document.getElementById('secret').value.trim();
    let account = document.getElementById('account').value.trim();
    if (!secret || !account) {
        alert("Secret key and account name cannot be empty!");
        return;
    }

    fetch('/add_totp', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ secret: secret, account: account }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.success);
        location.reload();
    })
    .catch(error => {
        alert('Error adding TOTP: ' + error);
    });
}

// Other functions for copying to clipboard, handling TOTP display, etc.
