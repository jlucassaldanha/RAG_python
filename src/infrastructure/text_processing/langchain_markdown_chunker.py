from typing import List
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from src.domain.interfaces.text_chunker import ITextChunker

class LangchainMarkdownChunker(ITextChunker):
    """
    Divisor de texto robusto. Primeiramente, tenta dividir pelo formato Markdown.
    Caso uma seção sob um cabeçalho seja maior que o limite de caracteres, 
    ele subdivide recursivamente o texto preservando o contexto do cabeçalho.
    """
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        # 1. Regra de divisão por cabeçalhos lógicos
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=False
        )
        
        # 2. Regra de segurança de tamanho
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def chunk(self, text: str) -> List[str]:
        if not text:
            return []

        # Etapa A: Divide o texto utilizando os cabeçalhos (##)
        md_splits = self.markdown_splitter.split_text(text)
        
        # Etapa B: Aplica o limite de tamanho (garante que nenhuma seção fique gigante)
        final_documents = self.recursive_splitter.split_documents(md_splits)
        
        formatted_chunks = []
        for doc in final_documents:
            # O LangChain salva a qual título o texto pertence no metadado.
            # Injetamos essa informação de volta no bloco para o LLM saber o contexto.
            context_header = " > ".join(doc.metadata.values()) if doc.metadata else "Geral"
            formatted_block = f"[Contexto da Seção: {context_header}]\n{doc.page_content}"
            formatted_chunks.append(formatted_block)
            
        return formatted_chunks