const API_BASE_URL = "http://localhost:8000/api"; // Nginx routes this to backend

async function checkHealth() {
    try {
        const res = await fetch(`${API_BASE_URL}/health`);
        const data = await res.json();
        document.getElementById("health-status").innerText = `Backend Status: ${data.status} (Env: ${data.environment})`;
    } catch (e) {
        document.getElementById("health-status").innerText = "Backend is Offline";
        document.getElementById("health-status").style.color = "red";
    }
}

async function fetchMessages() {
    try {
        const res = await fetch(`${API_BASE_URL}/messages`);
        const data = await res.json();
        const list = document.getElementById("message-list");
        list.innerHTML = "";
        data.messages.forEach(msg => {
            const li = document.createElement("li");
            li.innerText = msg.text;
            list.appendChild(li);
        });
    } catch (e) {
        console.error("Error fetching messages", e);
    }
}

async function postMessage() {
    const input = document.getElementById("new-message");
    const text = input.value.trim();
    if (!text) return;

    try {
        await fetch(`${API_BASE_URL}/messages`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
        });
        input.value = "";
        fetchMessages(); // Refresh the list
    } catch (e) {
        console.error("Error posting message", e);
    }
}

// Run on load
window.onload = () => {
    checkHealth();
    fetchMessages();
};
