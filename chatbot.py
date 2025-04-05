import random
import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [ r"Oi | Olá",["Oi, como posso te ajudar?", "Olá"],],
    [],
]

reflexoes = {
    "eu":"você",
}

chatbot = Chat(pares, reflections)

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("MatBot: Adeus!")
        break
    response = chatbot.respond(user_input)
    print("MatBot: ", response)