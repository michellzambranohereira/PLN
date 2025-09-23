 # Análisis de NLP: 'Análisis sobre la evolución del Merengue desde 1985 al 2007'

## Descripción
Breve descripción del corpus elegido: El corpus elegido está basado en canciones del genero Merengue, todas con temática sobre el 'amor', comprendidas entre los años 1985 al 2007. El corpus abarca 20 canciones, todas extraídas de las páginas: Genius.com, Letras.com. Cada una de ellas transformadas al formato .txt

Objetivos del análisis: Saber si en términos de letras el merengue a ido evolucionando en sus descripciones sobre el amor.

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
- #1: El uso de adjetivos en las cancionces de Merengue no cambió sustancialmente dentro del período de estudio, indicando que en realidad el Merengue no se sustenta en descripciones sobre el amor, sino en un lenguaje más activo y narrativo
- #2: Uso elevado de sustantivos en la década de los 80s-90s, que refuerzan el estilo poético.
- #3: En los 90s, las letras se centraron mucho más en verbos, es decir, en narrar lo que ocurre en la relación: buscar, perder, sufrir, enamorarse.
- Comparación entre métodos: Embbedings fue el mejor enfoque para poder dar respuesta la hipótesis planteada, ya que al representar las palabras en un espacio semántico, permitió detectar similitudes temáticas más profundas entre canciones, incluso cuando no compartían vocabulario explícito.

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
