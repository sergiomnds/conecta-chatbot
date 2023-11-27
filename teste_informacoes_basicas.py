import unittest
from robo import *


class TesteInformacoesBasicas(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def teste_servico(self):
        mensagens = ["quais bairros a conecta oferece serviço?",
                     "me fale os bairros que a conecta oferece serviço"]

        for mensagem in mensagens:
            print(f"testando a pergunta: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Conecta cobre toda a cidade de Vitória da Conquista, exceto: Bairro Brasil e Candeias.", resposta.text)

    def teste_pagar(self):
        mensagens = ["quais são as opções de pagamento disponíveis para minha fatura de internet?",
                     "como posso pagar minha fatura?"]

        for mensagem in mensagens:
            print(f"testando a pergunta: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Você pode pagar sua fatura através do boleto bancário, cartão de crédito ou débito automático. Entre em contato com um vendedor para mais informações.", resposta.text)

    def testar_planos(self):
        mensagens = ["quais os planos de internet disponíveis?",
                     "quais planos a conecta tem?"]

        for mensagem in mensagens:
            print(f"testando a pergunta: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Conecta oferece planos de 100, 200 e 300 megas. Custando respectivamente R$ 99,90, R$ 119,90 e R$ 139,90.", resposta.text)

    def testar_senha(self):
        mensagens = ["como faço para mudar a senha do wi-fi?",
                     "quero mudar a senha do wi-fi"]

        for mensagem in mensagens:
            print(f"testando a pergunta: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Você pode chamar um técnico para fazer a alteração da senha do seu Wi-Fi, sem custo. Entre em contato com um vendedor e solicite a visita de um técnico.", resposta.text)

    def testar_instalacao(self):
        mensagens = ["quanto custa a instalação da internet?",
                     "quanto é para instalar a internet?"]

        for mensagem in mensagens:
            print(f"testando a pergunta: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A instalação da internet é gratuita. Após a contratação, um técnico irá até sua residência para fazer a instalação.", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)
