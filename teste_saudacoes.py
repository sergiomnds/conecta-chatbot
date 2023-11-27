import unittest
from robo import *


class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_saudacoes(self):
        saudacoes = ["oi", "olá", "ola", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá! Sou o robô de atendimento da Conecta. Tire suas dúvidas de forma rápida, assim como nossa internet!",
                resposta.text
            )

    def testar_saudacoes02(self):
        saudacoes = ["Bom Dia", "Boa Tarde", "Boa Noite"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                f"{saudacao}! Sou o robô de atendimento da Conecta. Tire suas dúvidas de forma rápida, assim como nossa internet!",
                resposta.text
            )

    def testar_saudacoes03(self):
        saudacoes = ["Bom Dia", "Boa Tarde", "Boa Noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(f"oi, {saudacao.lower()}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                f"{saudacao}! Sou o robô de atendimento da Conecta. Tire suas dúvidas de forma rápida, assim como nossa internet!",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)
