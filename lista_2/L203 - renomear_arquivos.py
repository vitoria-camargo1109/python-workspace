"""
Com os.listdir() e os.rename(), renomeie 20 arquivos de uma pasta 
seguindo um padrão (ex.: relatorio_01.pdf). Não precisa de PyAutoGUI.
"""

import os

# Cria a pasta com os 20 arquivos.
base = os.path.dirname(os.path.abspath(__file__))
pasta = os.path.join(base, "arquivos_renomeados")

os.makedirs(pasta, exist_ok=True)

arquivos = sorted(os.listdir(pasta))

for arquivo in range(20):
    caminho = os.path.join(pasta, f"arquivo_{arquivo}.txt")
    open(caminho, "w").close()
    print("Criado: ", caminho)

print("Total na pasta: ", len(os.listdir(pasta)))


# Renomeia os arquivos da pasta 
# .listdir() e os.rename()
for numero, nome in enumerate(arquivos, start = 1):
    extensao = os.path.splitext(nome)[1]
    novo_nome = f"relatorio_{numero:02d}{extensao}" # Mude o nome para as pastas nessa linha.

    antigo = os.path.join(pasta, nome)
    novo = os.path.join(pasta, novo_nome)

    os.rename(antigo, novo)
    print(nome, "-->", novo_nome)