 # Análisis de NLP: 'Análisis sobre la evolución del Merengue desde 1985 al 2007'

## Descripción
Breve descripción del corpus elegido: El corpus elegido está basado en canciones del genero Merengue, todas con temática sobre el 'amor', comprendidas entre los años 1985 al 2007. El corpus abarca 20 canciones, todas extraídas de las páginas: Genius.com, Letras.com. Cada una de ellas transformadas al formato .txt

Objetivos del análisis: Saber si evolucionó el lenguaje amoroso en el merengue entre 1985 y 2007, haciendo énfasis en las formas de describir el amor en las letras.

Principales hallazgos encontrados: Se descubrió que, en el merengue entre 1985 y 2007, los adjetivos casi no crecieron en importancia, lo que significa que las letras no se volvieron más descriptivas con el tiempo. Ademas, los verbos y los sutantivos fueron utilizados con mucha frecuencia en la década de los 80s-90s, y luego los tres grupos gramaticales fueron reduciendose a partir de los años 2000. 

## Información del Corpus
- **Tipo**: [Músical]
- **Tamaño**: 20 textos, aproximadamente 3100 palabras totales
- **Fuentes principales**: [Genius.com y Letras.com]
- **Período temporal**: [1985 al 2007]
- **Criterios de selección**: [Los elegí basandome en las cancionces más populares del género Merengue en el período de tiempo mencionado.]

## Técnicas de NLP Aplicadas
- Preprocesamiento de texto (limpieza, tokenización, stop words)
- Análisis con Bag of Words (BoW) y TF-IDF
- Análisis con Word Embeddings (spaCy)
- Técnica complementaria aplicada: POS Tagging

## Principales Hallazgos
- #1: El merengue parece haber enfatizado más los sustantivos (cosas, personas, conceptos) y los verbos (acciones, sentimientos, dinámicas) que los adjetivos (descripciones).
- #2: Los sustantivos fueron muy relevantes a fines de los 80s y principio de los 90s.
- #3: Hubo un cambio en los 90: los sustantivos bajaron mientras que los verbos subieron, lo que sugiere un viraje desde lo nominal (nombres, objetos) hacia lo activo (acciones, procesos) en las letras.
- #4: A partir de los 2000, se percibe una simplificación general: menos sustantivos y verbos, y pocos adjetivos, lo que podría reflejar un estilo más directo o repetitivo en las letras.
- #5 Se pudo evidenciar las diferencias estilísticas entre diferentes autores.
- Comparación entre métodos: Embedding fue el mejor enfoque, ya que al representar las palabras en un espacio semántico, permitió detectar similitudes temáticas más profundas entre canciones, incluso cuando no compartían vocabulario explícito. Pero, Pos Tagging fue el análisis que finalmente dió respuesta de la hipótesis planteada.

## Tecnologías Utilizadas
- Python 3.x
- pandas, numpy
- scikit-learn
- spaCy
- matplotlib, seaborn
- collections
- string
- re
- pickle

## Instrucciones de Reproducción
El notebook ya está debidamente ejecutado, se encuentra en la carpeta Notebook.

## Limitaciones y Trabajo Futuro
- No se pudo realizar el Análisis de Sentimientos porque textblolt daba valores nulos, probablemente porque está optimizado para textos en inglés.
- Tal vez enfocarlos a otros estilos músicales e incluso profundizar en el análisis por intérprete, especialmente en aquellos artistas que han explorado distintos géneros a lo largo de su carrera. Comparar cómo cambia su estilo lírico según el género musical permitiría entender mejor su evolución artística y emocional.

## Autor
Michell Andreina Zambrano Hereira - email: 19121189@ifts24.edu.ar / GitHub: https://github.com/michellzambranohereira/PLN
Trabajo Integrador - NLP - Fecha: 25/09/2025
