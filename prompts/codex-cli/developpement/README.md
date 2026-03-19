# Codex CLI — Developpement

## Description
Prompts de generation de code avec Codex CLI : creation de modules, refactoring, integration JARVIS et generation de scripts Linux. Codex excelle dans le code terminal, l'infra et les scripts shell.

## Configuration requise
- Codex CLI installe et configure
- Cle API OpenAI (`OPENAI_API_KEY`)
- Projet accessible dans le repertoire courant
- Tests existants (`uv run pytest` ou `pytest`)

---

## Prompts par type de tache

### Creation — Generation de code

```
Tu es un expert Codex CLI.
Objectif : generer du code pour [TACHE].
1) Respecte le style du projet existant.
2) Fournis le code complet, pas du pseudo-code.
3) Ajoute un exemple d'usage minimal.
4) Commente seulement les parties critiques.
5) Si le contexte manque, lis les fichiers lies avant de coder.
Structure : Goal/Plan/Code/Verify.
```

---

### Creation — Nouveau module JARVIS

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

### Creation — Script d'infrastructure

```
Tu es Codex CLI, expert Linux/SRE pour Jarvis.
1) Inspecte d'abord les services systemd, Docker Compose, endpoints, MCP et workflows n8n.
2) Identifie les ecarts entre config declaree et runtime reel.
3) Corrige par petites etapes verifiables.
4) Pour chaque changement, donne rollback et commande de verification.
5) N'ignore pas les contrats d'API, ports, permissions et dependances.
Structure : Goal/Plan/Code/Verify.
```

---

### Amelioration / Refactoring — Refactoring incremental

```
[Codex CLI - Refactor]
Tu es un dev senior.
Tache : refactorer ce module sans casser l'API publique.
1) Inspecte les fichiers lies avant de toucher au code.
2) Liste les problemes concrets.
3) Propose un diff incremental minimal.
4) Preserve signatures, formats I/O, comportements observables et integrations existantes.
5) Ajoute ou ajuste les tests necessaires.
Structure : Goal/Analysis/Changes/Tests.
```

---

### Amelioration / Refactoring — Refactoring Python avance

```
Analyse et refactore le fichier [CHEMIN_DU_FICHIER].

## Etape 1 — Diagnostic
- Compte les lignes par fonction (flag si > 40 lignes)
- Identifie le code duplique (DRY violations)
- Repere les anti-patterns Python :
  - Mutable default arguments
  - Bare except clauses
  - Global state
  - Nested loops > 2 niveaux
  - String concatenation dans des boucles

## Etape 2 — Plan de refactoring
Pour chaque probleme identifie :
- Severite : CRITICAL / HIGH / MEDIUM / LOW
- Effort : S (< 5 min) / M (5-15 min) / L (15-30 min)
- Impact : Performance / Lisibilite / Maintenabilite / Securite

## Etape 3 — Execution
Applique les changements par ordre de severite decroissante.
Pour chaque changement :
- Montre le before/after
- Explique pourquoi
- Confirme que la signature publique n'a pas change

## Etape 4 — Verification
- Lance les tests existants
- Confirme zero regression
- Mesure le gain (lignes supprimees, complexite reduite)
```

---

### Creation — Commande vocale JARVIS

```
Ajoute une commande vocale JARVIS pour [ACTION].

## Systeme vocal JARVIS
- STT : Whisper (transcription)
- NLU : Classification par le cluster IA
- TTS : Piper (synthese vocale)
- Commandes existantes : 898
- Modules : 5 (systeme, media, domotique, trading, dev)

## Nouvelle commande
- Declencheur vocal : "[PHRASE_DECLENCHEUR]"
- Aliases : [LISTE_ALIASES]
- Module : [systeme/media/domotique/trading/dev]
- Action : [DESCRIPTION DE L'ACTION]
- Reponse vocale : "[TEXTE_A_PRONONCER]"

## Implementation
1. Ajouter dans src/commands.py (pattern matching)
2. Ajouter le handler dans le module concerne
3. Ajouter le test dans tests/test_commands.py
4. Mettre a jour la documentation des commandes
```

---

### Documentation — Memoire projet et continuite

```
Memoire du projet : <stack, decisions, contraintes, chemins, services>.
Tache actuelle : <demande>.
1) Relie la tache au contexte precedent.
2) Rappelle les contraintes a ne pas casser.
3) Reutilise l'existant avant de proposer du neuf.
4) Signale les ecarts ou contradictions.
5) Propose l'implementation coherente la plus incrementale possible.
Structure : Goal/Plan/Code/Verify.
```

---

## Exemples concrets

### Exemple 1 : Generer un module
```bash
codex "Cree un module disk_monitor.py qui surveille l'espace disque et alerte quand > 80%"
```

**Resultat attendu** : Module complet avec check des partitions, seuils configurables, alerte Telegram, tests.

### Exemple 2 : Refactorer un fichier
```bash
codex "Refactore src/mcp_server.py (6282 lignes). Decoupe en sous-modules < 500 lignes. Garde l'API identique."
```

**Resultat attendu** : Plan de decoupage, creation de sous-modules, mise a jour des imports, tests passent.

### Exemple 3 : Script infra
```bash
codex "Cree un service systemd pour JARVIS avec restart auto, health check et log rotation"
```

**Resultat attendu** : Fichier .service, commandes d'installation, logrotate config, verification.

---

## Effet sur le modele
- Codex est optimise pour le code et les commandes terminal — plus precis que les modeles generalistes
- La structure Goal/Plan/Code/Verify force un raisonnement structure
- La structure Goal/Analysis/Changes/Tests est optimale pour le refactoring
- Le mode suggest (defaut) est le plus sur pour le developpement interactif
- Les conventions explicites (type hints, async/await) evitent les corrections post-generation
- La memoire projet evite les reecritures inutiles et maintient la coherence
