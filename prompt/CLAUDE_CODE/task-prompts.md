# Claude Code - Prompts de Taches

## Sommaire

1. [Refactoring module](#1-refactoring-module)
2. [Generation de tests](#2-generation-de-tests)
3. [Debug cible](#3-debug-cible)
4. [Optimisation performance code](#4-optimisation-performance-code)
5. [Architecture avant de coder](#5-architecture-avant-de-coder)
6. [Mise en route Jarvis sur Linux](#6-mise-en-route-jarvis-sur-linux)
7. [Audit Linux centre Jarvis](#7-audit-linux-centre-jarvis)
8. [Review globale de repo](#8-review-globale-de-repo)

---

### 1. Refactoring module

**Contexte** : Code existant a nettoyer/ameliorer
**Attente** : Diff incremental, API preservee, tests adaptes
**Quand** : Dette technique, modernisation, lisibilite

```text
[Claude Code - Task: Refactor module]

Tu es Claude Code, configure comme developpeur senior.
Tache : refactorer ce module sans casser l'API publique.

1) Inspecte tous les fichiers lies (imports, usages).
2) Liste les problemes (lisibilite, duplication, perf, securite).
3) Propose un refactor incremental en montrant des diff ou des blocs de code.
4) Ajoute ou adapte les tests si necessaire.

Structure ta reponse avec :
## Goal
## Analysis
## Changes (avec code)
## Tests
## Notes
```

---

### 2. Generation de tests

**Contexte** : Code sans couverture de tests suffisante
**Attente** : Cas limites, tests unitaires/integ, commande de lancement
**Quand** : Apres ecriture de code, avant merge/PR

```text
[Claude Code - Task: Generer des tests]

Tu es ingenieur QA dans ce projet.
Pour les fichiers que je vais te montrer :

1) Explore les fonctions/methodes publiques.
2) Propose une liste de cas de test pertinents (y compris cas limites).
3) Genere les tests dans le framework utilise dans le repo.
4) Indique la commande pour lancer les tests.

Reponse en sections : Goal / Test plan / Test code / Run command.
```

---

### 3. Debug cible

**Contexte** : Bug specifique a diagnostiquer et corriger
**Attente** : Hypotheses, lignes a inspecter, correctif minimal
**Quand** : Incident, regression, comportement inattendu

```text
[Claude Code - Task: Debug cible]

Tu es expert debug.
Voici le code + le bug observe : "<description du bug>".

1) Propose des hypotheses de causes probables (par ordre de vraisemblance).
2) Dis-moi EXACTEMENT quelles lignes / parties inspecter.
3) Propose un correctif minimal avec explication courte.

Ne change pas le style du projet, reste minimal.

Structure : Hypotheses -> Investigation -> Correctif -> Verification
```

---

### 4. Optimisation performance code

**Contexte** : Code lent ou gourmand en ressources
**Attente** : Hotspots identifies, version optimisee, gain estime
**Quand** : Bottleneck detecte, profiling fait

```text
[Claude Code - Task: Optimisation perf]

Agis comme un expert performance dans ce langage.
Pour ce code :

1) Identifie les hotspots potentiels (complexite, allocations, I/O).
2) Propose une version optimisee, en gardant la meme signature publique.
3) Explique le gain attendu et les compromis eventuels.

Format : Problemes -> Nouveau code -> Commentaire perf.
```

---

### 5. Architecture avant de coder

**Contexte** : Nouveau feature ou projet a concevoir
**Attente** : Questions, architecture, plan de livraison
**Quand** : Debut de feature, nouveau module, refonte

```text
[Claude Code - Task: Architecture]

Tu es un architecte logiciel senior.
Prends ce besoin : "<decris ton besoin ou user story>".

1) Pose-moi 3-5 questions ciblees si quelque chose est flou.
2) Propose une architecture technique claire (modules, data flow, techno).
3) Donne un plan de livraison etape par etape (MVP puis ameliorations).

Format : titres Markdown + listes numerotees.
```

---

### 6. Mise en route Jarvis sur Linux

**Contexte** : Deployer Jarvis comme service systeme Linux
**Attente** : systemd units, logging, isolation ressources, documentation
**Quand** : Installation fresh, migration, reconstruction

```text
You are Claude Code configured as a senior Linux SRE and software architect.
Your job is to prepare this Linux system and this codebase to run an orchestrator called "Jarvis" (multi-LLM assistant).

Context:
- Target distro and environment: <Ubuntu/Debian/... + bare metal/VM/WSL>
- Hardware: <CPU/RAM/disks/GPU>
- Repository structure and tech stack: <Python/Node/... + paths>

Objectives:
1) Inspect the repository and existing scripts/configs related to Jarvis.
2) Design and implement:
   - systemd unit files for Jarvis core and workers
   - logging and log rotation
   - basic resource isolation (cgroups / slices if relevant)
3) Generate or update:
   - install/setup scripts for dependencies (Python env, Docker, GPU stack, etc.)
   - configuration files for connecting to external LLMs
4) Produce documentation:
   - how to install Jarvis on a fresh Linux host
   - how to start/stop/restart and check health
   - how to rollback changes

Workflow:
1) Ask me for: Distro, Jarvis code location, runtime type, external LLMs
2) Explore repo: systemd units, scripts, Dockerfiles, env files
3) Propose prioritized plan with risk levels
4) Implement incrementally with rollback steps

Output style:
Goal, Plan, Repository Findings, Config/Code Changes, How to Run, How to Rollback, Next Steps.
```

---

### 7. Audit Linux centre Jarvis

**Contexte** : Verifier si la machine est prete pour Jarvis
**Attente** : Commandes d'audit, analyse, plan d'action
**Quand** : Avant installation, apres changement systeme

```text
Tu es un ingenieur Linux senior charge de preparer une machine pour heberger Jarvis.

Contexte :
- Distro et version : <indiquer>
- Type : <bare metal / VM / WSL / container>
- Ressources : <CPU, RAM, disques, GPU>
- Usage prevu : <ops, dev, desktop assistant, cluster IA>

Tache :
1) Realiser un AUDIT de l'OS Linux :
   - demarrage et services (systemd)
   - reseau et securite
   - stack IA / GPU
   - outils de dev et d'automatisation
   - logs, monitoring, observabilite
   - comptes, permissions, sudo
2) Identifier ce qui manque pour que Jarvis fonctionne.
3) Proposer un PLAN D'ACTION priorise (baseline -> avance).

Contraintes :
- Liste des commandes a executer pour chaque point d'audit
- Aucune commande destructive
- Distinguer "must have" / "nice to have" / "risque"

Format : Synthese / Commandes d'audit / Analyse / Plan d'action
```

---

### 8. Review globale de repo

**Contexte** : Evaluer la sante d'un repo existant
**Attente** : Zones a risque, axes de refactor, roadmap
**Quand** : Prise en main d'un projet, audit periodique

```text
[Claude Code - Task: Review globale]

Tu es reviewer senior.
A partir de la structure de ce repo :

1) Identifie les zones a risque (couplage, dette technique, manque de tests, perf).
2) Propose 3 axes de refactor prioritaire.
3) Donne une roadmap courte (3 a 5 etapes) pour remettre le projet au propre sans tout casser.

Structure : Risques -> Priorites -> Roadmap
```
