# IAtrainning --- Oráculo Energia Solar ☀️

Assistente de inteligência artificial desenvolvido para responder
perguntas com base em documentos de conhecimento da SolarGroup. O
projeto reúne uma interface conversacional, recuperação de trechos
relevantes de PDFs e uma API para consulta.

> **Status:** projeto em desenvolvimento. Confira as dependências e os
> comandos de execução abaixo, pois os módulos de interface e API
> utilizam conjuntos de bibliotecas diferentes.

## ✨ Funcionalidades

-   Consulta a uma base de conhecimento em PDF.
-   Extração e divisão do conteúdo do documento em trechos (*chunks*).
-   Busca semântica de trechos relevantes usando embeddings e FAISS.
-   Geração de respostas com um modelo de linguagem.
-   Interface de chat com Streamlit e opção de modelo local via Ollama.
-   API com FastAPI para enviar perguntas e receber respostas.
-   Registro de perguntas e respostas em banco de dados pela camada
    SQLAlchemy.

## 🧰 Tecnologias

-   **Python**
-   **Streamlit** --- interface conversacional.
-   **FastAPI / Uvicorn** --- API HTTP.
-   **LangChain** --- integração entre prompt, recuperação de contexto e
    modelo.
-   **Ollama** --- execução local de modelos de linguagem e embeddings.
-   **Sentence Transformers** --- geração de embeddings.
-   **FAISS** --- busca vetorial.
-   **Transformers / PyTorch** --- suporte ao modelo utilizado pela API.
-   **SQLAlchemy** --- persistência de perguntas e respostas.
-   **PDF** --- fonte da base de conhecimento.

## 📁 Estrutura do repositório

``` text
IAtrainning/
├── Documento_Mestre_MKT_SolarGroup_FINAL_ORGANIZADO.pdf
├── main.py          # API FastAPI
├── oraculo.py       # Interface de chat Streamlit
├── retriever.py     # Leitura do PDF, embeddings e busca vetorial
├── llm.py           # Geração de respostas para a API
├── database.py      # Configuração e inicialização do banco de dados
├── models.py        # Modelo de dados das perguntas e respostas
├── requirements.txt
├── requirements.lock.txt
└── README.md
```

## ⚙️ Pré-requisitos

-   Python instalado.
-   Git.
-   Para a interface local: [Ollama](https://ollama.com/) instalado e em
    execução.
-   Espaço em disco e memória suficientes para carregar os modelos de
    IA.

## 🚀 Instalação

Clone o repositório e entre na pasta:

``` bash
git clone https://github.com/Jullyhein/IAtrainning.git
cd IAtrainning
```

Crie e ative um ambiente virtual.

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências listadas:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Dependências da interface Streamlit

O arquivo `requirements.txt` atual pode não incluir todas as bibliotecas
importadas por `oraculo.py`. Se necessário, instale também as
dependências da interface:

``` bash
pip install streamlit langchain-core langchain-community langchain-ollama langchain-groq
```

Instale e inicie o Ollama e baixe os modelos utilizados pela interface:

``` bash
ollama pull llama3.1:8b-instruct-q4_K_S
ollama pull nomic-embed-text
```

Os nomes dos modelos precisam corresponder aos configurados no código.
Se usar um servidor Ollama remoto, ajuste o endereço configurado em
`oraculo.py`.

## ▶️ Como executar

### Interface de chat

Com o ambiente virtual ativado, as dependências da interface instaladas
e o Ollama em execução:

``` bash
streamlit run oraculo.py
```

O Streamlit exibirá no terminal o endereço local para abrir a interface
no navegador.

### API FastAPI

Para iniciar a API:

``` bash
uvicorn main:app --reload
```

A API define o endpoint `POST /responder`. Com o servidor em execução, a
documentação interativa do FastAPI normalmente fica disponível em:

``` text
http://127.0.0.1:8000/docs
```

Exemplo de requisição:

``` bash
curl -X POST "http://127.0.0.1:8000/responder" \
  -H "Content-Type: application/json" \
  -d "{\"pergunta\":\"Quais informações estão disponíveis na base?\"}"
```

Exemplo de corpo JSON:

``` json
{
  "pergunta": "Quais informações estão disponíveis na base?"
}
```

A resposta contém os campos `pergunta` e `resposta`.

## 🧠 Como funciona

1.  **Leitura:** o sistema extrai o texto do PDF configurado.
2.  **Fragmentação:** o conteúdo é dividido em trechos menores para
    facilitar a recuperação.
3.  **Vetorização:** os trechos são convertidos em embeddings.
4.  **Recuperação:** a pergunta é vetorizada e o sistema busca os
    trechos mais próximos no índice FAISS.
5.  **Geração:** os trechos recuperados são usados como contexto para o
    modelo de linguagem.
6.  **Retorno:** a resposta é exibida na interface ou devolvida pela
    API. A camada da API também registra pergunta e resposta no banco de
    dados.

## 📄 Base de conhecimento

Por padrão, o código referencia o arquivo:

``` text
Documento_Mestre_MKT_SolarGroup_FINAL_ORGANIZADO.pdf
```

Para utilizar outro documento, atualize o caminho no código
correspondente e garanta que o arquivo esteja acessível ao processo. Use
apenas documentos que você tenha autorização para processar.

## 🔐 Segurança e configuração

-   Não versione chaves de API, tokens ou senhas.
-   Armazene segredos em variáveis de ambiente e mantenha arquivos
    `.env` fora do Git.
-   Antes de publicar a API, restrinja o CORS: a configuração permissiva
    (`*`) não é recomendada para produção.
-   Revise o uso de modelos e os requisitos de memória antes de executar
    em servidores limitados.
-   As respostas geradas por IA podem conter erros; valide informações
    importantes na fonte original.

## ⚠️ Observações

-   A interface Streamlit e a API FastAPI são caminhos de execução
    distintos.
-   As dependências presentes em `requirements.txt` podem precisar ser
    complementadas para executar a interface Streamlit.
-   O caminho do PDF e os nomes dos modelos devem corresponder aos
    arquivos e modelos disponíveis no ambiente.
-   Este README documenta a estrutura e o comportamento observáveis no
    repositório; valide a instalação no ambiente em que o projeto será
    executado.

## 👩‍💻 Autoria

Desenvolvido por [Jullyhein](https://github.com/Jullyhein).

## 📌 Repositório

[github.com/Jullyhein/IAtrainning](https://github.com/Jullyhein/IAtrainning)
