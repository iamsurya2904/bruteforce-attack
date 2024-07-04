script.js
function bruteForceDecrypt() {
    const message = document.getElementById('message').value;

    fetch('http://127.0.0.1:5000/bruteforce', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        const outputElement = document.getElementById('output');
        outputElement.textContent = data.result.join('\n');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
