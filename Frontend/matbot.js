// import getBotResponse from '../';

// document.getElementById("send-btn").addEventListener("click", function() {
//     let userMessage = document.getElementById("user-input").value;
//     if (userMessage.trim() === "") return;

//     let chatBox = document.getElementById("chat-box");
//     let userDiv = document.createElement("div");
//     userDiv.textContent = "Você: " + userMessage;
//     chatBox.appendChild(userDiv);

//     let botResponse = document.createElement("div");
//     botResponse.textContent = getBotResponse(userMessage);
//     chatBox.appendChild(botResponse);

//     document.getElementById("user-input").value = "";
//     chatBox.scrollTop = chatBox.scrollHeight;
// });

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
    
        await fetch("http://127.0.0.1:3000/enviaMensagem",{
            mode:'no-cors',
            method: "POST",
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
            botDiv.textContent = "Bot: " + data.resultado;
            chatBox.appendChild(botDiv);

            document.getElementById("user-input").value = "";
            chatBox.scrollTop = chatBox.scrollHeight;
        }).catch((error) => {
            console.error("Erro:", error);
        });
    });

}

