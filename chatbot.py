import random
import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [ r"Oi",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"Olá",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"Quanto é ()?",["Resposta"],],
    [r"()",["Não Entendi, por favor use o formato: quanto é (operação)."],],
    [r"(.*)\?",["Desculpe não entendi a pergunta."],],

]

reflexoes = {
    "eu":"você",
    "meu":"seu",
    "você":"eu",
    "seu":"meu",
    "eu sou":"você é",
    "você é":"eu sou",
    "você estava":"eu estava",
    "eu estava":"você estava"
}

chatbot = Chat(pares, reflections)

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("MatBot: Adeus!")
        break
    response = chatbot.respond(user_input)
    print("MatBot: ", response)
