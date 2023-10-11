import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializando a janela
        self.setWindowTitle("Cardápio")
        self.setGeometry(100, 100, 800, 600)

        # Texto
        texto = QLabel("<b>Cardápio do dia:</b>", self)
        texto.setStyleSheet('font-size: 20px;')
        self.cardapio = QLabel("1 - Bacalhau com arroz — R$19,30\n\n 2 - Arroz, feijão e bife acebolado  — R$25,00 \n\n 3 - Macarrão com carne moída  — R$20,70\n\n 4 - Sopa de legumes com pão francês  — R$18,30\n\n 5 - Filé de frango, arroz, feijão e fritas  — R$27,90", self)
        texto.move(40, 50)
        self.cardapio.move(39, 85)

        # Criando um Input
        label = QLabel("<b>Digite o número do pedido: <b/>", self)
        label.move(40, 280)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(40, 310, 300, 30)
        self.lineEdit.setStyleSheet('border-radius: 10px; font-family: Arial;')

        # Botão
        self.btn = QPushButton("Enviar", self)
        self.btn.setGeometry(40, 360, 90, 40)
        self.btn.setStyleSheet('background-color: black; color: white; border-radius: 5px; font-family: Arial; font-weight: bold;')

        # Criar um QLabel para exibir o valor total e o nome do prato
        self.valor_total_label = QLabel("", self)
        self.valor_total_label.setGeometry(40, 400, 400, 90)  # Define a largura e altura desejadas
        self.valor_total_label.setStyleSheet('font-size: 22px; font-family: Arial;')

        # Variáveis para armazenar o valor total e o nome do prato
        self.valor_total = 0.0
        self.nome_prato = ""

        # Conecte o sinal clicked do botão a uma função
        self.btn.clicked.connect(self.calcularValor)

    def calcularValor(self):
        # Esta função é chamada quando o botão é clicado
        valor = self.lineEdit.text()
        opcoes = {
            "1": ("Bacalhau com arroz", 19.30),
            "2": ("Arroz, feijão e bife acebolado", 25.00),
            "3": ("Macarrão com carne moída", 20.70),
            "4": ("Sopa de legumes com pão francês", 18.30),
            "5": ("Filé de frango, arroz, feijão e fritas", 27.90)
        }

        if valor in opcoes:
            prato, preco = opcoes[valor]
            self.nome_prato = prato
            self.valor_total += preco

        self.valor_total_label.setText(f"Prato: {self.nome_prato}\nValor total = R${self.valor_total:.2f}")
        self.lineEdit.clear()  # Limpa o QLineEdit após cada adição

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec())
