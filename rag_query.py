from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import ingest_to_vector_db
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize vector database
db_path = 'faiss_index'
if not os.path.exists(db_path):
    ingest_to_vector_db.create_vector_store()

embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.load_local("faiss_index", embeddings=embedder, allow_dangerous_deserialization=True)

# Prompt template
template = """
Based on the provided context, respond to the user query about shopping deals:

Query: {input}

Context:
{context}

Format the response as follows:
1. Brief summary of relevant deals
2. List of matching offers with:
   - Product name
   - Price
   - Discount
   - Store/Brand
   - Category
   - Link to offer

If no relevant offers found, respond with: "No matching deals found."
"""

prompt = PromptTemplate.from_template(template)
llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.0)
model = prompt | llm | StrOutputParser()

def query(input):
    docs = vector_db.similarity_search(query=input, k=5)
    context = '\n'.join(doc.page_content for doc in docs)
    return model.invoke({'input': input, 'context': context})
