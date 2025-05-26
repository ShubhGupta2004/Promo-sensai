from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import scraper
from dotenv import load_dotenv

load_dotenv()

def create_document(deal):
    content = f"""
    Product: {deal['title']}
    Details: {deal['description']}
    Discount: {deal['discount']}
    Price: Rs.{deal['price']}
    Store: {deal['brand_merchant']}
    Link: {deal['deal_url']}
    """

    metadata = {
        "store": deal['brand_merchant'],
        "price": deal['price'],
        "discount": deal['discount'],
        "url": deal['deal_url']
    }

    return Document(page_content=content.strip(), metadata=metadata)

def create_vector_store():
    # Get fresh deals
    deals = scraper.get_deals()
    
    # Convert to documents
    documents = [create_document(deal) for deal in deals]
    
    # Create and save vector store
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents=documents, embedding=embedder)
    vector_store.save_local('faiss_index')

if __name__ == '__main__':
    create_vector_store()
