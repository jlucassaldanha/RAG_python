import os
from src.application.use_cases.extract_text_from_document import ExtractTextFromDocumentUseCase
from src.infrastructure.text_processing.regex_sanitizer import RegexTextSanitizer
from src.application.use_cases.process_document_text import ProcessDocumentTextUseCase
from src.infrastructure.readers.markdown_universal_reader import MarkdownUniversalReader
from src.infrastructure.text_processing.langchain_markdown_chunker import LangchainMarkdownChunker
	
if __name__ == "__main__":
	target_file = "Instruções Conexão Serial - Precision v1_v2.pdf"

	try:
		file_reader = MarkdownUniversalReader()
		text_sanitizer = RegexTextSanitizer()
		text_chunker = LangchainMarkdownChunker(chunk_size=800, chunk_overlap=100)

		extract_use_case = ExtractTextFromDocumentUseCase(file_reader)
		process_use_case = ProcessDocumentTextUseCase(text_sanitizer, text_chunker)

		raw_text = extract_use_case.execute(target_file)
		text_chunks = process_use_case.execute(raw_text)

		print(f"Processamento concluído. O documento gerou {len(text_chunks)} blocos.")

		for index, chunk in enumerate(text_chunks):
			print(f"\n[BLOCO {index + 1}]")
			print(chunk)
			print("-" * 40)

	except Exception as e:
		print("Erro:", e)