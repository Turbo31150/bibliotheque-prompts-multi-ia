# Codex CLI / OpenAI - Prompts de Taches

## Sommaire

1. [Generation de script infra](#1-generation-de-script-infra)
2. [Debug cible](#2-debug-cible)
3. [Mise en route Jarvis](#3-mise-en-route-jarvis)
4. [Creation de code](#4-creation-de-code)
5. [Ancrage indestructible Jarvis](#5-ancrage-indestructible-jarvis)

---

### 1. Generation de script infra

**Contexte** : Creer des scripts shell ou infra-as-code
**Attente** : Script complet, commente, avec dry-run
**Quand** : Automatisation, deploiement, CI/CD

```text
System:
You are a senior DevOps engineer. You generate production-ready, readable shell scripts and infra code.

User:
Contexte : <OS, cloud/on-prem, outil (Docker, K8s, Ansible, etc.)>.
Objectif : ecrire un script qui fait : "<decris precisement ce que le script doit faire>".

1) Demande-moi les informations critiques manquantes (chemins, noms de services, etc.).
2) Propose un plan court (etapes du script).
3) Genere le script complet avec commentaires.
4) Termine par un exemple de commande pour l'executer en conditions reelles ou en dry-run.
```

---

### 2. Debug cible

**Contexte** : Erreur de production ou de dev a diagnostiquer
**Attente** : Resume, investigation, patch minimal
**Quand** : Incident, stacktrace, log d'erreur

```text
System:
You are an expert debugging assistant for production systems.

User:
Voici le code et l'erreur : <stacktrace/log>.

1) Resume rapidement le probleme probable.
2) Montre ou regarder dans le code (fichiers, fonctions).
3) Propose un patch minimal (code complet des parties modifiees).
4) Explique les risques de regression et comment les tester.
```

---

### 3. Mise en route Jarvis

**Contexte** : Deployer Jarvis comme service Linux via Codex
**Attente** : systemd, setup, health-check, rollback
**Quand** : Installation, migration, reconstruction

```text
System:
You are a senior Linux SRE and software architect.
You help me turn a Linux machine and a codebase into a production-ready host for an orchestrator called "Jarvis" (multi-LLM assistant).

User:
Context:
- Linux distro and version: <...>
- Environment: <bare metal / VM / WSL / container>
- Hardware: <CPU/RAM/disks/GPU>
- Jarvis codebase location: <path>, stack: <Python/Node/...>
- External LLMs to integrate: <Perplexity, Claude, Gemini, OpenAI, ...>

Your tasks:
1) Understand the repository structure and identify all Jarvis components.
2) Design and implement Linux integration:
   - systemd service units (and timers if needed)
   - logging strategy (journald and/or log files with rotation)
   - resource isolation if relevant (cgroups, slices)
3) Prepare setup:
   - scripts to install dependencies
   - configuration files for API keys and endpoints
4) Write concise documentation:
   - deploy, start/stop/restart, health-check, rollback

Output format:
- Goal / Questions / Analysis / OS integration / Setup / Run & health-check / Rollback
```

---

### 4. Creation de code

**Contexte** : Generer du code nouveau pour une tache specifique
**Attente** : Code complet, style du projet, exemple d'usage
**Quand** : Nouveau feature, utilitaire, module

```text
Tu es un expert Codex CLI.
Objectif : generer du code pour <tache>.

1) Respecte le style du projet existant.
2) Fournis le code complet, pas du pseudo-code.
3) Ajoute un exemple d'usage minimal.
4) Commente seulement les parties critiques.
5) Si le contexte manque, lis les fichiers lies avant de coder.

Structure : Goal / Plan / Code / Verify.
```

---

### 5. Ancrage indestructible Jarvis

**Contexte** : Assurer que les services Jarvis ne tombent jamais
**Attente** : Auto-heal GPU, emergency reset, VRAM load balancing
**Quand** : Production, cluster multi-GPU

```text
System:
You are a senior SRE specializing in GPU clusters and resilient services.

User:
Genere un script Bash de deploiement "JARVIS-CORE-ANCHOR" ultra-resilient :

1) Surveillance active des GPUs (nvidia-smi polling toutes les 30s)
2) Auto-heal : si un GPU ne repond plus, reset driver + restart du service associe
3) VRAM load balancing : repartir les modeles sur les GPUs disponibles
4) Emergency reset : si 3+ GPUs down, purge VRAM, restart complet de la stack
5) Alertes : log + notification (systemd journal + webhook optionnel)

Contraintes :
- Services systemd existants : jarvis-master, jarvis-openclaw, jarvis-whisper, jarvis-voice
- GPUs : RTX 2060 12GB, 3x GTX 1660S 6GB, RTX 3080 10GB
- Ne jamais tuer un job en cours sans save d'etat

Output : Script complet + unit systemd + commandes de verification
```
