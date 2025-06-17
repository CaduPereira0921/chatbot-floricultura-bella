# 🌸 Chatbot Floricultura FloresBella

Este projeto implementa um chatbot de atendimento ao cliente para a floricultura "FloresBella", utilizando a API da OpenAI (GPT). O chatbot é capaz de responder a perguntas comuns sobre a loja, seus produtos, horários de funcionamento e promoções, com base em um contexto fornecido.

## ✨ Funcionalidades

* Respostas baseadas em contexto da floricultura.
* Integração com a API da OpenAI.
* Fluxo de conversa interativo via terminal.
* Gerenciamento de segredos com variáveis de ambiente.

## 🚀 Como Usar

### Pré-requisitos

* Python 3.8+
* Uma chave de API da OpenAI.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/CaduPereira0921/chatbot-floricultura-bella.git](https://github.com/CaduPereira0921/chatbot-floricultura-bella.git)
    cd chatbot-floricultura-bella
    ```
    *Substitua `CaduPereira0921` pelo seu nome de usuário do GitHub se for diferente.*

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuração da API Key

1.  Crie um arquivo `.env` na raiz do projeto (na mesma pasta onde está o `main.py`).
2.  Adicione sua chave da API OpenAI a este arquivo no formato:
    ```
    OPENAI_API_KEY='sua_chave_da_openai_aqui'
    ```
    *Substitua `sua_chave_da_openai_aqui` pela sua chave real da API OpenAI.*

    **Atenção:** O arquivo `.env` está no `.gitignore` e **NÃO** será enviado para o GitHub, mantendo sua chave segura.

### Executando o Chatbot

1.  Certifique-se de que o ambiente virtual está ativado.
2.  Execute o script principal:
    ```bash
    python src/chatbot_floricultura/main.py
    ```

## 📂 Estrutura do Projeto