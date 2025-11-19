import streamlit as st
import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# --- Configuración de la página ---
st.set_page_config(page_title="Chatbot Harry Potter Reviews", page_icon="🪄")
st.title("🪄 Chatbot RAG: Reseñas de Harry Potter")
st.markdown("Consulta opiniones de usuarios sobre personajes y aspectos de las películas.")

# --- Sidebar ---
with st.sidebar:
    st.header("Información del corpus")
    st.write("Dataset: Harry Potter Reviews")
    st.write("Modelo: Flan-T5 base + Embeddings MiniLM-L6-v2")
    st.markdown("---")
    st.subheader("Ejemplos de consultas:")
    st.write("- ¿Qué comentarios negativos hay sobre Severus Snape?")
    st.write("- Opiniones de usuarios de España sobre Hermione Granger")
    st.write("- ¿Qué dicen los mayores de 40 años sobre Ron Weasley?")

# --- 1) Cargar dataset ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/michellzambranohereira/PLN/refs/heads/main/TP%20Final%20Integrador/dataset/rese%C3%B1as.csv"
    df = pd.read_csv(url)
    documentos = [
        Document(
            page_content=row["comment"],
            metadata={
                "user_id": row["user_id"],
                "user_sex": row["user_sex"],
                "user_age": row["user_age"],
                "user_country": row["user_country"],
                "rating": row["rating"],
                "favourite_character": row["favourite_character"],
                "date": row["date"]
            }
        )
        for _, row in df.iterrows()
    ]
    return documentos

documentos = load_data()

# --- 2) Preparar pipeline RAG ---
splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
chunks = splitter.split_documents(documentos)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings, collection_name="hp_reviews_collection")
retriever = db.as_retriever(search_kwargs={"k": 8})

model_id = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
hf_pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256, temperature=0)
llm = HuggingFacePipeline(pipeline=hf_pipe)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="map_reduce",
    retriever=retriever,
    return_source_documents=True
)

# --- 3) Interfaz principal ---
consulta = st.text_input("Escribí tu consulta:", placeholder="Ejemplo: ¿Qué comentarios negativos hay sobre Severus Snape?")
if st.button("Consultar", type="primary"):
    if not consulta:
        st.warning("Por favor, escribí una consulta.")
    else:
        with st.spinner("Buscando información relevante..."):
            try:
                resultado = qa_chain({"query": consulta})
                st.success("Consulta completada ✅")
                st.subheader("Respuesta:")
                st.write(resultado["result"])

                st.subheader("Fuentes consultadas:")
                for i, doc in enumerate(resultado["source_documents"], 1):
                    with st.expander(f"Fuente {i}"):
                        st.write(doc.page_content[:300] + "...")
                        st.caption(f"Metadata: {doc.metadata}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Intentá reformular tu consulta.")

