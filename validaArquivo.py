import os
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print("Erro : permissão de acesso ao arquivo")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    return []
def escrever_arquivo(nome_arquivo, conteudo, modo='w'):
    try:
        with open(nome_arquivo, modo,  encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print(f"Erro : permissão de acesso ao arquivo {nome_arquivo}")
    except Exception as e:
        print(f"Erro inesperado no arquivo '{nome_arquivo}': {e}")

def garantir_arquivo_existe(arquivo):
    if not os.path.exists(arquivo):
        open(arquivo, 'a').close()