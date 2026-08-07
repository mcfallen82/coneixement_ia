---
title: Taula de lectures
source_type: reading_plan
original_name: Taula_Lectures.xlsx
status: processed
created: 2026-08-07
updated: 2026-08-07
processed_into:
  - "1. Wiki/1.2. conceptes/"
  - "1. Wiki/1.3. models/"
---

# Taula de lectures

> Transcripció fidel i consultable de `Taula_Lectures.xlsx`. És una font bruta i un pla de lectura: els enllaços a fitxes permanents s’afegeixen només quan el recurs aporta un concepte, una arquitectura, un model o un patró prou diferenciat.

## Criteri de processament

La taula barreja tres tipus d’entrades:

- **recursos pedagògics**: cursos, tutorials i repositoris;
- **models i arquitectures**: candidats a `1. Wiki/1.3. models/`;
- **datasets, benchmarks i casos d’aplicació**: evidència per a fitxes conceptuals, no models.

Les entrades financeres s’utilitzen com a casos per entendre [[1. Wiki/1.2. conceptes/raonament_numeric_documental]], recuperació d’informació i validació. No redefineixen l’abast general de la wiki.

## Primers papers i recursos

| Prioritat | Recurs | Per què és important | Tractament |
|---:|---|---|---|
| 1 | Neural Networks: Zero to Hero — Andrej Karpathy | Backpropagation, xarxes neuronals, makemore i nanoGPT des de zero. | Font de [[1. Wiki/1.2. conceptes/backpropagation]] i [[1. Wiki/1.3. models/nanoGPT]]. |
| 2 | GPT in 60 Lines of NumPy — Jay Mody | *Forward pass* d’un GPT amb poques abstraccions. | Lectura pràctica complementària de [[1. Wiki/1.3. models/GPT]]. |
| 3 | The Illustrated Transformer — Jay Alammar | Explicació visual d’atenció i Transformer. | Lectura introductòria de [[1. Wiki/1.3. models/transformer]]. |
| 4 | The Illustrated GPT-2 — Jay Alammar | Transformer de només descodificador i generació autoregressiva. | Lectura introductòria de [[1. Wiki/1.3. models/GPT-2]]. |
| 5 | FinQA | Preguntes financeres amb raonament numèric i càlcul explicable. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| 6 | TAT-QA | Preguntes que combinen taules i text. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| 7 | DocFinQA | QA sobre documents SEC llargs. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| 8 | Form 10-K Itemization | Segmentació d’ítems de 10-K. | Cas d’estudi de preprocessament documental. |
| 9 | SEC EDGAR APIs | Accés oficial a submissions i dades XBRL. | Font externa; no és un model ni un concepte nou. |
| 10 | A Scalable Data-Driven Framework for SEC 10-K Filings Using LLMs | Pipeline complet de processament amb LLMs. | Cas d’estudi per a RAG i validació. |

## Fonaments de *deep learning*

