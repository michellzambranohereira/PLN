import streamlit as st
import pandas as pd

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


# =========================
# CONFIG STREAMLIT
# =========================
st.set_page_config(page_title="Chatbot Harry Potter Reviews", page_icon="🪄")
st.title("🪄 Chatbot RAG: Reseñas de Harry Potter")


# =========================
# CARGA DATASET
# =========================
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/michellzambranohereira/PLN/refs/heads/main/TP%20Final%20Integrador/dataset/rese%C3%B1as.csv"
    df = pd.read_csv(url)

    documentos = [
        Document(
            page_content=row["reseña"],
            metadata={
                "titulo_pelicula": row["titulo_pelicula"],
                "sentimiento": row["sentimiento"]
            }
        )
        for _, row in df.iterrows()
    ]

    return documentos


documentos = load_data()


# =========================
# CONFIG RAG
# =========================
@st.cache_resource
def setup_rag():

    # 1) Chunking
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documentos)

    # 2) Embeddings LOCALES (NO GEMINI)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 3) ChromaDB en memoria
    db = Chroma.from_documents(
        chunks,
        embeddings,
        collection_name="hp_reviews_collection"
    )
    retriever = db.as_retriever(search_kwargs={"k": 5})

    # 4) LLM local (NO GEMINI)
    model_id = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    text_gen = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0
    )

    llm = HuggingFacePipeline(pipeline=text_gen)

    # 5) Cadena QA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa


qa_chain = setup_rag()


# =========================
# UI CONSULTA
# =========================
consulta = st.text_input(
    "Escribí tu consulta:",
    placeholder="Ejemplo: ¿Qué comentarios negativos hay sobre Snape?"
)

if st.button("Consultar"):

    if not consulta:
        st.warning("Escribí una consulta.")
    else:
        with st.spinner("Buscando respuesta..."):
            respuesta = qa_chain({"query": consulta})

            st.subheader("📌 Respuesta:")
            st.write(respuesta["result"])

            st.subheader("📚 Fuentes usadas:")
            for doc in respuesta["source_documents"]:
                st.write(doc.page_content)
                st.caption(doc.metadata)
