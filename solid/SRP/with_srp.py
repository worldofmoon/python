class FileProcessor:
    """docstring for FileProcessor"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_file(self):
        with open(self.input_file, "r") as file:
            return file.read()

    def process_data(self, data):
        return data.upper()

    def write_file(self, data):
        with open(self.output_file, "w") as file:
            file.write(data)

    def process_file(self):
        data = self.read_file()
        processed_data = self.process_data(data)
        self.write_file(processed_data)


# Instancia a classe FileProcessor
processor = FileProcessor("input.txt", "output.txt")
processor.process_file()

################################################################
################################################################


class UserManager:
    def validate_user_data(self, user_data):
        if not user_data.get("name") or not user_data.get("email"):
            raise ValueError("Nome e email são obrigatórios")

    def save_user(self, user_data):
        with open("users.txt", "a") as file:
            file.write(f"{user_data['name']},{user_data['email']}\n")

    def send_welcome_email(self, user_data):
        print(f"Enviando email de boas-vindas para {user_data['email']}")

    def manage_user(self, user_data):
        self.validate_user_data(user_data)
        self.save_user(user_data)
        self.send_welcome_email(user_data)


# Uso
user_manager = UserManager()
user_data = {"name": "João", "email": "joao@example.com"}
user_manager.manage_user(user_data)

################################################################
################################################################


class OrderProcessor:
    def calculate_total(self, order):
        return sum(item["price"] for item in order["items"])

    def process_payment(self, payment_details, total):
        # Simulação de processamento de pagamento
        return True

    def update_stock(self, item_id, quantity):
        # Simulação de atualização de estoque
        pass

    def send_order_confirmation(self, order):
        print(f"Pedido {order['id']} processado com sucesso")

    def process_order(self, order):
        total = self.calculate_total(order)
        if not self.process_payment(order["payment_details"], total):
            raise ValueError("Pagamento falhou")
        for item in order["items"]:
            self.update_stock(item["id"], item["quantity"])
        self.send_order_confirmation(order)


# Uso
order_processor = OrderProcessor()
order = {
    "id": 1,
    "items": [
        {"id": 101, "price": 50, "quantity": 2},
        {"id": 102, "price": 30, "quantity": 1},
    ],
    "payment_details": {"method": "credit_card", "number": "1234-5678-9876-5432"},
}
order_processor.process_order(order)

################################################################
################################################################


class NotificationSender:
    def send_email(self, email, message):
        print(f"Enviando email para {email}: {message}")

    def send_sms(self, phone, message):
        print(f"Enviando SMS para {phone}: {message}")

    def send_push_notification(self, device_id, message):
        print(f"Enviando notificação push para {device_id}: {message}")

    def send_notification(self, user, message):
        self.send_email(user["email"], message)
        self.send_sms(user["phone"], message)
        self.send_push_notification(user["device_id"], message)


# Uso
notification_sender = NotificationSender()
user = {"email": "user@example.com", "phone": "123456789", "device_id": "device123"}
message = "Você tem uma nova mensagem"
notification_sender.send_notification(user, message)

""" SRP (Single Responsibility Principle) - Princípio da Responsabilidade Única
O Princípio da Responsabilidade Única (SRP) afirma que uma classe deve ter apenas um motivo para mudar,
ou seja, ela deve ter apenas uma responsabilidade.

Quando uma classe tem mais de uma responsabilidade, ela se torna mais difícil de manter e evoluir,
pois mudanças em uma responsabilidade podem afetar as outras.
Para resolver esse problema, podemos dividir a classe em classes menores, cada uma com uma única responsabilidade.

No exemplo acima, temos quatro classes que violam o SRP: FileProcessor, UserManager, OrderProcessor e NotificationSender.
    A classe FileProcessor é responsável por ler um arquivo, processar os dados e escrever o resultado em outro arquivo.
    A classe UserManager é responsável por validar os dados do usuário, salvar o usuário no banco de dados e enviar um email de boas-vindas.
    A classe OrderProcessor é responsável por calcular o total de um pedido, processar o pagamento, atualizar o estoque e
    enviar uma confirmação de pedido.
    A classe NotificationSender é responsável por enviar notificações por email, SMS e push.

Para aplicar o SRP, podemos dividir essas classes em classes menores, cada uma com uma única responsabilidade.

O SRP é um princípio fundamental para escrever código limpo e modular.
Ao garantir que cada classe ou módulo tenha uma única responsabilidade, você cria um sistema mais fácil de entender,
manter e expandir. A aplicação do SRP pode inicialmente parecer que aumenta a quantidade de código,
mas os benefícios em termos de clareza, manutenção e testabilidade superam em muito esse custo inicial.
"""
