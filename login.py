import mysql.connector
from mysql.connector import Error
from getpass import getpass

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="199.204.160.93",
            port="3306",
            user="u38_O5V1Ib5Hjg",
            password="mIf+HW6.NsA5nl3XrRzdt^c@",
            database="s38_Sky"
        )
        return connection
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def authenticate_user(username, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT username FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                return True
            else:
                return False
        except Error as e:
            print("Erro durante a autenticação:", e)
            return False

def change_password(username, new_password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE users SET password = %s WHERE username = %s"
            cursor.execute(query, (new_password, username))
            connection.commit()
            cursor.close()
            connection.close()
            print("Senha alterada com sucesso!")
        except Error as e:
            print("Erro ao alterar a senha:", e)

def change_username(old_username, new_username):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE users SET username = %s WHERE username = %s"
            cursor.execute(query, (new_username, old_username))
            connection.commit()
            cursor.close()
            connection.close()
            print("Nome de usuário alterado com sucesso!")
        except Error as e:
            print("Erro ao alterar o nome de usuário:", e)

def main():
    print("Bem-vindo ao sistema de login!")

    while True:
        username = input("Digite seu nome de usuário: ")
        password = getpass("Digite sua senha: ")

        if authenticate_user(username, password):
            print("Autenticação bem-sucedida! Acesso concedido.")
            break
        else:
            print("Credenciais inválidas. Tente novamente.")

    while True:
        print("\nMenu de Usuário:")
        print("1. Mudar senha")
        print("2. Mudar nome de usuário")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            new_password = getpass("Digite a nova senha: ")
            change_password(username, new_password)
        elif choice == "2":
            new_username = input("Digite o novo nome de usuário: ")
            change_username(username, new_username)
            username = new_username  # Atualiza o nome de usuário para o novo valor
        elif choice == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()