import re
from src.domain.interfaces.text_sanitizer import ITextSanitizer

class RegexTextSanitizer(ITextSanitizer):
	"""Limpa quebra de linhas e espaços"""

	def sanitize(self, raw_text: str) -> str:
		text = re.sub(r'\n+','\n', raw_text)
		text = re.sub(r'\s+', ' ', text)
		return text.strip()
	