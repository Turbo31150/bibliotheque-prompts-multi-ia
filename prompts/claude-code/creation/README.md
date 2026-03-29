# Claude Code — Creation

## Description
Prompts pour la creation de nouvelles fonctionnalites avec Claude Code : brainstorming, planning, implementation. Exploite les superpowers (agents paralleles, consensus multi-modele, skills JARVIS) pour maximiser la qualite et la vitesse de creation.

## Configuration requise
- Claude Code avec plugin `jarvis-turbo` actif
- Cluster IA operationnel pour le consensus et les agents paralleles
- `uv run pytest` pour la validation automatique
- CLAUDE.md dans le projet avec les conventions

---

## Prompts par type de tache

### Creation — Brainstorming structure

```
Je veux creer [FONCTIONNALITE].

## BRAINSTORM
1. Genere 5 approches differentes pour implementer cette fonctionnalite
2. Pour chaque approche :
   - Nom court
   - Description en 2 lignes
   - Avantages (2-3 points)
   - Inconvenients (2-3 points)
   - Complexite : S/M/L/XL
   - Temps estime

3. Classe les approches par ratio valeur/effort
4. Recommande la meilleure avec justification

## CONTRAINTES
- Stack : Python 3.13 + uv + async/await
- Integration : doit s'integrer avec le MCP existant (658 handlers)
- Performance : < 2s de latence
- Tests : couverture 90%+
```

---

### Creation — Planning d'implementation

```
Cree un plan d'implementation detaille pour [FONCTIONNALITE].

## FORMAT
Pour chaque etape :
- Numero et titre
- Fichiers a creer/modifier
- Dependances (quelles etapes doivent etre terminees avant)
- Estimation (en minutes)
- Critere de validation (comment savoir que c'est termine)

## REGLES
- Etapes de maximum 30 minutes chacune
- Chaque etape produit du code testable
- Les tests sont ecrits AVANT le code (TDD)
- Chaque etape est commitable independamment
- Aucune etape ne casse les tests existants

## LIVRABLE
Tableau recapitulatif :
| # | Etape | Fichiers | Dependances | Temps | Validation |
|---|-------|----------|-------------|-------|------------|
```

---

### Creation — Implementation avec agents paralleles

```
Implemente [FONCTIONNALITE] en utilisant 3 agents paralleles :

Agent 1 — ARCHITECTURE
- Concois les interfaces (classes, fonctions, types)
- Cree les fichiers vides avec les signatures
- Definis le flux de donnees

Agent 2 — TESTS
- Ecris tous les tests (TDD) base sur les interfaces de l'Agent 1
- Cas nominal, edge cases, erreurs
- Minimum 10 tests

Agent 3 — DOCUMENTATION
- Ecris les docstrings
- Cree le README du module
- Documente les endpoints API si applicable

Une fois les 3 agents termines :
- Implemente le code pour faire passer les tests de l'Agent 2
- Verifie que la documentation de l'Agent 3 correspond
- Lance la suite complete : uv run pytest -v
```

---

### Creation — Nouveau module JARVIS complet

```
Cree un nouveau module JARVIS pour [FONCTIONNALITE].

## Architecture JARVIS
- Runtime : Python 3.13 + uv
- Framework : Claude Agent SDK
- MCP : 658 handlers existants dans src/mcp_server.py
- DB : SQLite (63 bases, 160 MB)
- API : FastAPI (670+ endpoints)

## Conventions obligatoires
- from __future__ import annotations en premier import
- Type hints sur toutes les fonctions
- async/await pour tout I/O
- Logging via logging module (pas print)
- snake_case pour Python
- Docstrings en francais
- Tests dans tests/test_[module].py

## Structure du module
Genere :
1. src/[module].py — Code principal
2. tests/test_[module].py — Tests (min 5 cas)
3. Integration MCP : handlers a ajouter dans mcp_server.py
4. Integration API : endpoints a ajouter
5. Documentation : docstring du module

## Contraintes
- Ne pas modifier les fichiers critiques directement
- Utiliser le pool httpx partage de src/tools.py
- Respecter le rate limiting de src/rate_limiter.py
- Exporter les metriques via src/metrics_exporter.py
```

---

### Amelioration / Refactoring — Etendre une fonctionnalite existante

```
Etends la fonctionnalite [EXISTANTE] avec [NOUVELLE_CAPACITE].

## PROCESSUS
1. AUDIT de l'existant :
   - Lis le code actuel
   - Identifie les points d'extension (hooks, plugins, callbacks)
   - Verifie la couverture de tests actuelle

2. DESIGN de l'extension :
   - Propose l'interface de la nouvelle capacite
   - Montre comment elle s'integre sans modifier le code existant (Open/Closed)
   - Identifie les risques de regression

3. IMPLEMENTATION :
   - Ecris les tests d'abord (TDD)
   - Implemente le minimum pour faire passer les tests
   - Verifie zero regression

4. VALIDATION :
   - Tests de la nouvelle capacite : vert
   - Tests existants : vert
   - Benchmark si applicable
```

---

### Debug — Prototype qui ne fonctionne pas

```
Mon prototype pour [FONCTIONNALITE] ne fonctionne pas.

Code actuel : [CHEMIN_OU_COLLER]
Comportement attendu : [DESCRIPTION]
Comportement observe : [DESCRIPTION]

## PROCESSUS
1. Identifie ce qui manque pour que ca fonctionne
2. Classe les problemes : conceptuel vs implementation vs configuration
3. Corrige dans l'ordre de criticite
4. Ajoute les tests manquants
5. Verifie le fonctionnement complet
```

---

### Documentation — Specification technique

```
Ecris la specification technique pour [FONCTIONNALITE] avant implementation.

## FORMAT
### 1. Objectif
[1-2 phrases]

### 2. Contexte
[Pourquoi cette fonctionnalite est necessaire]

### 3. Architecture
[Diagramme ASCII + description des composants]

### 4. API
[Endpoints, parametres, reponses]

### 5. Modele de donnees
[Tables, colonnes, relations]

### 6. Flux
[Sequence d'operations step by step]

### 7. Tests
[Scenarios de test prevus]

### 8. Risques
[Points d'attention, dependances, limites]
```

---

## Exemples concrets

### Exemple 1 : Brainstorming pour un health check aggrege

```
Je veux creer un module health_aggregator.py qui collecte le status
de 8 composants (cluster, GPU, trading, RAG, voice, BrowserOS, Canvas, n8n)
en parallele avec asyncio, et expose un endpoint /health/full.
```

**Resultat attendu** :
- 5 approches (asyncio.gather, thread pool, polling cache, event-driven, healthcheck lib)
- Recommandation : asyncio.gather + cache TTL (meilleur ratio valeur/effort)
- Plan d'implementation en 4 etapes de 15-20 min chacune

### Exemple 2 : Creation avec agents paralleles

```
Implemente un systeme de notifications multi-canal (Telegram, Discord, email)
en utilisant 3 agents paralleles.
```

**Resultat attendu** :
- Agent 1 : Interface NotificationChannel avec send(), format(), validate()
- Agent 2 : 15 tests couvrant tous les canaux et cas d'erreur
- Agent 3 : Documentation complete avec exemples d'usage

---

## Effet sur le modele
- Le brainstorming en 5 approches force une exploration large avant de converger
- Le planning en etapes de 30 min max decoupe les problemes complexes
- Les agents paralleles divisent le temps par 3 pour les taches independantes
- Les conventions JARVIS explicites evitent les corrections post-generation
- Le TDD integre dans chaque prompt garantit du code testable des le depart
- La specification technique avant implementation reduit les allers-retours de 50-70%
