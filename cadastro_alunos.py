alunos = []

while True:
    print ("===SISTEMA DE CADASTRO DE ALUNOS===")
    print ("1 - Cadastrar Aluno")
    print ("2 - Listar Alunos")
    print ("3 - Ver Média De Um Aluno")
    print ("4 - Sair")  

    opcao = input("Escolha uma opção ").strip()
    
    
    if opcao == "1":
        nome = input ("Digite o nome do aluno: ")

        while True:
            try:
                nota1 = float (input("Digite a primeira nota: "))
                if 0 <= nota1 <= 10:
                    break
                else:
                    print ("Nota Inválida. Digite um valor entre 0 e 10.") 
            except:
                    print ("Entrada Inválida. Digite apenas numeros!")        

        while True:
            try:
                nota2 = float (input("Digite a segunda nota: "))
                if 0 <= nota2 <= 10:
                    break
                else:
                    print ("Nota Inválida. Digite um valor entre 0 e 10.")
            except:
                    print ("Nota Inválida. Digite apenas numeros!")        

        aluno = { 
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2, 
    }

        alunos.append(aluno)
        print ("Aluno Cadastrado com Sucesso!")     


    elif opcao == "2":
        if len(alunos) == 0:
            print ("Nenhum aluno cadastrado.") 
        else:
            print ("===LISTA DE ALUNOS===") 
            for aluno in alunos: 
                print(f"Nome: {aluno['nome']} | Nota 1: {aluno['nota1']} | Nota 2: {aluno['nota2']}")  

    elif opcao == "3":
        nome_busca = input("Digite o nome do aluno: ")
        encontrado = False
        for aluno in alunos: 
            if aluno ["nome"].lower() == nome_busca.lower():         
                media = (aluno["nota1"] + aluno ["nota2"]) / 2
                print (f"Aluno: {aluno['nome']}")
                print (f"Média: {media:.2f}")
                if media >=6:
                    print ("Situação Aprovado!")
                else:
                    print ("Situação Reprovado!")
                encontrado = True
                break
        if not encontrado:
            print ("Aluno Não encontrado!")
   
    elif opcao == "4":
        print ("Encerrando o programa...")
        break

    else:
        print ("Opção ainda não implementada ou inválida") 
