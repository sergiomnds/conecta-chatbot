from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
CONFIANCA_MINIMA = 0.6


def iniciar():
    robo = ChatBot("Robô de Atendimento Conecta",
                   read_only=True,
                   logic_adapters=[
                       {
                           "statement_comparison_function": LevenshteinDistance,
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar_robo(robo):
    while True:
        mensagem = input("Digite alguma coisa... \n")
        resposta = robo.get_response(mensagem.lower())

        if resposta.confidence >= CONFIANCA_MINIMA:
            print(resposta.text + '\n')
        else:
            print(
                "Desculpe, não sei responder esta pergunta. Entre em contato com um vendedor. \n")


if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
