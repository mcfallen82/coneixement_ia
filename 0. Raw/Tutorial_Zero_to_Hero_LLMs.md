---
title: Tutorial Zero to Hero LLMs
raw_type: tutorial
source_type: tutorial
original_name: Tutorial_Zero_to_Hero_LLMs_Finances.md
processing_status: raw_ingested
status: raw_ingested
created: 2026-08-07
updated: 2026-08-13
previous_path: "0. Raw/0.1. llibres/Tutorial_Zero_to_Hero_LLMs.md"
---

# Tutorial escrit — Neural Networks: Zero to Hero, LLMs i documents financers

> Document de treball per estudiar xarxes neuronals, models de llenguatge i aplicacions a documents financers SEC com 10-K i 10-Q.

---

## Índex

1. [Objectiu del document](#1-objectiu-del-document)
2. [Mapa general d’aprenentatge](#2-mapa-general-daprenentatge)
3. [Capítol 1 — Micrograd i Autograd](#3-capítol-1--micrograd-i-autograd)
4. [Capítol 2 — Model bigrama](#4-capítol-2--model-bigrama)
5. [Capítol 3 — Model bigrama com a xarxa neuronal](#5-capítol-3--model-bigrama-com-a-xarxa-neuronal)
6. [Capítol 4 — Softmax i cross-entropy](#6-capítol-4--softmax-i-cross-entropy)
7. [Capítol 5 — MLP amb embeddings](#7-capítol-5--mlp-amb-embeddings)
8. [Capítol 6 — Mini-batches, train/dev/test i overfitting](#8-capítol-6--mini-batches-traindevtest-i-overfitting)
9. [Capítol 7 — Activacions, gradients i inicialització](#9-capítol-7--activacions-gradients-i-inicialització)
10. [Capítol 8 — BatchNorm i normalització](#10-capítol-8--batchnorm-i-normalització)
11. [Capítol 9 — Backpropagation manual avançat](#11-capítol-9--backpropagation-manual-avançat)
12. [Capítol 10 — WaveNet i context jeràrquic](#12-capítol-10--wavenet-i-context-jeràrquic)
13. [Capítol 11 — GPT des de zero](#13-capítol-11--gpt-des-de-zero)
14. [Capítol 12 — Adam](#14-capítol-12--adam)
15. [Capítol 13 — Tokenització i BPE](#15-capítol-13--tokenització-i-bpe)
16. [Capítol 14 — De models de joguina a LLMs reals](#16-capítol-14--de-models-de-joguina-a-llms-reals)
17. [Aplicació a documents financers SEC](#17-aplicació-a-documents-financers-sec)
18. [Ruta d’estudi recomanada](#18-ruta-destudi-recomanada)
19. [Referències externes](#19-referències-externes)

---

# 1. Objectiu del document

Aquest document converteix l’aprenentatge de la sèrie **Neural Networks: Zero to Hero** d’Andrej Karpathy i l’article **microgpt** en un tutorial escrit, estructurat i orientat a tres objectius:

1. Entendre les bases matemàtiques del deep learning.
2. Entendre com un model de llenguatge aprèn a predir el següent token.
3. Preparar una base conceptual per aplicar LLMs a documents financers com **10-K** i **10-Q** de la **Securities Exchange Commission**.

Els apartats ja treballats prèviament —Autograd, Parameters, Architecture i Training loop— apareixen en format resumit. Els apartats més delicats —Softmax, Adam, BatchNorm, inicialització i tokenització— reben una explicació més extensa.

---

# 2. Mapa general d’aprenentatge

La progressió conceptual és aquesta:

```text
micrograd
   ↓
autograd i backpropagation
   ↓
model bigrama
   ↓
model de llenguatge simple
   ↓
MLP amb embeddings
   ↓
activacions, inicialització i normalització
   ↓
models seqüencials més profunds
   ↓
Transformer / GPT
   ↓
tokenització real
   ↓
LLMs aplicats a documents financers
```

## Resum per capítols

| Capítol | Tema | Funció dins l’aprenentatge |
|---:|---|---|
| 1 | Micrograd / Autograd | Entendre com es calculen gradients automàticament |
| 2 | Model bigrama | Primer model de llenguatge estadístic |
| 3 | Bigrama neuronal | Veure el mateix model com una xarxa entrenable |
| 4 | Softmax i cross-entropy | Convertir logits en probabilitats i calcular error |
| 5 | MLP amb embeddings | Introduir representacions internes apreses |
| 6 | Mini-batches i validació | Entrenar sense autoenganyar-se |
| 7 | Activacions i inicialització | Evitar gradients dolents i xarxes inestables |
| 8 | BatchNorm | Normalitzar activacions durant l’entrenament |
| 9 | Backprop manual | Entendre què fa autograd per sota |
| 10 | WaveNet | Incorporar context de forma jeràrquica |
| 11 | GPT | Attention, MLP, residuals i logits |
| 12 | Adam | Optimització adaptativa moderna |
| 13 | Tokenització / BPE | Passar de text real a tokens útils |
| 14 | LLMs reals | Escala, dades, frameworks i inferència |

---

# 3. Capítol 1 — Micrograd i Autograd

Aquest capítol correspon al motor bàsic d’aprenentatge: **backpropagation**.

## Idea central

Una xarxa neuronal és una funció amb molts paràmetres:

\[
L = f(\theta_1, \theta_2, ..., \theta_n)
\]

On:

- \(L\) és la pèrdua o error.
- \(\theta_i\) són els paràmetres entrenables.
- L’objectiu és calcular:

\[
\frac{\partial L}{\partial \theta_i}
\]

per a cada paràmetre.

## Flux bàsic

```text
forward pass  → calcula prediccions
loss          → mesura error
backward pass → calcula gradients
update        → mou els pesos
```

## Regla de la cadena

Si:

\[
y = f(x)
\]

I:

\[
L = g(y)
\]

Llavors:

\[
\frac{dL}{dx} = \frac{dL}{dy} \cdot \frac{dy}{dx}
\]

El backpropagation aplica aquesta regla a un graf enorme d’operacions.

## Què cal retenir

Autograd és una màquina de calcular derivades parcials automàticament. Durant el forward pass construeix un graf de càlcul; durant el backward pass reparteix la responsabilitat de l’error cap enrere.

---

# 4. Capítol 2 — Model bigrama

El model bigrama és el primer model de llenguatge.

## Objectiu

Aprendre a predir el següent caràcter a partir del caràcter actual.

Si tenim noms com:

```text
emma
olivia
ava
isabella
```

Afegim un símbol especial d’inici/final, per exemple `.`:

```text
. e m m a .
```

Els bigrames són:

```text
. → e
e → m
m → m
m → a
a → .
```

## Probabilitat condicional

El model aprèn:

\[
P(y|x)
\]

És a dir: donat el caràcter actual \(x\), quina és la probabilitat del següent caràcter \(y\)?

## Matriu de freqüències

Construïm una matriu \(N\):

\[
N_{ij} = \text{vegades que el caràcter } j \text{ segueix el caràcter } i
\]

Després convertim cada fila en probabilitats:

\[
P_{ij} = \frac{N_{ij}}{\sum_j N_{ij}}
\]

## Generació

Per generar un nom:

```text
1. Comença amb "."
2. Tria el següent caràcter segons P(. → caràcter)
3. Tria el següent segons el caràcter actual
4. Repeteix fins tornar a "."
```

## Loss

Per cada bigrama real:

\[
x \rightarrow y
\]

la loss és:

\[
L = -\log P(y|x)
\]

Per tot el dataset:

\[
L = -\frac{1}{n}\sum_{k=1}^{n}\log P(y_k|x_k)
\]

## Smoothing

Si una combinació no apareix mai, tindria probabilitat zero:

\[
P(y|x)=0
\]

I això provocaria:

\[
-\log(0)=+\infty
\]

Per evitar-ho:

\[
P_{ij} = \frac{N_{ij}+\alpha}{\sum_j (N_{ij}+\alpha)}
\]

Això és suavització. Evita conclusions massa radicals a partir d’una mostra limitada.

---

# 5. Capítol 3 — Model bigrama com a xarxa neuronal

Karpathy reconstrueix el model bigrama com una xarxa neuronal mínima.

## One-hot encoding

Cada caràcter es representa com un vector amb un 1 i la resta zeros.

Exemple amb vocabulari reduït:

```text
a = [1, 0, 0]
b = [0, 1, 0]
c = [0, 0, 1]
```

## Logits

La xarxa fa:

\[
logits = xW
\]

On:

- \(x\) és el vector one-hot.
- \(W\) és una matriu entrenable.
- `logits` són puntuacions per al següent caràcter.

Després:

\[
probs = softmax(logits)
\]

I la loss és:

\[
L = -\log p_y
\]

## Idea clau

El model estadístic de freqüències i la petita xarxa neuronal poden acabar aprenent una informació semblant. La diferència és que la xarxa ho aprèn ajustant pesos amb gradients.

---

# 6. Capítol 4 — Softmax i cross-entropy

Softmax i cross-entropy són peces centrals dels models de classificació i dels models de llenguatge.

## 6.1. El problema

El model produeix logits:

\[
z = [z_1, z_2, ..., z_K]
\]

Aquests logits són puntuacions brutes. Poden ser positius, negatius, grans o petits.

Però volem probabilitats:

\[
p_i \geq 0
\]

I:

\[
\sum_i p_i = 1
\]

## 6.2. Fórmula de softmax

\[
p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}
\]

L’exponencial fa tres coses:

1. Converteix qualsevol valor en positiu.
2. Amplifica diferències entre logits.
3. Manté l’ordre: si \(z_i > z_j\), llavors \(e^{z_i} > e^{z_j}\).

## 6.3. Exemple numèric

Si:

\[
z = [2, 1, 0]
\]

Llavors:

\[
e^z = [7.39, 2.72, 1]
\]

Suma:

\[
7.39 + 2.72 + 1 = 11.11
\]

Probabilitats:

\[
p = [0.665, 0.245, 0.090]
\]

## 6.4. Estabilitat numèrica

Softmax té aquesta propietat:

\[
softmax(z) = softmax(z + c)
\]

Per qualsevol constant \(c\).

A la pràctica es fa:

\[
z'_i = z_i - \max(z)
\]

Això evita que \(e^{z_i}\) sigui massa gran i provoqui errors numèrics.

## 6.5. Temperatura

Una variant habitual és:

\[
p_i = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

On \(T\) és la temperatura.

| Temperatura | Efecte |
|---:|---|
| Baixa | Distribució més concentrada; sortida més conservadora |
| Alta | Distribució més plana; sortida més diversa però més erràtica |

## 6.6. Cross-entropy

Si el token correcte és \(y\), la pèrdua és:

\[
L = -\log p_y
\]

Exemples:

Si:

\[
p_y = 0.90
\]

\[
L = -\log(0.90) = 0.105
\]

Si:

\[
p_y = 0.01
\]

\[
L = -\log(0.01) = 4.605
\]

La cross-entropy castiga molt les prediccions que donen poca probabilitat al token correcte.

## 6.7. Gradient de softmax + cross-entropy

Quan combinem softmax amb cross-entropy, el gradient respecte als logits és molt simple:

\[
\frac{\partial L}{\partial z_i} = p_i - y_i
\]

On:

- \(p_i\) és la probabilitat predita.
- \(y_i\) és 1 si és la classe correcta, 0 si no.

Exemple:

| Token | \(p_i\) | \(y_i\) | Gradient \(p_i-y_i\) |
|---|---:|---:|---:|
| correcte | 0.70 | 1 | -0.30 |
| incorrecte A | 0.20 | 0 | 0.20 |
| incorrecte B | 0.10 | 0 | 0.10 |

Interpretació:

- El logit del token correcte ha de pujar.
- Els logits dels tokens incorrectes han de baixar.

Aquesta és una de les fórmules més netes de tot el deep learning.

---

# 7. Capítol 5 — MLP amb embeddings

Ara passem d’un model que només mira un caràcter a un model que mira una finestra de context.

## 7.1. Limitació del bigrama

El bigrama aprèn:

\[
P(x_{t+1}|x_t)
\]

Però el llenguatge sovint depèn de més context.

Per això volem:

\[
P(x_{t+1}|x_{t-k},...,x_t)
\]

## 7.2. Embeddings

Cada caràcter es converteix en un vector dens après.

Si el vocabulari té 27 caràcters i l’embedding té dimensió \(d\):

\[
C \in \mathbb{R}^{27 \times d}
\]

Cada caràcter té una fila:

\[
C[x]
\]

## 7.3. Context window

Amb 3 caràcters de context:

```text
. . e → predir m
. e m → predir m
e m m → predir a
```

Si cada embedding té 10 dimensions, el vector concatenat té:

\[
3 \times 10 = 30
\]

## 7.4. Xarxa MLP

El model fa:

\[
h = \tanh(xW_1 + b_1)
\]

\[
logits = hW_2 + b_2
\]

Després:

\[
probs = softmax(logits)
\]

I:

\[
L = -\log p_y
\]

## 7.5. Què aprèn l’embedding?

L’embedding permet que el model aprengui representacions internes. No veu només símbols aïllats; aprèn vectors que poden capturar similituds de comportament.

---

# 8. Capítol 6 — Mini-batches, train/dev/test i overfitting

## 8.1. Mini-batches

En lloc d’entrenar amb tot el dataset a cada pas, s’agafa un subconjunt:

```text
1. Agafo 32 exemples
2. Calculo la loss mitjana
3. Calculo gradients
4. Actualitzo pesos
5. Repeteixo
```

Això produeix una estimació sorollosa però útil del gradient:

\[
\nabla \hat{L}_B(\theta)
\]

On \(B\) és el batch.

## 8.2. Train/dev/test split

| Conjunt | Funció |
|---|---|
| Train | Ajustar pesos |
| Dev / validation | Escollir hiperparàmetres |
| Test | Mesurar rendiment final |

## 8.3. Overfitting

Un model pot aprendre molt bé el train set però generalitzar malament.

La pregunta important no és:

```text
Com de bé funciona amb el que ja ha vist?
```

Sinó:

```text
Com de bé funciona amb dades noves?
```

En finances, és l’equivalent a una estratègia massa optimitzada sobre el passat.

---

# 9. Capítol 7 — Activacions, gradients i inicialització

Aquest capítol explica per què una xarxa pot no aprendre encara que el codi sigui correcte.

## 9.1. Activacions saturades

Amb `tanh`:

\[
\tanh(x)
\]

La sortida està entre -1 i 1.

Quan \(x\) és molt gran:

\[
\tanh(x) \approx 1
\]

Quan \(x\) és molt petit:

\[
\tanh(x) \approx -1
\]

La derivada és:

\[
\frac{d}{dx}\tanh(x)=1-\tanh^2(x)
\]

Si \(\tanh(x) \approx 1\), llavors:

\[
1-\tanh^2(x) \approx 0
\]

El gradient gairebé desapareix.

## 9.2. Vanishing gradients

En xarxes profundes, els gradients es multipliquen enrere.

Si moltes derivades locals són menors que 1:

\[
0.5 \cdot 0.5 \cdot 0.5 \cdot ... \rightarrow 0
\]

El gradient s’esvaeix.

## 9.3. Exploding gradients

Si moltes derivades són superiors a 1:

\[
2 \cdot 2 \cdot 2 \cdot ... \rightarrow \infty
\]

El gradient explota.

## 9.4. Inicialització

La inicialització dels pesos controla l’escala inicial de les activacions.

Si els pesos són massa grans:

```text
activacions saturades
gradients dolents
entrenament inestable
```

Si són massa petits:

```text
senyal feble
gradients petits
aprenentatge lent
```

## 9.5. Diagnòstic

Cal observar:

```text
histogrames d'activacions
histogrames de gradients
loss durant l'entrenament
magnitud dels pesos
```

No n’hi ha prou que el codi funcioni. Cal que la xarxa aprengui de manera sana.

---

# 10. Capítol 8 — BatchNorm i normalització

BatchNorm és una tècnica per estabilitzar l’entrenament normalitzant activacions dins d’un batch.

## 10.1. El problema

Durant l’entrenament, els pesos canvien. Això fa que la distribució d’entrada de cada capa també canviï.

BatchNorm intenta estabilitzar aquesta distribució.

## 10.2. Fórmula

Per un batch de valors \(x\):

Mitjana:

\[
\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_i
\]

Variància:

\[
\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m}(x_i-\mu_B)^2
\]

Normalització:

\[
\hat{x}_i = \frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
\]

Reescalat après:

\[
y_i = \gamma \hat{x}_i + \beta
\]

## 10.3. Per què \(\gamma\) i \(\beta\)?

Si només normalitzéssim, obligaríem les activacions a tenir mitjana 0 i variància 1.

Però la xarxa pot necessitar una altra escala.

Els paràmetres \(\gamma\) i \(\beta\) permeten que el model recuperi l’escala que li convé.

## 10.4. Entrenament vs inferència

Durant entrenament, BatchNorm utilitza estadístiques del batch.

Durant inferència, utilitza mitjanes acumulades:

```text
running mean
running variance
```

Això fa que el comportament sigui diferent entre mode entrenament i mode inferència.

## 10.5. Què ensenya BatchNorm

BatchNorm mostra que entrenar xarxes neuronals no és només triar una arquitectura. També cal controlar la dinàmica interna de les activacions i gradients.

---

# 11. Capítol 9 — Backpropagation manual avançat

Aquest capítol serveix per entendre què fan les llibreries automàtiques.

## 11.1. Objectiu

Calcular manualment gradients de blocs com:

```text
embedding lookup
concatenació
matmul
BatchNorm
tanh
softmax
cross-entropy
```

## 11.2. Idea clau

Autograd no és màgia. Només aplica la regla de la cadena a totes les operacions.

## 11.3. Fórmula més important

Per softmax + cross-entropy:

\[
\frac{\partial L}{\partial z_i}=p_i-y_i
\]

Aquest és el primer gradient que torna enrere des de la sortida del model.

---

# 12. Capítol 10 — WaveNet i context jeràrquic

WaveNet introdueix una manera jeràrquica de processar seqüències.

## 12.1. Problema

Un MLP amb finestra fixa pot mirar només uns quants caràcters enrere.

Si augmentem molt la finestra, el vector d’entrada creix massa.

## 12.2. Solució jeràrquica

En lloc de processar tot el context de cop, es poden combinar patrons locals progressivament:

```text
parelles de caràcters
grups de quatre
grups de vuit
contextos més amplis
```

## 12.3. Connexió amb Transformers

WaveNet i Transformers no són iguals, però comparteixen una pregunta:

```text
Com combino informació distribuïda en una seqüència?
```

WaveNet ho fa de manera jeràrquica.

Transformers ho fan amb attention.

---

# 13. Capítol 11 — GPT des de zero

Aquest apartat ja ha estat treballat amb `microgpt`, per tant aquí només queda el mapa essencial.

## 13.1. Components principals

| Peça | Funció |
|---|---|
| Token embeddings | Representen tokens com vectors |
| Position embeddings | Informen de la posició |
| Attention | Permet mirar tokens anteriors |
| MLP | Processa informació local |
| Residual connections | Acumulen informació sense destruir l’anterior |
| LayerNorm / RMSNorm | Estabilitzen escala |
| LM head | Converteix vector intern en logits |
| Softmax + cross-entropy | Calculen probabilitats i error |

## 13.2. Evolució dels models de llenguatge

Bigrama:

\[
P(x_{t+1}|x_t)
\]

MLP amb finestra fixa:

\[
P(x_{t+1}|x_{t-k},...,x_t)
\]

GPT:

\[
P(x_{t+1}|x_{\leq t})
\]

## 13.3. Idea central

El GPT pot aprendre quines parts del context són rellevants per predir el següent token.

```text
embedding → attention → MLP → logits → softmax → loss
```

---

# 14. Capítol 12 — Adam

Adam és un optimitzador adaptatiu molt utilitzat en deep learning.

## 14.1. Descens del gradient simple

El descens del gradient fa:

\[
\theta_t = \theta_{t-1} - \eta g_t
\]

On:

\[
g_t = \nabla_\theta L(\theta_t)
\]

El problema és que tots els paràmetres reben el mateix learning rate \(\eta\).

## 14.2. Momentum

Momentum suavitza el gradient:

\[
m_t = \beta m_{t-1} + (1-\beta)g_t
\]

Això redueix zig-zags i acumula direcció si els gradients apunten de manera consistent.

## 14.3. Segon moment

Adam també mira el quadrat del gradient:

\[
v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2
\]

Això mesura l’escala històrica dels gradients.

## 14.4. Primer moment

Adam calcula:

\[
m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t
\]

És una mitjana mòbil del gradient.

## 14.5. Correcció de biaix

Com que \(m_0=0\) i \(v_0=0\), les primeres estimacions estan esbiaixades cap a zero.

Adam corregeix:

\[
\hat{m}_t = \frac{m_t}{1-\beta_1^t}
\]

\[
\hat{v}_t = \frac{v_t}{1-\beta_2^t}
\]

## 14.6. Actualització final

\[
\theta_t = \theta_{t-1} - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}
\]

Interpretació:

```text
direcció = gradient suavitzat
escala = arrel del segon moment
pas = learning rate adaptatiu per paràmetre
```

## 14.7. Adam com a intuïció financera

Pensa en una estratègia que ajusta posicions segons senyals:

- El primer moment és la direcció recent del senyal.
- El segon moment és la volatilitat recent del senyal.
- L’actualització ajusta la mida del pas segons la volatilitat.

Adam no elimina el risc d’un mal learning rate, dades dolentes o arquitectura inadequada. Però acostuma a donar entrenaments més estables que el gradient descent simple.

---

# 15. Capítol 13 — Tokenització i BPE

La tokenització és el pont entre text i model.

## 15.1. El model no veu text

Un LLM no rep paraules directament. Rep enters:

```text
text → tokens → ids numèrics → vectors
```

## 15.2. Per què no tokenitzar per paraules?

Perquè el vocabulari explotaria amb:

```text
plurals
majúscules
noms propis
errors tipogràfics
termes tècnics
idiomes diferents
símbols financers
```

## 15.3. Per què no tokenitzar per caràcters?

Perquè les seqüències serien molt llargues.

Un model tindria menys informació per token i necessitaria més passos per entendre el mateix text.

## 15.4. BPE

**Byte Pair Encoding** comença amb unitats petites i fusiona parelles freqüents.

Exemple conceptual:

```text
l + o → lo
lo + w → low
e + r → er
```

Les paraules freqüents poden quedar com tokens grans. Les rares es descomponen en subparaules.

## 15.5. Importància en documents financers

Els 10-K i 10-Q tenen molts termes especialitzats:

```text
Adjusted EBITDA
non-GAAP
Item 7
ASC 606
goodwill impairment
restructuring charges
share-based compensation
```

Un bon tokenitzador ajuda a preservar patrons útils. Un mal tokenitzador pot trencar massa els termes i dificultar el raonament.

## 15.6. Cost de context

Els documents SEC són llargs. Tokenitzar-los bé importa perquè el context disponible és limitat.

No sempre pots posar tot un 10-K dins del model.

Cal fer:

```text
segmentació → chunking → recuperació → resposta amb evidència
```

---

# 16. Capítol 14 — De models de joguina a LLMs reals

## 16.1. Progressió

| Projecte | Funció |
|---|---|
| micrograd | Entendre gradients |
| makemore | Entendre modelatge de llenguatge |
| microGPT | Veure un GPT mínim en una sola peça |
| nanoGPT | Entrenament més realista amb PyTorch |
| LLM real | Escala, dades massives, optimització i infraestructura |

## 16.2. Què canvia en models reals?

Canvien sobretot:

```text
mida del model
quantitat de dades
qualitat del tokenitzador
infraestructura GPU
optimització distribuïda
fine-tuning
post-entrenament
avaluació
seguretat
inferència eficient
```

## 16.3. Què es manté?

Es manté el batec bàsic:

```text
text
tokens
vectors
xarxa neuronal
logits
softmax
loss
backpropagation
optimització
```

---

# 17. Aplicació a documents financers SEC

Aquest bloc connecta l’aprenentatge amb documents 10-K i 10-Q.

## 17.1. Problema pràctic

Un 10-K no és només text. Conté:

```text
narrativa de negoci
factors de risc
MD&A
estats financers
taules
notes comptables
segments
mètriques no-GAAP
litigis
adquisicions
```

Un LLM ha de poder:

1. Localitzar la secció correcta.
2. Recuperar el fragment rellevant.
3. Interpretar-lo.
4. Fer càlculs si cal.
5. Citar evidència.
6. Separar dades de conclusions.

## 17.2. Pipeline recomanat

```text
SEC EDGAR
   ↓
descàrrega del filing
   ↓
neteja HTML / XBRL
   ↓
segmentació per Items
   ↓
chunking
   ↓
embeddings
   ↓
recuperació semàntica / híbrida
   ↓
LLM amb context seleccionat
   ↓
extracció estructurada
   ↓
validació i cites
```

## 17.3. Segmentació per Items

En un 10-K, és crític separar:

| Item | Contingut |
|---|---|
| Item 1 | Business |
| Item 1A | Risk Factors |
| Item 7 | MD&A |
| Item 7A | Market Risk |
| Item 8 | Financial Statements |
| Notes | Polítiques comptables i detalls |

Abans de preguntar a un LLM, convé saber d’on prové cada fragment.

## 17.4. Tasques possibles

| Tasca | Exemple |
|---|---|
| Extracció | “Extreu revenue, gross margin i operating income” |
| Comparació | “Com ha canviat el risc de client concentrat respecte l’any anterior?” |
| Detecció de canvis | “Què ha canviat a Item 1A?” |
| Raonament numèric | “Calcula la variació del marge brut i explica’n els drivers” |
| Evidència | “Cita la frase o taula que justifica la resposta” |
| Classificació | “Aquest risc és operatiu, financer, regulatori o competitiu?” |

## 17.5. Riscos habituals

```text
al·lucinacions
errors de càlcul
fragments recuperats fora de context
confusió entre anys fiscals
confusió entre GAAP i non-GAAP
no distingir dades reals de narrativa de management
ignorar notes comptables
```

## 17.6. Connexió amb Zero to Hero

| Concepte | Aplicació financera |
|---|---|
| Tokenització | Convertir filings llargs en unitats processables |
| Embeddings | Representar fragments financers |
| Softmax | Triar respostes, classes o tokens |
| Cross-entropy | Entrenar classificadors/extractors |
| Attention | Relacionar fragments distants del document |
| Context window | Límit pràctic en filings llargs |
| RAG | Recuperar fragments rellevants |
| Evaluation | Mesurar exactitud, cites i càlculs |

---

# 18. Ruta d’estudi recomanada

## Fase 1 — Fonament matemàtic

1. Autograd i backpropagation.
2. Softmax i cross-entropy.
3. Descens del gradient i Adam.

Objectiu:

```text
entendre com aprèn el model
```

## Fase 2 — Llenguatge com a predicció

1. Model bigrama.
2. MLP amb embeddings.
3. Mini-batches i validació.

Objectiu:

```text
entendre que un LLM és una màquina de probabilitats condicionals
```

## Fase 3 — Xarxes profundes sanes

1. Inicialització.
2. Activacions.
3. BatchNorm / normalització.
4. Diagnòstic de gradients.

Objectiu:

```text
entendre per què entrenar una xarxa és delicat
```

## Fase 4 — Transformer i LLMs

1. Attention.
2. MLP dins del Transformer.
3. Residual stream.
4. Tokenització BPE.
5. nanoGPT.

Objectiu:

```text
entendre què separa un model de joguina d’un LLM modern
```

## Fase 5 — Aplicació SEC

1. SEC EDGAR.
2. Segmentació de 10-K / 10-Q.
3. Extracció de dades.
4. RAG financer.
5. Validació amb cites.
6. Comparació anual.
7. Detecció de patrons d’inversió.

---

# 19. Referències externes

## Curs i codi base

- Andrej Karpathy — Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- Repositori oficial `nn-zero-to-hero`: https://github.com/karpathy/nn-zero-to-hero
- Andrej Karpathy — nanoGPT: https://github.com/karpathy/nanoGPT

## Softmax i classificació

- Stanford CS231n — Linear Classification and Softmax: https://cs231n.github.io/linear-classify/

## Adam

- Kingma & Ba — Adam: A Method for Stochastic Optimization: https://arxiv.org/abs/1412.6980

## BatchNorm

- Ioffe & Szegedy — Batch Normalization: https://arxiv.org/abs/1502.03167

## Transformer

- Vaswani et al. — Attention Is All You Need: https://arxiv.org/abs/1706.03762

## Tokenització i BPE

- Sennrich, Haddow & Birch — Neural Machine Translation of Rare Words with Subword Units: https://arxiv.org/abs/1508.07909
- Hugging Face Course — Byte-Pair Encoding tokenization: https://huggingface.co/learn/llm-course/en/chapter6/5

## Documents financers i SEC

- SEC EDGAR APIs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- FinQA — A Dataset of Numerical Reasoning over Financial Data: https://arxiv.org/abs/2109.00122
- TAT-QA — Question Answering over Tabular and Textual Data: https://aclanthology.org/2021.acl-long.254/
- DocFinQA — Financial Question Answering over Long Documents: https://arxiv.org/abs/2401.06915
- Form 10-K Itemization: https://arxiv.org/abs/2303.04688

---

# Resum final

La idea central de tot el recorregut és aquesta:

```text
Una xarxa neuronal aprèn ajustant matrius amb gradients.
Un model de llenguatge aplica això a predir el següent token.
Un GPT hi afegeix embeddings, attention, MLPs, normalització, tokenització i escala.
Un sistema financer sobre 10-K/10-Q hi afegeix recuperació, segmentació, evidència i validació.
```

Per estudiar LLMs aplicats a finances, la clau no és només saber fer servir un model. La clau és entendre la cadena completa:

```text
text financer
   ↓
tokens
   ↓
fragments recuperables
   ↓
representacions vectorials
   ↓
raonament del model
   ↓
resposta estructurada
   ↓
evidència verificable
```

Aquest document pot servir com a base per crear una wiki local, un Agent.md temàtic o un itinerari d’estudi aplicat al projecte Beagle/Valkyria.
