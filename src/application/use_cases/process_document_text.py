from typing import List
from src.domain.interfaces.text_sanitizer import ITextSanitizer
from src.domain.interfaces.text_chunker import ITextChunker

class ProcessDocumentTextUseCase:
	"""
	Use Case responsavel por higienizar e fatiar o texto, preparando para vetorização (embeddings)
	"""

	def __init__(self, sanitizer: ITextSanitizer, chunker: ITextChunker):
		self._sanitizer = sanitizer
		self._chunker = chunker

	def execute(self, raw_text: str) -> List[str]:
		if not raw_text:
			return []
		
		sanitized_text = self._sanitizer.sanitize(raw_text)
		text_chunks = self._chunker.chunk(sanitized_text)

		return text_chunks