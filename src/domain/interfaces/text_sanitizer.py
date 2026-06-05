from abc import ABC, abstractmethod

class ITextSanitizer(ABC):
	@abstractmethod
	def sanitize(self, raw_text: str) -> str:
		pass
	