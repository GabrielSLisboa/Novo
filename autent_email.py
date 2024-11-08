import pyrebase
import json

def autenticacao():
    with open('firebase_config.json', 'r') as arquivo:
        config = json.load(arquivo)
    return config

if __name__ == '__main__':
    firebase =pyrebase.initialize_app(autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    email = input('Entre com o e-mail: ')
    senha = input('Entre com a senha: ')
    try:
        print(auth.sign_in_with_email_and_password(email,senha))
        #auth.sign_in_with_email_and_password(email,senha)
        print('Login realizado com sucesso')
    except:
        print('Senha invalida')

## para adicionar e-mail 
#auth.create_user_with_email_and_password(email,senha)