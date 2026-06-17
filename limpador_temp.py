import os

temp_path = os.environ['TEMP']

while True:

    arquivos = os.listdir(temp_path)

    print("\n=== LIMPEZA TEMP ===")
    print("1 - Quantidade de arquivos")
    print("2 - Espaço ocupado")
    print("3 - Listar arquivos")
    print("4 - Limpar arquivos temporários")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        print(f"\nForam encontrados {len(arquivos)} itens.")

    elif opcao == "2":

        tamanho_total = 0

        for item in arquivos:

            caminho = os.path.join(temp_path, item)

            if os.path.isfile(caminho):

                tamanho_total += os.path.getsize(caminho)

        print(f"Espaço ocupado: {tamanho_total / 1024 / 1024:.2f} MB")

    elif opcao == "3":

        for arquivo in arquivos[:20]:
            print(arquivo)
            
    elif opcao == "4":
        
        confirmar = input(
            "Tem certeza que deseja apagar os arquivos temporários? (s/n): "
        )       
        
        if confirmar.lower() == "s":    
            
            apagados = 0 
            
            for item in arquivos:
                caminho = os.path.join(temp_path, item)
                
                if os.path.isfile(caminho):
                    
                    try:
                        
                        os.remove(caminho)
                        apagados += 1
                        
                    except:
                        
                        pass
                    
            print(f"{apagados} arquivos apagados com sucesso!")
            
    elif opcao == "5":

        print("Encerrando...")
        break

    else:

        print("Opção inválida!")
    
    
    