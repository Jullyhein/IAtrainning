from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from loguru import logger
import os

load_dotenv()

class QASystem:
    def __init__(self, vectorstore, metadata: dict):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        self.verifier_llm = ChatOpenAI(model="gpt-4", temperature=0.0)

        self.qa_chain = self._setup_qa_chain(vectorstore, metadata)
        self.verifier_prompt = self._build_verifier_prompt()

    def _setup_qa_chain(self, vectorstore, metadata):
        prompt = PromptTemplate(
            input_variables=["question", "context"],
            partial_variables={
                "document_title": metadata.get("title", "Desconhecido"),
                "author": metadata.get("author", "Desconhecido"),
            },
            template="""
Você é um assistente inteligente que leu um documento técnico.

Baseando-se no seguinte conteúdo extraído do documento:

{context}

Forneça uma resposta bem estruturada para a pergunta:

{question}

Informações adicionais:
- Título: {document_title}
- Autor: {author}
"""
        )

        return RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=vectorstore.as_retriever(search_type="mmr"),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )

    def _build_verifier_prompt(self):
        return PromptTemplate(
            input_variables=["question", "context", "answer"],
            template="""
Você é um verificador de qualidade de respostas geradas por IA.

Analise a resposta abaixo à luz do contexto e da pergunta original.

Pergunta:
{question}

Contexto:
{context}

Resposta gerada:
{answer}

Avalie se a resposta está correta, completa e alinhada com o contexto.
Diga claramente se:
- A resposta está correta
- Há omissões importantes
- Há sinais de alucinação
- A resposta pode ou não ser confiável

Forneça um parecer objetivo e técnico.
"""
        )

    def ask(self, question: str) -> dict:
        logger.info(f"Pergunta recebida: {question}")
        result = self.qa_chain.invoke({"query": question})

        answer = result["result"]
        context = "\n\n".join([doc.page_content for doc in result["source_documents"]])

        # Verificação da resposta
        verifier_input = self.verifier_prompt.format(
            question=question,
            context=context,
            answer=answer
        )
        validation = self.verifier_llm.invoke(verifier_input)

        return {
            "resposta": answer,
            "validacao": validation.content
        }
