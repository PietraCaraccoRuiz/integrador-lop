import pandas as pd
import pyautogui
import webbrowser
import urllib.parse
import time
from datetime import datetime


def determinar_status_esteira(valor_csv):
    """
    Converte valores do CSV em símbolos para WhatsApp
    1 = [!] - Estoque baixo, nível crítico
    2 = [~] - Estoque médio, planejar
    3 = [OK] - Estoque cheio, sem necessidade
    """
    if valor_csv == 1:
        return "[!]"
    elif valor_csv == 2:
        return "[~]"
    elif valor_csv == 3:
        return "[OK]"
    else:
        return "[?]"


# Configurações do pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Lê o CSV e pega os dados da última linha
df = pd.read_csv("dados.csv")
ultima_linha = df.iloc[-1]

# Pega os valores das esteiras
e1 = ultima_linha['esteira1']
e2 = ultima_linha['esteira2']
e3 = ultima_linha['esteira3']

print(f"Dados do CSV - E1: {e1}, E2: {e2}, E3: {e3}")

# Verifica se há dados válidos
if e1 is not None and e2 is not None and e3 is not None:
    # Formatar data e status
    data_formatada = datetime.now().strftime("%d/%m")
    status_e1 = determinar_status_esteira(e1)
    status_e2 = determinar_status_esteira(e2)
    status_e3 = determinar_status_esteira(e3)

    # Criar mensagem
    mensagem = f"Estoque em {data_formatada}: Esteira 1: {status_e1} | Esteira 2: {status_e2} | Esteira 3: {status_e3}"
    numero = "5519989849917"

    # Codifica apenas caracteres especiais, preserva emojis
    mensagem_codificada = urllib.parse.quote(mensagem, safe='🔴🟡🟢[]')
    link_whatsapp = f"https://wa.me/{numero}?text={mensagem_codificada}"

    print(f"Enviando: {mensagem}")

    # Abrir WhatsApp
    webbrowser.open(link_whatsapp)

    print("Aguardando carregamento da página de conversa...")
    time.sleep(7)

    # Clica no botão 'Continuar para o WhatsApp Web'
    pyautogui.click(x=921, y=325)
    print("Clicou no botão 'Continuar para o WhatsApp Web'.")

    time.sleep(7)

    # Clica no campo de mensagem
    pyautogui.click(x=957, y=389)

    time.sleep(8)

    # Envia a mensagem
    pyautogui.press("enter")
    print("Mensagem enviada automaticamente.")

else:
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Nenhum dado encontrado para a data de hoje ({today}).")