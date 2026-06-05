from abc import ABC, abstractmethod

class IDocumentReader(ABC):
	"""Contrato base para qualquer leitura de documento no sistema"""

	@abstractmethod
	def read(self, file_path: str) -> str:
		pass