import os
from unstructured.partition.auto import partition
from src.domain.interfaces.document_reader import IDocumentReader

class MarkdownUniversalReader(IDocumentReader):
	"""
    Leitor universal (PDF, DOCX, PPTX, HTML) que preserva o layout original.
    Transforma tabelas estruturadas e textos colunados em formato Markdown.
    """
	def read(self, file_path: str) -> str:
		if not os.path.exists(file_path):
			raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
		
		elements = partition(filename=file_path)

		markdown_content = []

		for element in elements:
			if element.category == "Table":
				markdown_content.append(element.metadata.text_as_html or str(element))
			elif element.category == "Title":
				markdown_content.append(f"## {str(element)}")
			else:
				markdown_content.append(str(element))

		return "\n\n".join(markdown_content)