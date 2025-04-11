async function sendMessage() {
    const input = document.getElementById("user-input").value;
    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<div><b>You:</b> ${input}</div>`;

    const response = await fetch('/ask-pdf', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ question: input })
    });

    const data = await response.json();

    if (data.answer) {
        chatbox.innerHTML += `<div><b>Bot:</b> ${data.answer}</div>`;
    } else {
        chatbox.innerHTML += `<div><b>Bot:</b> Sorry, I don't know the answer.</div>`;
    }

    document.getElementById("user-input").value = '';
}
