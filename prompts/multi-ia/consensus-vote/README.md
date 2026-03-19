# Multi-IA — Consensus Vote

> Généré par M1 cluster (gpt-oss-20b)

# Guide du Consensus Multi‑IA  
*(pour cinq modèles : Qwen 3, DeepSeek‑R1, GPT‑OSS, Gemini, Claude)*  

## 1. Pourquoi un consensus multi‑IA ?
- **Robustesse** : les erreurs d’un modèle sont compensées par d’autres.  
- **Diversité de perspective** : chaque architecture a ses forces (langage, logique, créativité).  
- **Fiabilité métier** : on obtient une réponse plus fiable que celle d’un seul modèle.

## 2. Architecture générale

```
+--------------------+
|  Prompt & Context  |
+--------+-----------+
         | 
+--------v-----------+      +------------+
|  Qwen 3 (0.20)     |<-----|  GPT‑OSS   |
+--------+-----------+      +------------+
         |                        ^
+--------v-----------+      +------------+
|  DeepSeek‑R1(0.15) |<---->|  Gemini    |
+--------+-----------+      +------------+
         |                        ^
+--------v-----------+      +------------+
|  Claude (0.30)     |------>|
+--------------------+

```

- **Poids** : chaque modèle reçoit un poids (ex : Claude = 0.30).  
- **Seuil de confiance** : 0,7 → si la moyenne pondérée ≥ 0,7, on accepte le résultat.  
- **Processus** :
  1. Envoyer le même prompt à chaque modèle via leurs APIs.  
  2. Récupérer les réponses et leurs scores internes (confidence, relevancy).  
  3. Normaliser les scores entre 0–1 si nécessaire.  
  4. Calculer la moyenne pondérée.  
  5. Si ≥ 0,7 → réponse finale ; sinon, demander un second tour ou escalader.

## 3. Implémentation (Python + LangChain)

```python
from langchain import LLMChain, PromptTemplate
from langchain_community.llms import OpenAI, Gemini, Claude, Qwen, DeepSeek

# --- Configuration des modèles et poids ---
model_configs = [
    {"name": "qwen3",   "instance": Qwen(model_name="Qwen/Qwen-3.5-1.8B"), "weight": 0.20},
    {"name":"deepseek", "instance": DeepSeek(model_name="DeepSeek-ai/deepseek-chat-7b"), "weight": 0.15},
    {"name":"gptoss",   "instance": OpenAI(temperature=0),                     "weight": 0.10},
    {"name":"gemini",   "instance": Gemini(api_key="GEMINI_KEY"),              "weight": 0.25},
    {"name":"claude",   "instance": Claude(temperature=0, model="claude-3-opus"),"weight": 0.30}
]

# --- Prompt à copier ---
prompt_template = """
Contexte : {context}

Question : {question}

Répondez clairement en une seule phrase.
"""

prompt = PromptTemplate(input_variables=["context","question"], template=prompt_template)

def multi_ai_consensus(context, question):
    responses = []
    for cfg in model_configs:
        llm_chain = LLMChain(llm=cfg["instance"], prompt=prompt)
        answer = llm_chain.run({"context": context, "question": question})
        # Supposons que chaque modèle retourne un score de confiance (0–1)
        confidence = getattr(cfg["instance"], "confidence", 0.8)  # fallback
        responses.append((answer, confidence, cfg["weight"]))

    weighted_sum = sum(ans * conf * w for ans, conf, w in responses)
    total_weight = sum(w for _,_,w in responses)

    consensus_score = weighted_sum / total_weight

    if consensus_score >= 0.7:
        # On choisit la réponse avec le plus haut score pondéré
        best_answer = max(responses, key=lambda x: x[1]*x[2])[0]
        return best_answer, consensus_score
    else:
        return "Consensus non atteint. Veuillez reformuler.", consensus_score

# Exemple d’utilisation
ctx  = "Le marché des crypto-monnaies est très volatil."
qnt  = "Quel risque un investisseur doit-il prévoir en achetant du Bitcoin ?"
print(multi_ai_consensus(ctx, qnt))
```

> **Remarque** :  
> - Les APIs réelles retournent souvent une `logprobs` ou un `confidence`.  
> - Si le modèle ne fournit pas de score, utilisez une valeur par défaut (ex : 0.8).  

## 4. Exemples d’applications

### 4.1 Trading
| Étape | Prompt | Résultat attendu |
|-------|--------|------------------|
| 1 | « Analyse le graphique BTC‑USD sur les 30 derniers jours et prédis la tendance du prochain mois. » | Score de confiance = 0,73 → réponse finale : *« Le prix devrait rester stable avec une légère hausse prévue vers la fin du mois suivant. »* |
| 2 | Si score < 0,7, on peut ajouter un filtre supplémentaire (ex : indicateur RSI) et re‑voter. |

### 4.2 Code Review
| Étape | Prompt | Résultat attendu |
|-------|--------|------------------|
| 1 | « Revois ce snippet Python et indique les bugs potentiels, les inefficacités, et propose des améliorations. » | Score = 0,78 → réponse finale : *« Le boucle `for` est inutile; utilisez une compréhension de liste pour optimiser … »* |
| 2 | Si score < 0,7, on peut demander à un modèle spécialisé (ex : GPT‑OSS) plus d’analyse détaillée. |

## 5. Prompts à copier

```text
# Prompt général (context + question)
Contexte : {context}

Question : {question}

Répondez en une phrase concise.
```

```text
# Prompt trading
Analyse le graphique suivant (décrivez les données) et prédis la tendance pour les 30 prochains jours.

Données : {chart_description}
```

```text
# Prompt code review
Revois le code ci‑dessous. Indique les erreurs, inefficacités, et propose des améliorations détaillées.

Code :
{code_snippet}
```

## 6. Bonnes pratiques

1. **Uniformiser les prompts** : chaque modèle doit recevoir exactement la même formulation pour éviter les biais.  
2. **Normalisation des scores** : si certains modèles donnent un score en % (ex : 85 %), convertir en 0–1.  
3. **Gestion des erreurs** : prévoir un fallback (ex : demander à un humain ou ré‑envoyer avec un prompt plus simple).  
