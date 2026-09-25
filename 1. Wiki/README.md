# 📚 Wiki — coneixement permanent sobre IA

## Una guia per llegir i ampliar les fitxes

La wiki és el nucli de coneixement de **coneixement_ia**. Transforma articles, documentació, llibres i altres fonts verificables en explicacions pròpies que es poden consultar i relacionar. Inclou fonaments d'intel·ligència artificial, models de llenguatge i sistemes de coneixement; les finances i l'economia hi apareixen com a casos d'aplicació.

Una fitxa permanent ha de respondre què és una idea, per què importa, com funciona, d'on prové i amb quines altres idees es relaciona. La wiki creix quan una font nova amplia o corregeix fitxes existents, no només quan s'afegeixen pàgines.

## 🗂️ Contingut de les carpetes

### 👥 [1.1. autors](1.1.%20autors/)

Fitxes de persones que han contribuït a la recerca, la divulgació o la pràctica de la IA i de l'organització del coneixement. Cada pàgina situa l'autor en el seu àmbit, identifica obres o projectes rellevants i l'enllaça amb els conceptes o models que ajuda a entendre. És un bon punt d'entrada si vols seguir l'origen d'una idea o descobrir altres aportacions de la mateixa persona.

### 💡 [1.2. conceptes](1.2.%20conceptes/)

Explicacions de les idees i tècniques que formen el vocabulari de la wiki: des de xarxes neuronals, atenció i embeddings fins a RAG, agents i gestió del coneixement. Les fitxes combinen definició, intuïció, funcionament, exemples, limitacions i relacions. Consulta-les quan necessitis entendre una peça abans de llegir un model o aplicar una tècnica.

### 🤖 [1.3. models](1.3.%20models/)

Fitxes d'arquitectures, models concrets i famílies de models, com ara Transformer, GPT, FinBERT o Jev. Expliquen quin problema aborda cada model, com s'estructura quan hi ha informació documentada, quines entrades i sortides admet, com s'entrena, en què pot ser útil i quins límits té. També hi ha fitxes sobre enfocaments de sistemes de coneixement: revisa el contingut i les fonts de cadascuna abans d'atribuir-li propietats d'un model entrenat.

### 📖 [1.4. llibres](1.4.%20llibres/)

Fitxes de llibres llegits com a fonts d'aprenentatge. Recullen les idees que val la pena conservar, les connexions amb altres fitxes i les possibles aplicacions, amb la referència bibliogràfica corresponent. Serveixen per recuperar el valor d'una lectura sense confondre el resum d'una obra amb una fitxa conceptual autònoma.

## 🧭 Com navegar per la wiki

Comença per un [concepte](1.2.%20conceptes/) si tens una pregunta concreta, per un [model](1.3.%20models/) si vols entendre'n el funcionament, o per un [autor](1.1.%20autors/) o un [llibre](1.4.%20llibres/) si parteixes d'una font. Segueix els enllaços entre fitxes per aprofundir. L'[índex general](../index.md) ofereix una altra vista del conjunt, i el [README del repositori](../README.md) explica com encaixa la wiki amb les skills, els quadres de seguiment i les plantilles.

## ✍️ Com incorporar o revisar una fitxa

1. **Comprova què ja existeix:** cerca duplicats, sinònims i fitxes relacionades abans de crear una pàgina.
2. **Tria la categoria:** autor, concepte, model o llibre segons el contingut principal; evita confondre una tècnica amb un model o una font amb la idea que exposa.
3. **Explica i relaciona:** escriu una síntesi pròpia, indica'n aplicacions i límits, i afegeix enllaços interns que ajudin a seguir l'explicació.
4. **Conserva la procedència:** usa el camp `sources` i URLs o referències bibliogràfiques verificables. Les fitxes permanents porten frontmatter; els README en queden exempts.
5. **Valida el canvi:** aplica les [plantilles de fitxes](../4.%20Templates/90.1.%20templates_fitxes/), les [regles del projecte](../AGENTS.md) i les comprovacions corresponents abans de proposar-lo.

## 🧩 Criteri per als README

Els README són guies d'entrada al contingut, no fitxes permanents. En actualitzar-ne un, mantén una estructura reconeixible: **títol, subtítol o introducció, mapa del contingut amb enllaços, explicació del propòsit de cada secció i orientacions d'ús o manteniment**. Empra subtítols clars i emojis discrets per facilitar la lectura. Descriu només carpetes i documents reals, adapta el detall a la mida de l'àmbit i explica prou context perquè el lector sàpiga què hi trobarà i com utilitzar-ho; una simple llista o una frase resum no és suficient. La norma comuna per a tot el repositori figura a [`AGENTS.md`](../AGENTS.md).
