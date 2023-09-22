''' Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.'''

email = "infinity.school@dev.br"
senha = "infinityschool123"

while True:
    email_Digitado = input("informe o email de cadastrado: ")
    senha_Digitada = input("informe a senha cadastrada: ")
    if email_Digitado != email and senha_Digitada != senha:
        print("Acesso recusado")
        continue
    else:
        print("Acesso Permitido")
        break