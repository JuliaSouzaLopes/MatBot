import random
import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [ r"Oi | Olá",["Oi, sou o MatBot, o chat que te ajuda à aprender a tabuada!", "Olá, sou o MatBot, o chat que te ajuda à aprender a tabuada!"],],
    [r"Qual a tabuada do 1?",["A tabuada do 1 é: 1 x 1 = 1, 1 x 2 = 2, 1 x 3 = 3, 1 x 4 = 4, 1 x 5 = 5, 1 x 6 = 6, 1 x 7 = 7, 1 x 8 = 8, 1 x 9 = 9"],],
    [r"Qual a tabuada do 2?",["A tabuada do 2 é: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6, 2 x 4 = 8, 2 x 5 = 10, 2 x 6 = 12, 2 x 7 = 14, 2 x 8 = 16, 2 x 9 = 18"],],
    [r"Qual a tabuada do 3?",["A tabuada do 3 é: 3 x 1 = 3, 3 x 2 = 6, 3 x 3 = 9, 3 x 4 = 12, 3 x 5 = 15, 3 x 6 = 18, 3 x 7 = 21, 3 x 8 = 24, 3 x 9 = 27"],],
    [r"Qual a tabuada do 4?",["A tabuada do 4 é: 4 x 1 = 4, 4 x 2 = 8, 4 x 3 = 12, 4 x 4 = 16, 4 x 5 = 20, 4 x 6 = 24, 4 x 7 = 28, 4 x 8 = 32, 4 x 9 = 36"],],
    [r"Qual a tabuada do 5?",["A tabuada do 5 é: 5 x 1 = 5, 5 x 2 = 10, 5 x 3 = 15, 5 x 4 = 20, 5 x 5 = 25, 5 x 6 = 30, 5 x 7 = 35, 5 x 8 = 40, 5 x 9 = 45"],],
    [r"Qual a tabuada do 6?",["A tabuada do 6 é: 6 x 1 = 6, 6 x 2 = 12, 6 x 3 = 18, 6 x 4 = 24, 6 x 5 = 30, 6 x 6 = 36, 6 x 7 = 42, 6 x 8 = 48, 6 x 9 = 54"],],
    [r"Qual a tabuada do 7?",["A tabuada do 7 é: 7 x 1 = 7, 7 x 2 = 14, 7 x 3 = 21, 7 x 4 = 28, 7 x 5 = 35, 7 x 6 = 42, 7 x 7 = 49, 7 x 8 = 56, 7 x 9 = 63"],],
    [r"Qual a tabuada do 8?",["A tabuada do 8 é: 8 x 1 = 8, 8 x 2 = 16, 8 x 3 = 24, 8 x 4 = 32, 8 x 5 = 40, 8 x 6 = 48, 8 x 7 = 56, 8 x 8 = 64, 8 x 9 = 72"],],
    [r"Qual a tabuada do 9?",["A tabuada do 9 é: 9 x 1 = 9, 9 x 2 = 18, 9 x 3 = 27, 9 x 4 = 36, 9 x 5 = 45, 9 x 6 = 54, 9 x 7 = 63, 9 x 8 = 72, 9 x 9 = 81"],],
    [r"Quanto é 1 x 1?",["1 x 1 é igual a 1."],],
    [r"Quanto é 1 x 2? | Quanto é 2 x 1?",["1 x 2 ou 2 x 1 é igual a 2."],],
    [r"Quanto é 1 x 3? | Quanto é 3 x 1?",["1 x 3 ou 3 x 1 é igual a 3."],],
    [r"Quanto é 1 x 4? | Quanto é 4 x 1?",["1 x 4 ou 4 x 1 é igual a 4."],],
    [r"Quanto é 1 x 5? | Quanto é 5 x 1?",["1 x 5 ou 5 x 1 é igual a 5."],],
    [r"Quanto é 1 x 6? | Quanto é 2 x 6?",["1 x 6 ou 6 x 1 é igual a 6."],],
    [r"Quanto é 1 x 7? | Quanto é 7 x 1?",["1 x 7 ou 7 x 1 é igual a 7."],],
    [r"Quanto é 1 x 8? | Quanto é 8 x 1?",["1 x 8 ou 8 x 1 é igual a 8."],],
    [r"Quanto é 1 x 9? | Quanto é 9 x 1?",["1 x 9 ou 9 x 1 é igual a 9."],],
    [r"Quanto é 2 x 2?",["2 x 2 é igual a 4."],],
    [r"Quanto é 2 x 3? | Quanto é 3 x 2?",["2 x 3 ou 3 x 2 é igual a 6."],],
    [r"Quanto é 2 x 4? | Quanto é 4 x 2?",["2 x 4 ou 4 x 2 é igual a 8."],],
    [r"Quanto é 2 x 5? | Quanto é 5 x 2?",["2 x 5 ou 5 x 2 é igual a 10."],],
    [r"Quanto é 2 x 6? | Quanto é 6 x 2?",["2 x 6 ou 6 x 2 é igual a 12."],],
    [r"Quanto é 2 x 7? | Quanto é 7 x 2?",["2 x 7 ou 7 x 2 é igual a 14."],],
    [r"Quanto é 2 x 8? | Quanto é 8 x 2?",["2 x 8 ou 8 x 2 é igual a 16."],],
    [r"Quanto é 2 x 9? | Quanto é 9 x 2?",["2 x 9 ou 9 x 2 é igual a 18."],],
    [r"Quanto é 3 x 3?",["3 x 3 é igual a 9."],],
    [r"Quanto é 3 x 4? | Quanto é 4 x 3?",["3 x 4 ou 4 x 3 é igual a 12."],],
    [r"Quanto é 3 x 5? | Quanto é 5 x 3?",["3 x 5 ou 5 x 3 é igual a 15."],],
    [r"Quanto é 3 x 6? | Quanto é 6 x 3?",["3 x 6 ou 6 x 3 é igual a 18."],],
    [r"Quanto é 3 x 7? | Quanto é 7 x 3?",["3 x 7 ou 7 x 3 é igual a 21."],],
    [r"Quanto é 3 x 8? | Quanto é 8 x 3?",["3 x 8 ou 8 x 3 é igual a 24."],],
    [r"Quanto é 3 x 9? | Quanto é 9 x 3?",["3 x 9 ou 9 x 3 é igual a 27."],],
    [r"Quanto é 4 x 4? | Quanto é 4 x 4?",["4 x 4 é igual a 16."],],
    [r"Quanto é 4 x 5? | Quanto é 5 x 4?",["4 x 5 ou 5 x 4 é igual a 20."],],
    [r"Quanto é 4 x 6? | Quanto é 6 x 4?",["4 x 6 ou 6 x 4 é igual a 24."],],
    [r"Quanto é 4 x 7? | Quanto é 7 x 4?",["4 x 7 ou 7 x 4 é igual a 28."],],
    [r"Quanto é 4 x 8? | Quanto é 8 x 4?",["4 x 8 ou 8 x 4 é igual a 32."],],
    [r"Quanto é 4 x 9? | Quanto é 9 x 4?",["4 x 9 ou 9 x 4 é igual a 36."],],
    [r"Quanto é 5 x 5?",["5 x 5 é igual a 25."],],
    [r"Quanto é 5 x 6? | Quanto é 6 x 5?",["5 x 6 ou 6 x 5 é igual a 30."],],
    [r"Quanto é 5 x 7? | Quanto é 7 x 5?",["5 x 7 ou 7 x 5 é igual a 35."],],
    [r"Quanto é 5 x 8? | Quanto é 8 x 5?",["5 x 8 ou 8 x 5 é igual a 40."],],
    [r"Quanto é 5 x 9? | Quanto é 9 x 5?",["5 x 9 ou 9 x 5 é igual a 45."],],
    [r"Quanto é 6 x 6?",["6 x 6 é igual a 36."],],
    [r"Quanto é 6 x 7? | Quanto é 7 x 6?",["6 x 7 ou 7 x 6 é igual a 42."],],
    [r"Quanto é 6 x 8? | Quanto é 8 x 6?",["6 x 8 ou 8 x 6 é igual a 48."],],
    [r"Quanto é 6 x 9? | Quanto é 9 x 6?",["6 x 9 ou 9 x 6 é igual a 54."],],
    [r"Quanto é 7 x 7?",["7 x 7 é igual a 49."],],
    [r"Quanto é 7 x 8? | Quanto é 8 x 7?",["7 x 8 ou 8 x 7 é igual a 56."],],
    [r"Quanto é 7 x 9? | Quanto é 9 x 7?",["7 x 9 ou 9 x 7 é igual a 63."],],
    [r"Quanto é 8 x 8?",["8 x 8 é igual a 64."],],
    [r"Quanto é 8 x 9? | Quanto é 9 x 8?",["8 x 9 ou 9 x 8 é igual a 72."],],
    [r"Quanto é 9 x 9?",["9 x 9 é igual a 81."],],
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