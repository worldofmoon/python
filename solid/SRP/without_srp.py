def process_file(input_file, output_file):
    # Lê dados do arquivo de entrada
    with open(input_file, "r") as file:
        data = file.read()

    # Processa os dados
    processed_data = data.upper()

    # Grava os dados processados no arquivo de saída
    with open(output_file, "w") as file:
        file.write(processed_data)


################################################################
################################################################


def manage_user(user_data):
    # Valida os dados do usuário
    if not user_data.get("name") or not user_data.get("email"):
        raise ValueError("Nome e email são obrigatórios")

    # Salva o usuário no banco de dados
    with open("users.txt", "a") as file:
        file.write(f"{user_data['name']},{user_data['email']}\n")

    # Envia um email de boas-vindas
    print(f"Enviando email de boas-vindas para {user_data['email']}")


################################################################
################################################################


def process_order(order):
    # Calcula o total do pedido
    total = sum(item["price"] for item in order["items"])

    # Processa o pagamento
    if not process_payment(order["payment_details"], total):
        raise ValueError("Pagamento falhou")

    # Atualiza o estoque
    for item in order["items"]:
        update_stock(item["id"], item["quantity"])

    # Envia confirmação de pedido
    print(f"Pedido {order['id']} processado com sucesso")


################################################################
################################################################


def send_notification(user, message):
    # Envia email
    print(f"Enviando email para {user['email']}: {message}")

    # Envia SMS
    print(f"Enviando SMS para {user['phone']}: {message}")

    # Envia notificação push
    print(f"Enviando notificação push para {user['device_id']}: {message}")


###############################################################################

# Desvantagens:
# - As funções estão muito grandes e fazem mais de uma coisa
# - Difícil de reutilizar o código
# - Difícil de testar as funções isoladamente
# - Difícil de manter e evoluir o código
# - Violação do princípio da responsabilidade única
# - Código menos legível e mais propenso a erros
# - Dificuldade em identificar e corrigir problemas
# - Dificuldade em adicionar novas funcionalidades
# - Dificuldade em remover ou alterar funcionalidades existentes

# Vantagens:
# - Código mais simples e direto
# - Menos abstrações e camadas

# 1. Dificuldade de Manutenção
# Cada função realiza múltiplas tarefas, o que torna o código mais difícil de entender e modificar. 
# Por exemplo, a função process_file lê dados de um arquivo, processa esses dados e grava os resultados em outro arquivo.
# Se houver uma mudança na forma como os dados são processados, você terá que modificar essa função, o que pode introduzir bugs.

# 2. Baixa Reusabilidade
# Funções que fazem muitas coisas são menos reutilizáveis. Por exemplo, se você precisar apenas validar os dados do usuário
# em outro contexto, não poderá reutilizar a função manage_user sem também salvar os dados no banco de dados e enviar um
# email de boas-vindas.

# 3. Testabilidade Comprometida
# Funções que realizam múltiplas tarefas são mais difíceis de testar.
# Testar a função process_order requer a configuração de um ambiente que suporte cálculo de total, processamento de pagamento,
# atualização de estoque e envio de confirmação de pedido. Isso torna os testes mais complexos e propensos a falhas.

# 4. Isolamento de Mudanças
# Quando uma função tem múltiplas responsabilidades, uma mudança em uma parte da função pode afetar outras partes.
# Por exemplo, se você mudar a forma como os dados são lidos em process_file, isso pode afetar a forma como os dados são
# processados e gravados.

# 5. Código Duplicado
# Funções com múltiplas responsabilidades podem levar a duplicação de código. Por exemplo, se você precisar enviar
# notificações em vários lugares do seu código, pode acabar duplicando a lógica de envio de email, SMS e notificação push.
