import os

def listar_arquivos_html(pasta):
    try:
        arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith(".html")]
        if arquivos:
            print("<ul>")
            for arquivo in arquivos:
                print(f"    <li><a href='{arquivo}'>{arquivo}</a></li>")
            print("</ul>")
        else:
            print("Nenhum arquivo HTML encontrado.")
    except FileNotFoundError:
        print("Pasta não encontrada.")

# Exemplo de uso
pasta_alvo = "c:/Users/Bruno Lindão/Desktop/teste/Caderno/Js"
listar_arquivos_html(pasta_alvo)
