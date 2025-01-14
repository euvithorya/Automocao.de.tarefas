from pathlib import Path

# Caminho da pasta para serem renomeados
caminho_pasta = Path('caminho/da/sua/pasta')

# Prefixo ou sufixo que você quer adicionar aos arquivos
prefixo = 'novo_'


for arquivo in caminho_pasta.iterdir():
    if arquivo.is_file():
        novo_nome = arquivo.name
        novo_nome = prefixo + novo_nome
        
        novo_arquivo = caminho_pasta / novo_nome
        
        arquivo.rename(novo_arquivo)
        print(f'Renomeado: {arquivo.name} -> {novo_nome}')

#:V