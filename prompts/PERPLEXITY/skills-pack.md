# Perplexity Skills Pack — Integration JARVIS

> Derniere mise a jour : 2026-03-28
> Role : recherche web, verification de sources, monitoring de dependances

---

## Skills Recherche

### 1. retrieval-web

**Description** : Recuperation de contenu web, recherche de documentation, veille technologique.

| Capacite | Detail |
|----------|--------|
| Recherche web | Requetes en langage naturel, synthese de resultats |
| Lookup documentation | Recherche dans docs officielles (NVIDIA, CUDA, Python, Node, systemd) |
| Veille techno | Monitoring de nouvelles versions, breaking changes, CVEs |
| Fact-checking | Verification de donnees techniques contre sources web |

**Exemples d'usage :**
```
- "Quelle est la derniere version de CUDA compatible avec le driver 550 ?"
- "Quels sont les known issues de llama.cpp v0.4.x ?"
- "Comparatif Piper TTS vs Coqui TTS performance 2026"
```

### 2. github-reader

**Description** : Lecture de repositories GitHub, monitoring de dependances, changelogs.

| Capacite | Detail |
|----------|--------|
| Dependency updates | Suivre les mises a jour de packages critiques |
| Changelog monitoring | Lire les CHANGELOG.md et release notes |
| Issue tracking | Verifier si un bug connu existe deja |
| Code search | Chercher des patterns dans des repos publics |

**Exemples d'usage :**
```
- "Y a-t-il une issue ouverte sur llama-cpp-python pour le bug CUDA 12.4 ?"
- "Quoi de neuf dans la derniere release de faster-whisper ?"
- "Quel est le pattern recommande pour fastapi + websockets en 2026 ?"
```

---

## Patterns de Documentation

Perplexity excelle pour rechercher de la documentation technique specifique :

| Domaine | Type de recherche | Exemple |
|---------|-------------------|---------|
| NVIDIA | Compatibilite driver/CUDA, erreurs Xid, configuration multi-GPU | "NVIDIA Xid error 79 fix linux" |
| CUDA | Versions compatibles, installation, troubleshooting | "CUDA 12.4 ubuntu 24.04 installation guide" |
| llama.cpp | Build options, quantization, performance | "llama.cpp GGUF Q4_K_M vs Q5_K_M benchmark" |
| systemd | Unit files, timers, resource control | "systemd MemoryMax cgroup v2 configuration" |
| Python | Packages, async patterns, debugging | "asyncio task group exception handling python 3.12" |
| Linux | Kernel, networking, filesystem | "ext4 journal recovery linux 6.8" |

---

## Integration dans JARVIS

### Via Comet MCP

Perplexity est accessible via le serveur MCP Comet :

```
Outil : mcp__comet__comet_ask
Mode : recherche web avec synthese
```

Le flux typique :
1. JARVIS detecte un besoin de recherche (question sans reponse locale)
2. Requete envoyee via Comet MCP a Perplexity
3. Reponse avec sources integree dans le contexte
4. Validation par consensus si necessaire

### Via Perplexity API

```python
import requests

response = requests.post(
    "https://api.perplexity.ai/chat/completions",
    headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}"},
    json={
        "model": "sonar",
        "messages": [{"role": "user", "content": query}]
    }
)
```

---

## 4 Prompts de Taches

Extrait de `PERPLEXITY/task-prompts.md` :

### 1. Recherche technique + plan implementation
Comprendre un sujet technique avant d'implementer. Synthese sourcee, pieges, plan concret.

### 2. Comparatif decisionnel de technos
Choisir entre plusieurs solutions/technologies. Tableau comparatif, cas d'usage, recommandation.

### 3. Audit Linux centre Jarvis
Verifier qu'une machine Linux est prete pour Jarvis. Commandes d'audit, analyse structuree, plan d'action.

### 4. Cadrage de projet
Demarrer un nouveau projet ou feature. Questions de cadrage, objectif SMART, backlog.

> Voir `PERPLEXITY/task-prompts.md` pour les prompts complets.

---

## Role dans le Consensus

Perplexity fournit des **donnees de verification web** au protocole de consensus :

| Aspect | Detail |
|--------|--------|
| Type de contribution | Verification factuelle, donnees sourcees |
| Mode | Fournisseur de donnees (pas votant direct) |
| Declencheur | Question factuelle, besoin de source externe |
| Confiance | Elevee sur les faits verifiables, faible sur les opinions |
| Integration | Les reponses Perplexity alimentent le contexte des votants |

Quand le consensus est MOYEN ou FAIBLE, Perplexity peut etre sollicite pour apporter des sources web qui aident a trancher.

---

## Limites

- Perplexity **ne genere pas** de code executable
- Perplexity **ne modifie pas** de fichiers locaux
- Perplexity **depend** d'une connexion internet active
- Les reponses peuvent etre obsoletes (delai indexation web)
- Son role est **informationnel** : recherche, verification, documentation
