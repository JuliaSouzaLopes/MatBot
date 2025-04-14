document.addEventListener("DOMContentLoaded", startApp)

function startApp() {
    handleActions();
}


function handleActions() {

    document.getElementById("send-btn").addEventListener("click", async function() {
        let userMessage = document.getElementById("user-input").value;
    
        if (userMessage.trim() === "") {
            alert("O campo de entrada está vazio!");
            return;
        }
    
        await fetch("http://127.0.0.1:5000/enviaMensagem",{
            method: "POST",
            body: JSON.stringify({Mensagem:userMessage}),
            headers: {"Content-Type":"application/json"}
        }).then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Erro na resposta do servidor");
            }
        }).then((data) => {
            let chatBox = document.getElementById("chat-box");
            let userDiv = document.createElement("div");
            userDiv.textContent = "Você: " + userMessage;
            chatBox.appendChild(userDiv);

            let botDiv = document.createElement("div");
            botDiv.textContent = "MatBot: " + data.resultado;
            chatBox.appendChild(botDiv);

            document.getElementById("user-input").value = "";
            chatBox.scrollTop = chatBox.scrollHeight;
        }).catch((error) => {
            console.error("Erro:", error);
        });
    });

}

