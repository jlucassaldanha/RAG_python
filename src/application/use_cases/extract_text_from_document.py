from src.domain.interfaces.document_reader import IDocumentReader

class ExtractTextFromDocumentUseCase:
	"""Use Case responsavel por orquestrar a extração de texto bruto"""

	def __init__(self, document_reader: IDocumentReader):
		self._document_reader = document_reader

	def execute(self, file_path: str) -> str:
		raw_text = self._document_reader.read(file_path)

		if not raw_text:
			raise ValueError(f"Nenhum texto pode ser extraido de: {file_path}")
		
		return raw_text.strip()