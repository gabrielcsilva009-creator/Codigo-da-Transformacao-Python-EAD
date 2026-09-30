import os
import shutil


# Pastas de origem e destino
pasta_origem = "arquivos_importantes"
pasta_backup = "backup"


# Cria as pastas caso elas não existam
if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)

if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)


# Percorre os arquivos da pasta de origem
for arquivo in os.listdir(pasta_origem):

    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_destino = os.path.join(pasta_backup, arquivo)

    # Verifica se é um arquivo
    if os.path.isfile(caminho_origem):

        shutil.copy2(caminho_origem, caminho_destino)

        print(f"Backup realizado: {arquivo}")


print("\nBackup concluído com sucesso!")