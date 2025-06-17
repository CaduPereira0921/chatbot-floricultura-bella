import json
import openai
import os

def carregar_configuracao(caminho_arquivo):
    """Carrega as configurações da floricultura a partir de um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo de configuração '{caminho_arquivo}' não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: Erro ao decodificar JSON em '{caminho_arquivo}'. Verifique a sintaxe.")
        return None

def formatar_contexto_inicial(caminho_template, configuracao):
    """
    Carrega o template de contexto e o preenche com as informações da configuração.
    Retorna o contexto inicial como uma lista de mensagens.
    """
    try:
        with open(caminho_template, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de template de contexto '{caminho_template}' não encontrado.")
        return [{"role": "system", "content": "Você é um assistente prestativo."}]

    # Formatando o template com os dados da configuração
    # Garantir que listas sejam formatadas como strings legíveis (ex: unindo com ', ')
    for key, value in configuracao.items():
        if isinstance(value, list):
            configuracao[key] = ", ".join(value)

    contexto_formatado = template.format(**configuracao)
    
    return [{"role": "system", "content": contexto_formatado}]

def obter_resposta_chatgpt(pergunta, contexto_mensagens):
    """
    Envia a pergunta do usuário para a API do OpenAI e retorna a resposta.
    Mantém o histórico da conversa no contexto.
    """
    # Adiciona a pergunta do usuário ao contexto da conversa
    contexto_mensagens.append({"role": "user", "content": pergunta})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=contexto_mensagens,
            temperature=0.7,
            max_tokens=200
        )
        resposta_assistente = response.choices[0].message.content
        
        # Adiciona a resposta do assistente ao contexto para manter o histórico
        contexto_mensagens.append({"role": "assistant", "content": resposta_assistente})
        
        return resposta_assistente
    except openai.APIError as e:
        print(f"Erro na API OpenAI: {e}")
        return "Desculpe, ocorreu um erro ao processar sua solicitação com a OpenAI."
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return "Desculpe, não consigo responder no momento."