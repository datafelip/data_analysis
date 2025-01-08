import os
import validaDados
import validaArquivo
import matplotlib.pyplot as plt
limpadorTela = lambda:os.system("cls")
arquivoVendas = "vendasMes.txt"
def menuPrincipal():
    escolha = validaDados.pegaNumeroPositivo("[1] Adicionar Venda\n[2] Listar Vendas\n[3] Remover Venda\n[4] Alterar Venda\n[5] Buscar Venda \n[6] Plotar Gráfico\n[7] Sair \nDigite aqui -->: ")
    if escolha in range(1, 8):
        return escolha
    else:
        print("Selecione um número de 1 até 7")
def adicionarVenda(mesv, valorv, metav):
    validaArquivo.escrever_arquivo(arquivoVendas, f"{mesv} : {valorv} : {metav}\n", 'a')
    print(f"Venda adicionada: {mesv} - Venda: R$ {valorv}, Meta: R$ {metav} com sucesso")
def listarVendas():
    vendas = validaArquivo.ler_arquivo(arquivoVendas)
    print("========== Vendas Registradas ==========")
    print(f"{'Mês':<10} {'Venda (R$)':<15} {'Meta (R$)':<15}")
    for venda in vendas:
        mes, valor, meta = venda.strip().split(',')
        print(f"{mes:<10} {valor:<15} {meta:<15}")
    print("========================================")
def removerVendas(mesV):
    vendas = validaArquivo.ler_arquivo(arquivoVendas)
    vendas_atualizadas = [venda for venda in vendas if not venda.startswith(mesV)]
    if len(vendas) != len(vendas_atualizadas):
        validaArquivo.escrever_arquivo(arquivoVendas, ''.join(vendas_atualizadas), modo='w')
        print(f"Venda do mês {mesV} removida com sucesso.")
    else:
        print(f"Nenhuma venda encontrada para o mês {mesV}.")
def atualizarVendas(mesV):
    vendas = validaArquivo.ler_arquivo(arquivoVendas)
    vendas_atualizadas = []
    alteracao = False
    for venda in vendas:
        mes, valor, meta = venda.strip().split(',')
        if mes == mesV:
            novo_valor = validaDados.pegaNumeroPositivo(f"Digite o novo valor para o mês {mes}: ")
            nova_meta = validaDados.pegaNumeroPositivo(f"Digite a nova meta para o mês {mes}: ")
            vendas_atualizadas.append(f"{mes},{novo_valor},{nova_meta}\n")
            alteracao = True
        else:
            vendas_atualizadas.append(venda)
    if alteracao:
        validaArquivo.escrever_arquivo(arquivoVendas, ''.join(vendas_atualizadas), modo='w')
        print(f"Venda do mês {mesV} alterada com sucesso.")
    else:
        print(f"Nenhuma venda encontrada para o mês {mesV}.")
def buscarVenda(mesV):
    vendas = validaArquivo.ler_arquivo(arquivoVendas)
    for venda in vendas:
        mes, valor, meta = venda.strip().split(',')
        if mes == mesV:
            print(f"Venda encontrada: Mês: {mes}, Venda: R$ {valor}, Meta: R$ {meta}")
            return
    print(f"Nenhuma venda encontrada para o mês {mesV}.")
    
validaArquivo.garantir_arquivo_existe(vendasMes.txt)

def main():
    while True:
        limpadorTela()
        opcao = menuPrincipal()
        match opcao:
            case 1:
                mesVenda = validaDados.pegaStringVazia("Digite o mês da venda: ")
                valorVenda = validaDados.pegaNumeroPositivo("Digite o valor da venda: ")
                metaVenda = validaDados.pegaNumeroPositivo("Digite a meta da venda: ")
                adicionarVenda(mesVenda, valorVenda, metaVenda)
                input('<enter> para continuar')
            case 2:
                if os.path.getsize(arquivoVendas) > 0:
                    listarVendas()
                else:
                    print(f"O arquivo {arquivoVendas} está vazio.")
                input('<enter> para continuar')
            case 3:
                if os.path.getsize(arquivoVendas) > 0:
                    mesVenda = validaDados.pegaStringVazia("Digite o mês da venda que deseja remover: ")
                    removerVendas(mesVenda)
                else:
                    print(f"O arquivo {arquivoVendas} está vazio.")
                input('<enter> para continuar')
            case 4:
                if os.path.getsize(arquivoVendas) > 0:
                    mes_v = validaDados.pegaStringVazia("Digite o mês da venda: ")
                    atualizarVendas(mes_v)
                else:
                    print(f"Arquivo de vendas {arquivoVendas} vazio")
                input("<enter> para continuar...")
            case 5:
                if os.path.getsize(arquivoVendas) > 0:
                    mesVenda = validaDados.pegaStringVazia("Digite o mês que deseja buscar: ")
                    buscarVenda(mesVenda)
                else:
                     print(f"Arquivo de vendas {arquivoVendas} vazio")
                input("<enter> para continuar...")
            case 6:
                vendas = validaArquivo.ler_arquivo(arquivoVendas)
                meses = []
                valores = []
                metas = []
                for venda in vendas:
                    mes, valor, meta = venda.strip().split(',')
                    meses.append(mes)
                    valores.append(float(valor))
                    metas.append(float(meta))
                plt.figure(figsize=(10, 6))
                plt.plot(meses, valores, marker='o', linestyle='-', color='b', label='Vendas')
                plt.plot(meses, metas, marker='x', linestyle='--',color='r', label='Metas')
                plt.title("Vendas Mensais x Metas", fontsize=14)
                plt.xlabel("Meses", fontsize=10)
                plt.ylabel("Valores (em R$)", fontsize=10)
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.legend()
                plt.tight_layout()
                plt.show()
if __name__ == "__main__":
    main()
                
