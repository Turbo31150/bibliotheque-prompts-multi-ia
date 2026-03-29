# Claude API -- Web & Social

## Description

Prompts et patterns pour utiliser l'API Claude dans l'automatisation de contenu web et social : generation de posts, analyse de sentiment, moderation et personnalisation de contenu.

## Cas d'usage
- Generation automatisee de contenu multi-plateforme
- Analyse de sentiment sur des commentaires/mentions
- Moderation automatique de contenu
- Personnalisation de newsletters
- Adaptation de contenu par audience

---

## Prompts prets a copier

### 1 -- Generateur de contenu multi-plateforme

```
def generate_content(topic: str, platforms: list) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Tu es un expert en content marketing. Genere du contenu adapte a chaque plateforme. JSON avec une cle par plateforme.",
        messages=[{"role": "user", "content": f"Sujet: {topic}\nPlateformes: {', '.join(platforms)}\nGenere le contenu adapte a chaque plateforme."}]
    )
    return json.loads(response.content[0].text)

## UTILISATION
posts = generate_content(
    "Les avantages du self-hosting",
    ["twitter", "linkedin", "reddit", "blog"]
)
# → {"twitter": "Thread de 5 tweets...", "linkedin": "Post pro...", ...}
```

---

### 2 -- Analyseur de sentiment

```
def analyze_sentiment(comments: list) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Analyse le sentiment de chaque commentaire. JSON: [{text, sentiment: positive/negative/neutral, score: -1 to 1, topics: []}]",
        messages=[{"role": "user", "content": json.dumps(comments)}]
    )
    return json.loads(response.content[0].text)

## UTILISATION
- Analyser les commentaires sur un post
- Tracker le sentiment au fil du temps
- Detecter les sujets sensibles
- Alerter si pic de negativite
```

---

### 3 -- Moderateur automatique

```
def moderate(content: str) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Moderateur de contenu. Evalue: {approved: bool, reason: str, flags: [spam/toxic/off-topic/nsfw], confidence: 0-1}",
        messages=[{"role": "user", "content": content}]
    )
    return json.loads(response.content[0].text)

## PIPELINE
1. Nouveau commentaire → moderate()
2. Si approved et confidence > 0.9 → publier
3. Si !approved et confidence > 0.9 → rejeter
4. Sinon → file de moderation humaine
```

---

### 4 -- Personnalisation de newsletter

```
def personalize_newsletter(template: str, user_profile: dict) -> str:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Adapte cette newsletter au profil utilisateur. Garde la structure, adapte le ton et les exemples.",
        messages=[{"role": "user", "content": f"Profil: {json.dumps(user_profile)}\nNewsletter:\n{template}"}]
    )
    return response.content[0].text

## SEGMENTS
- Debutant : plus d'explications, moins de jargon
- Expert : plus technique, plus concis
- Manager : focus impact business et KPI
```

---

### 5 -- Adaptateur de contenu multilingue

```
def adapt_content(content: str, target_lang: str, context: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Adapte ce contenu en {target_lang}. Pas une traduction litterale : adapte les references culturelles, les expressions et le ton pour le public {target_lang}. Contexte: {context}",
        messages=[{"role": "user", "content": content}]
    )
    return response.content[0].text

## UTILISATION
- Adapter un post anglais pour LinkedIn France
- Adapter un guide technique pour un public japonais
- Pas juste traduire, mais localiser
```

---

## Exemples d'utilisation

### Exemple : Contenu multi-plateforme
**Code** : `posts = generate_content("Monitoring GPU avec Prometheus", ["twitter", "linkedin"])`

**Resultat attendu** : Thread Twitter technique + post LinkedIn professionnel sur le meme sujet.

---

## Effet sur le modele
- Haiku pour la moderation et le sentiment (volume eleve, cout reduit)
- Sonnet pour la generation de contenu (qualite requise)
- Le prompt caching pour les templates de newsletter (contenu statique cache)
- L'API permet l'automatisation complete du pipeline de contenu
