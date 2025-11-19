Sistema RAG — Análisis de Reseñas de Harry Potter

Descripción: 
Este proyecto implementa un Sistema de Retrieval-Augmented Generation (RAG) capaz de responder preguntas basadas en un corpus de 100 reseñas de películas de Harry Potter, utilizando: 

- Embeddings locales (MiniLM-L6-v2)

- ChromaDB como base vectorial

- Flan-T5-base como modelo generador

- Streamlit como interfaz web

Este sistema permite consultar opiniones, sentimientos y patrones narrativos presentes en las reseñas.

Demo: 

Ejecución local
streamlit run app.py

El sistema no requiere API keys ni GPU.
Funciona 100% local con modelos de Hugging Face.

Problema que Resuelve:

Los datasets de reseñas suelen ser extensos, repetitivos y difíciles de analizar manualmente.
Este sistema:
- Permite preguntar directamente sobre el contenido del corpus.

- Recupera las reseñas más relevantes y genera una síntesis automática.

- Es ideal para análisis de opinión, extracción de sentimientos y detección de patrones narrativos.

¿Por qué RAG?: Permite combinar la información real del corpus con la capacidad generativa del modelo evitando alucinaciones y respuestas sin fuente.

Arquitectura del Sistema: 

Pipeline RAG

1. Ingesta

Se carga el dataset reseñas.csv desde GitHub.

Cada fila se transforma en un objeto Document() de LangChain.

2. Chunking

Se utiliza RecursiveCharacterTextSplitter

chunk_size = 400

chunk_overlap = 50

Esto permite que los fragmentos tengan suficiente contexto sin ser demasiado largos.

3. Embeddings

Modelo utilizado:

sentence-transformers/all-MiniLM-L6-v2

Motivos:

- Ligero y rápido

- Funciona bien en español

- Ideal para correr sin GPU

4. Almacenamiento (Vectorstore)

Se usa: Chroma.from_documents(..., collection_name="hp_reviews_collection")

En memoria (sin persistencia) para evitar errores de permisos.

5. Retrieval

Estrategia:

Búsqueda por similitud

k = 5 documentos relevantes por consulta

6. Generation

Modelo generativo:

google/flan-t5-base

Integrado con:

HuggingFacePipeline

7. Interfaz (UI)

Hecha con Streamlit:

- Campo de texto para ingresar consultas

- Spinner de carga

- Respuesta generada

- Reseñas utilizadas como fuente

Diagrama de Flujo:
<img width="226" height="531" alt="image" src="https://github.com/user-attachments/assets/357ba9ea-5a9c-4c04-be00-0cd89c440ede" />

Stack Tecnológico: 
Componente	  /  Tecnología
LLM	             Flan-T5-Base (Hugging Face)
Embeddings	     MiniLM-L6-v2
Vector DB	       ChromaDB
Framework RAG	   LangChain
Interfaz	       Streamlit
Deployment	     Ejecución local

Ejecución Local:

1. Crear entorno
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar la aplicación
streamlit run app.py
