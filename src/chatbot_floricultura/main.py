import openai
import json
import os
from dotenv import load_dotenv

# Importa as funções do módulo utils
from .utils import carregar_configuracao, formatar_contexto_inicial, obter_resposta_chatgpt

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        print("Erro: A chave da API OpenAI não está configurada. Por favor, verifique seu arquivo .env.")
        return

    print("Seja bem-vindo à Floricultura FloresBella. Como posso te ajudar?")

    # Carrega a configuração da loja
    configuracao_loja = carregar_configuracao("config/config_lojaflores.json")
    if not configuracao_loja:
        print("Erro: Não foi possível carregar a configuração da loja.")
        return

    # Carrega e formata o contexto inicial
    contexto = formatar_contexto_inicial("config/context_template.txt", configuracao_loja)

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ['sair', 'exit', 'quit', 'tchau', 'até mais']:
            print("Obrigado, volte sempre!!")
            break
        
        # Obtém e imprime a resposta do ChatGPT
        resposta = obter_resposta_chatgpt(pergunta, contexto)
        print(f"Floricultura: {resposta}")

if __name__ == "__main__":
    main()