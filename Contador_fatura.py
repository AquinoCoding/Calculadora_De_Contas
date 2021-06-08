print('Contador de Fatura App')
print('Informe: \n[1]Devedor total\n[2]Somente Ubers\n[3]Pesquisar')

def contador():
        
        gravadorLine = []
        ListUserLucas = []
        ListUserLaryssa = []
        ListUserIrene = []
        ListUserAline = []
        ListUserOutros = []
        ListUserLucasLaryssa = []
        
        while True:
            with open('dados.txt','r',encoding='utf-8') as arquivo:
                palavra = input('Comando: ')
                
                if palavra == '1':
                    palavra = ''
                    gravador = open("contas.txt", "a")
                    
                elif palavra == '2':
                    palavra = 'Uber'
                    gravador = open("SomenteUber.txt", "a")
                    
                elif palavra == '3':
                    palavra = input('Digite a palavra para busca: ')
                    gravador = open("contas.txt", "a")
                    
                data_rep = ''
                cont = 0
                valores = []
                
                for linha in arquivo:
                    # Aqui definimos a data das compras
                    if 7 == len(linha) and data_rep != linha:
                        data_rep = linha
                        linha = linha.rstrip()
                        print(f'\n----------------------\n{linha}')
                        gravadorLine.append(f'\n----------------------\n{linha}\n')
                        
                        
                    # Aqui definimos as comprar de acordo com o nome
                    
                    elif palavra in linha:
                        linha = linha.rstrip()
                        print(linha)
                        print('\nInforme o usuario: \n[1]Lucas\n[2]Laryssa\n[3]Irene\n[4]Aline\n[5]Lucas & Laryssa\n[6]Outros')
                        user = int(input('Escolha: '))
                        if user == 1:
                            gravadorLine.append(f'{linha} - Lucas\n')
                            linha = linha + ' - Lucas'
                            
                        elif user == 2:
                            gravadorLine.append(f'{linha} - Laryssa\n')
                            linha = linha + ' - Laryssa\n'
                            
                        elif user == 3:
                            gravadorLine.append(f'{linha} - Irene\n')
                            linha = linha + ' - Irene\n'
                            
                        elif user == 4:
                            gravadorLine.append(f'{linha} - Aline\n')
                            linha = linha + ' - Aline\n'
                            
                        elif user == 5:
                            gravadorLine.append(f'{linha} - Lucas & Laryssa\n')
                            linha = linha + ' - Lucas&Laryssa\n'
                            
                        elif user == 6:
                            gravadorLine.append(f'{linha} - Outros\n')
                            linha = linha + ' - Outros\n'
                        
                        cont += 1
                        
                        for i in range(1):
                            linha = linha.split()
                            print(linha)
                            print(len(linha))
                            
                            if len(linha) == 4:
                                ValorCompra = linha[1]
                                ValorCompra = ValorCompra.replace(',','.')
                                ValorCompra = float(ValorCompra)
                                valores.append(ValorCompra)
                                
                            if len(linha) == 5:
                                ValorCompra = linha[2]
                                ValorCompra = ValorCompra.replace(',','.')
                                ValorCompra = float(ValorCompra)
                                valores.append(ValorCompra)
                                
                            if len(linha) == 6:
                                ValorCompra = linha[3]
                                ValorCompra = ValorCompra.replace(',','.')
                                ValorCompra = float(ValorCompra)
                                valores.append(ValorCompra)
                                
                                
                                
                            ValorUser = linha[-1:]
                            ValorUser = ValorUser[0]
                            
                            if ValorUser == 'Lucas':
                                ListUserLucas.append(ValorCompra)
                                print(ListUserLucas)
                                
                            elif ValorUser == 'Laryssa':
                                ListUserLaryssa.append(ValorCompra)
                            
                            elif ValorUser == 'Irene':
                                ListUserIrene.append(ValorCompra)
                            
                            elif ValorUser == 'Outros':
                                ListUserOutros.append(ValorCompra)
                                
                            elif ValorUser == 'Aline':
                                ListUserAline.append(ValorCompra)
                            
                            elif ValorUser == 'Lucas&Laryssa':
                                ListUserLucasLaryssa.append(ValorCompra)
                        
                ValLucas = sum(ListUserLucas)
                print(ValLucas)
                ValLucas = str(ValLucas)
                
                ValLaryssa = sum(ListUserLaryssa)
                print(ValLaryssa)
                ValLaryssa = str(ValLaryssa)
                
                ValIrene = sum(ListUserIrene)
                print(ValIrene)
                ValIrene = str(ValIrene)
                
                ValAline = sum(ListUserAline)
                print(ValAline)
                ValAline = str(ValAline)
                
                ValOutros = sum(ListUserOutros)
                print(ValOutros)
                ValOutros = str(ValOutros)
                
                ValLucasLaryssa = sum(ListUserLucasLaryssa)
                ValLucasLaryssa = str(ValLucasLaryssa)
                
                valores = sum(valores)
                valores = round(valores)
                valores = str(valores)
                cont = str(cont)
                
                print('\n----------------------')
                gravadorLine.append(f'\n----------------------\n')
                
                lista_final = []
                frase = palavra + ': R$ ' + valores
                lista_final.append(frase)
                
                user_totalLL = []
                frase1 =  'Lucas&Laryssa: R$ ' + ValLucasLaryssa
                user_totalLL.append(frase1)
                
                user_totalLu = []
                frase2 = 'Lucas: R$ ' + ValLucas
                user_totalLu.append(frase2)
                
                user_totalLa = []
                frase3 = 'Laryssa: R$ ' + ValLaryssa
                user_totalLa.append(frase3)
                
                user_totalOu = []
                frase4 = 'Outros: R$ ' + ValOutros
                user_totalOu.append(frase4)
                
                user_totalAl = []
                frase5 = 'Aline: R$ ' + ValAline
                user_totalAl.append(frase5)
                
                user_totalIr = []
                frase6 = 'Irene: R$ ' + ValIrene
                user_totalIr.append(frase6)
                
                lista_compras = []
                totalCompr = palavra +' ' + cont + ' compras.'
                lista_compras.append(totalCompr)
                
                print('[1]Sim\n[2]Não')
                select = int(input('Deseja Sair? '))
                if select == 1:
                    print(f'{lista_final}\n{user_totalLu}\n{user_totalLa}\n{user_totalLL}\n{user_totalIr}\n{user_totalAl}\n{user_totalOu}\n{lista_compras}')
                    
                    #gravadorLine.append(f'{lista_final:.2f}\n{user_totalLu:.2f}\n{user_totalLa:.2f}\n{user_totalLL:.2f}\n{user_totalIr:.2f}\n{user_totalAl:.2f}\n{user_totalOu:.2f}\n{lista_compras}')
                    gravadorLine.append(f'{lista_final}\n{user_totalLu}\n{user_totalLa}\n{user_totalLL}\n{user_totalIr}\n{user_totalAl}\n{user_totalOu}\n{lista_compras}')
                  
                    

                    gravador.writelines(gravadorLine)
                    break
contador()
    
        
