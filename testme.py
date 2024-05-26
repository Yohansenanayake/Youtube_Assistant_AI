from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores  import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import JinaEmbeddings
from langchain_ai21 import AI21SemanticTextSplitter


load_dotenv()

user_input = "What is the video about?"
url = "https://youtu.be/HCOQmKTFzYY?si=TFEoYFyL6B4sihgp"

#embeddings = OpenAIEmbeddings()
embeddings = JinaEmbeddings(
    jina_api_key="jina_82207cdb72b4418d9ed50e0d0a5b6404DG-DpT8WejhqlS0vijOzpFzX2klD", model_name="jina-embeddings-v2-base-en"
)

loader = YoutubeLoader.from_youtube_url(url)
transcripts = loader.load()
text = transcripts[0].page_content

semantic_text_splitter = AI21SemanticTextSplitter()
documents = semantic_text_splitter.split_text_to_documents(text)

print(f"The text has been split into {len(documents)} Documents.")
for doc in documents:
    print(f"type: {doc.metadata['source_type']}")
    print(f"text: {doc.page_content}")
    print("====")



""" 
transcript = " ".join(transcripts)

semantic_text_splitter = AI21SemanticTextSplitter(chunk_size=1000,chunk_overlap=100,api_key="P4jjGopn6jOnnXioXaS9U8RAVqx74D9t")
docs= semantic_text_splitter.split_text_to_documents(transcript)
print(docs)
 """