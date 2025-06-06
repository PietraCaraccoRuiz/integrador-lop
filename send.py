import pandas as pd
import pywhatkit as py
from datetime import datetime
import time


def get_status_emoji(status):
    """Retorna emoji baseado no status da esteira"""
    if status == 3:
        return "🟢"  # Verde
    elif status == 1:
        return "🔴"  # Vermelho
    elif status == 2:
        return "🟡"  # Amarelo
    else:
        return "⚪"  # Branco (status desconhecido)


def find_today_data(csv_file):
    """Encontra os dados do dia atual no CSV"""
    try:
        # Ler o arquivo CSV
        df = pd.read_csv(csv_file)

        # Obter data atual no formato do CSV
        today = datetime.now().strftime("%Y/%m/%d")

        # Filtrar dados do dia atual
        today_data = df[df['Date'] == today]

        if today_data.empty:
            print(f"Nenhum dado encontrado para {today}")
            return None

        # Pegar o registro mais recente do dia (último registro)
        latest_record = today_data.iloc[-1]

        return {
            'date': latest_record['Date'],
            'time': latest_record['Time'],
            'esteira1': int(latest_record['esteira1']),
            'esteira2': int(latest_record['esteira2']),
            'esteira3': int(latest_record['esteira3'])
        }

    except FileNotFoundError:
        print(f"Arquivo {csv_file} não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None


def send_whatsapp_notification(phone_number, data):
    """Envia notificação via WhatsApp"""
    if not data:
        print("Nenhum dado para enviar")
        return

    # Formatar data para exibição (DD/MM)
    date_obj = datetime.strptime(data['date'], "%Y/%m/%d")
    formatted_date = date_obj.strftime("%d/%m")

    # Criar mensagem
    message = f"""📊 *Relatório de Estoque - {formatted_date}*

🏭 Status das Esteiras:
• Esteira 1: {get_status_emoji(data['esteira1'])}
• Esteira 2: {get_status_emoji(data['esteira2'])}
• Esteira 3: {get_status_emoji(data['esteira3'])}

⏰ Última atualização: {data['time']}

🟢 = OK | 🔴 = Crítico | 🟡 = Planejar |"""

    try:
        # Enviar mensagem instantaneamente
        py.sendwhatmsg_instantly(phone_number, message)
        print(f"Mensagem enviada com sucesso para {phone_number}")

        # Aguardar um pouco para garantir que a mensagem foi enviada
        time.sleep(5)

    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


def main():
    # Configurações
    CSV_FILE = "dados.csv"
    PHONE_NUMBER = "+55 19 99692-0079"  # Número do WhatsApp

    print("🚀 Iniciando verificação de status das esteiras...")

    # Buscar dados do dia atual
    data = find_today_data(CSV_FILE)

    if data:
        print(f"✅ Dados encontrados para {data['date']}:")
        print(f"   Esteira 1: {data['esteira1']} {get_status_emoji(data['esteira1'])}")
        print(f"   Esteira 2: {data['esteira2']} {get_status_emoji(data['esteira2'])}")
        print(f"   Esteira 3: {data['esteira3']} {get_status_emoji(data['esteira3'])}")

        # Enviar notificação
        send_whatsapp_notification(PHONE_NUMBER, data)
    else:
        print("❌ Nenhum dado encontrado para hoje")


if __name__ == "__main__":
    main()