| Recurs | Què n’estudiaria | Enllaç permanent |
|---|---|---|
| Neural Networks: Zero to Hero — Karpathy | Autograd, xarxes neuronals, makemore i transició a GPT. | [[1. Wiki/1.2. conceptes/autodiferenciacio]], [[1. Wiki/1.2. conceptes/backpropagation]]. |
| nanoGPT lecture / codi de Karpathy | GPT petit entrenable amb PyTorch. | [[1. Wiki/1.3. models/nanoGPT]]. |
| GPT in 60 Lines of NumPy — Jay Mody | Embeddings, atenció, MLP i logits. | [[1. Wiki/1.2. conceptes/embeddings]], [[1. Wiki/1.2. conceptes/attention]]. |
| picoGPT — Jay Mody | Implementació mínima de GPT-2 en NumPy. | Recurs pràctic; no crea un model diferenciat. |
| The Illustrated Transformer — Jay Alammar | Atenció, encoder-decoder i self-attention. | [[1. Wiki/1.3. models/transformer]]. |
| The Illustrated GPT-2 — Jay Alammar | GPT-2 i generació de text. | [[1. Wiki/1.3. models/GPT-2]]. |
| Hugging Face LLM Course | Tokenitzadors, models, *fine-tuning* i *pipelines*. | [[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]. |
| Tokenizers — Hugging Face Course | Conversió de text en tokens i cost de context. | [[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]. |
| How do Transformers work? — Hugging Face | Famílies de Transformer i ús aplicat. | [[1. Wiki/1.3. models/transformer]]. |

## Papers i datasets documentals

| Recurs | Paper dins el pla | Tractament |
|---|---|---|
| FinQA | Preguntes-respostes amb programes de càlcul anotats. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| FinQA project page | Pàgina pràctica del dataset. | Font complementària. |
| TAT-QA | Context híbrid de taules i text. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| TAT-QA project page | Descripció i exemples del projecte. | Font complementària. |
| ConvFinQA | Converses multi-pas sobre documents financers. | Benchmark de QA conversacional; pendent de fitxa de font. |
| DocFinQA | Documents SEC complets i context llarg. | Dataset de [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]. |
| FinLongDocQA / Document-Level Numerical Reasoning | Raonament sobre documents llargs i múltiples taules. | Benchmark; pendent de fitxa de font. |
| FinanceReasoning Benchmark | Avaluació del raonament financer numèric. | Benchmark; pendent de fitxa de font. |

## Extracció estructural de 10-K

| Recurs | Paper dins el pla | Tractament |
|---|---|---|
| SEC EDGAR APIs — documentació oficial | Obtenció de submissions, company facts i XBRL. | Font operativa. |
| SEC EDGAR API Python / Read the Docs | Accés pràctic a les dades SEC. | Lectura d’implementació. |
| Introduction to Working with the SEC’s EDGAR API | Tutorial d’endpoints i metadades. | Lectura d’implementació. |
| Form 10-K Itemization | Segmentació per ítems abans de NLP o RAG. | Cas d’estudi de preprocessament. |
| Framework for SEC 10-K Using LLMs | Extracció, segmentació i valoracions amb LLM. | Cas d’estudi de pipeline. |
| Extracting Financial Data from SEC 10-K Filings with LLMs | Extracció estructurada cap a CSV. | Cas d’estudi d’extracció. |
| Mining Financial Data from SEC Filings with LlamaExtract | Extracció de riscos i *benchmarking*. | Cas d’estudi d’arquitectura. |
| RAG Chatbot for 10-Q and 10-K Reports | RAG sobre filings. | Cas d’estudi de [[RAG]]. |

## Models estructurats

| Recurs | Per què és rellevant | Tractament |
|---|---|---|
| FinBERT | Model BERT adaptat al llenguatge financer. | [[1. Wiki/1.3. models/FinBERT]]. |
| FinBERT: A Pre-trained Financial Language Representation Model | Variant acadèmica per a mineria de text financer. | Font complementària de FinBERT. |
| FinBERT-XRC | Classificació de risc amb explicacions. | Model de tasca específica; pendent de contrastar en una fitxa pròpia. |
| Transformer-based Summarization and Sentiment Analysis on 10-K Reports | Resum i sentiment de 10-K. | Cas d’aplicació, no un model base. |
| Evaluating LLMs in Financial NLP over 10-K Business Sections | Avaluació de LLMs sobre textos 10-K. | Benchmark. |
| Evaluating LLMs for Stance Detection on SEC Filings and Earnings Calls | Detecció de posició en filings i trucades. | Benchmark / tasca. |

## Fitxes creades en aquest processament

### Conceptes

- [[1. Wiki/1.2. conceptes/xarxes_neuronals]]
- [[1. Wiki/1.2. conceptes/autodiferenciacio]]
- [[1. Wiki/1.2. conceptes/backpropagation]]
- [[1. Wiki/1.2. conceptes/optimitzacio_i_adam]]
- [[1. Wiki/1.2. conceptes/softmax_i_cross_entropy]]
- [[1. Wiki/1.2. conceptes/embeddings]]
- [[1. Wiki/1.2. conceptes/tokenitzacio_i_bpe]]
- [[1. Wiki/1.2. conceptes/entrenament_validacio_i_overfitting]]
- [[1. Wiki/1.2. conceptes/activacions_i_inicialitzacio]]
- [[1. Wiki/1.2. conceptes/batch_normalization]]
- [[1. Wiki/1.2. conceptes/attention]]
- [[1. Wiki/1.2. conceptes/raonament_numeric_documental]]

### Models

- [[1. Wiki/1.3. models/transformer]]
- [[1. Wiki/1.3. models/WaveNet]]
- [[1. Wiki/1.3. models/GPT]]
- [[1. Wiki/1.3. models/GPT-2]]
- [[1. Wiki/1.3. models/nanoGPT]]
- [[1. Wiki/1.3. models/FinBERT]]
