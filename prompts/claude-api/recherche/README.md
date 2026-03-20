# Claude API -- Recherche

## Description

Prompts et patterns pour utiliser l'API Claude dans la recherche d'information : RAG (Retrieval-Augmented Generation), analyse de documents, extraction d'information et synthese de corpus.

## Cas d'usage
- RAG sur une base de connaissances locale
- Extraction d'information structuree depuis des documents
- Synthese de corpus de documents
- Question-answering sur de la documentation
- Analyse comparative de documents

---

## Prompts prets a copier

### 1 -- RAG simple avec embeddings

```
## ARCHITECTURE
1. Indexation : decouper les docs en chunks, generer des embeddings
2. Recherche : trouver les chunks pertinents par similarite
3. Generation : Claude repond en utilisant les chunks comme contexte

## CODE
def rag_query(question: str, knowledge_base: list) -> str:
    # Recherche des chunks pertinents
    relevant_chunks = search_similar(question, knowledge_base, top_k=5)
    context = "\n---\n".join(relevant_chunks)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=[{
            "type": "text",
            "text": f"Reponds en utilisant uniquement ces sources :\n{context}",
            "cache_control": {"type": "ephemeral"}
        }],
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

## PROMPT CACHING
Le contexte (sources) est cache → cout reduit pour les questions suivantes sur le meme corpus.
```

---

### 2 -- Extraction d'information structuree

```
def extract_info(document: str, schema: dict) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Extrais les informations du document selon ce schema JSON : {json.dumps(schema)}. Si une information n'est pas trouvee, utilise null.",
        messages=[{"role": "user", "content": document}]
    )
    return json.loads(response.content[0].text)

## SCHEMAS EXEMPLES
# CV
schema_cv = {"nom": "str", "email": "str", "competences": ["str"], "experience": [{"poste": "str", "entreprise": "str", "duree": "str"}]}

# Facture
schema_facture = {"numero": "str", "date": "str", "montant": "float", "tva": "float", "lignes": [{"description": "str", "quantite": "int", "prix": "float"}]}
```

---

### 3 -- Synthese de corpus

```
async def synthesize_corpus(documents: list) -> str:
    # Etape 1 : resume de chaque document (Haiku, parallele)
    summaries = await asyncio.gather(*[
        summarize_doc(doc, model="claude-haiku-3-5-20241022")
        for doc in documents
    ])

    # Etape 2 : synthese globale (Sonnet)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Synthetise ces resumes en un rapport coherent. Identifie les themes communs, les contradictions, et les conclusions.",
        messages=[{"role": "user", "content": "\n---\n".join(summaries)}]
    )
    return response.content[0].text

## UTILISATION
- Synthese de veille technologique (10+ articles)
- Resume de documentation (multiple fichiers)
- Analyse de logs multi-sources
```

---

### 4 -- Question-answering sur documentation

```
class DocQA:
    def __init__(self, docs_path: str):
        self.client = anthropic.Anthropic()
        self.docs = self._load_docs(docs_path)
        self.system = f"Tu es un assistant qui repond aux questions en se basant sur cette documentation :\n{self.docs}"

    def ask(self, question: str) -> str:
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            system=[{
                "type": "text",
                "text": self.system,
                "cache_control": {"type": "ephemeral"}
            }],
            messages=[{"role": "user", "content": question}]
        )
        return response.content[0].text

## PROMPT CACHING
La documentation est cachee au premier appel.
Les questions suivantes ne payent que les tokens de la question.
Reduction de cout de 90% a partir de la 2eme question.
```

---

### 5 -- Comparaison de documents

```
def compare_documents(doc_a: str, doc_b: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Compare ces deux documents. JSON: {similarities: [], differences: [], doc_a_only: [], doc_b_only: [], recommendation: str}",
        messages=[{"role": "user", "content": f"Document A:\n{doc_a}\n\nDocument B:\n{doc_b}"}]
    )
    return json.loads(response.content[0].text)

## CAS D'USAGE
- Comparer deux versions d'un contrat
- Comparer deux configurations
- Comparer deux approches techniques documentees
```

---

## Exemples d'utilisation

### Exemple : RAG
**Code** : `answer = rag_query("Comment configurer le monitoring GPU ?", knowledge_base)`

**Resultat attendu** : Reponse basee sur la documentation locale, avec references aux chunks source.

---

## Effet sur le modele
- Le prompt caching est essentiel pour le RAG (documentation cachee)
- Haiku pour l'extraction et les resumes (volume, cout), Sonnet pour la synthese
- Les schemas JSON contraignent la sortie pour une extraction fiable
- Le RAG evite les hallucinations en ancrant les reponses dans les sources
