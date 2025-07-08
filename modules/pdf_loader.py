from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    """
    Load a PDF file and return its content as a list of documents.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        list: A list of documents extracted from the PDF.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    return documents