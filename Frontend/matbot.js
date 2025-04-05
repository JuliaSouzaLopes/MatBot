
document.getElementById("send-btn").addEventListener("click", function() {
    let userMessage = document.getElementById("user-input").value;
    if (userMessage.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    let userDiv = document.createElement("div");
    userDiv.textContent = "Você: " + userMessage;
    chatBox.appendChild(userDiv);

    let botResponse = document.createElement("div");
    botResponse.textContent = "Chatbot: " + getBotResponse(userMessage);
    chatBox.appendChild(botResponse);

    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
});


