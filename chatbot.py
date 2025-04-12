import random
import nltk
from nltk.chat.util import Chat, reflections
import re
import ast

pares = [
    [ r"oi",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"olá",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"ei",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"bom dia",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"boa tarde",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"boa noite",["Oi, sou o MatBot, o chat que te ajuda com operações matemáticas!"],],
    [ r"quanto é (.*)\?",["O resultado é:"],],
    [ r"quanto é (.*)",["O resultado é:"],],
    [r"Nenhuma operação",["Não entendi, por favor digite uma operação!"],],
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
    operacao = ''
    simboloInvalido = False
    expressao = re.findall('.',user_input)
    print (expressao)
    for i in expressao:
        if i in ['=','^','%',',']:
            simboloInvalido = True
        elif i in ['+','-','*','/','.'] or i.isdigit():
            operacao = operacao + i
    print(operacao)
    if simboloInvalido:
        print("Símbolo Inválido Utilizado. Símbolos Válidos: +, -, /, *. Use ponto em vez de vírgula para números decimais.")
    elif operacao != '':
        resultado = eval(operacao)
        response = chatbot.respond(user_input.lower())
        if response:
            print("MatBot: ", response, resultado)
        else:
            print("MatBot: ", resultado)
    elif operacao == '':
        if user_input in ['oi','olá','ei','bom dia','boa tarde','boa noite']:
            response = chatbot.respond(user_input.lower())
            print("MatBot: ", response)
        else:
            response = chatbot.respond("Nenhuma operação")
            print("MatBot: ", response)


