import pandas as pd

# Mapeia os valores para os textos descritivos
status_map = {
    1: "Estoque baixo, nível crítico",
    2: "Estoque médio, planejar",
    3: "Estoque cheio, sem necessidade de planejamento"
}

# Define a cor com base no número original (antes da substituição)
def colorir_status(val):
    if val == "Estoque baixo, nível crítico":
        return 'background-color: lightcoral'
    elif val == "Estoque médio, planejar":
        return 'background-color: yellow'
    elif val == "Estoque cheio, sem necessidade de planejamento":
        return 'background-color: lightgreen'
    return ''

# Lê os dados
df = pd.read_csv("dados.csv")

# Colunas das esteiras
colunas_esteiras = ['esteira1', 'esteira2', 'esteira3']

# Substitui os números pelos textos do status
df[colunas_esteiras] = df[colunas_esteiras].replace(status_map)

# Aplica as cores com base nos textos
styled_df = df.style.map(colorir_status, subset=colunas_esteiras)

# Gera HTML da tabela
html_tabela = styled_df.to_html()

# HTML final com CSS
html_completo = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Status das Esteiras</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
            color: #333;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .tabela-wrapper {{
            overflow-x: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
        }}
        th, td {{
            padding: 12px;
            text-align: center;
            border: 1px solid #ccc;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
    </style>
</head>
<body>
    <h1>Status das Esteiras</h1>

    <div class="tabela-wrapper">
        {html_tabela}
    </div>
</body>
</html>
"""

# Salva o HTML no arquivo
with open("dados.html", "w", encoding="utf-8") as f:
    f.write(html_completo)

print("Página HTML com status e cores gerada com sucesso!")
