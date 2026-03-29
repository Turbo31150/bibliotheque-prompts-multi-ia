# Perplexity - Prompts de Taches

## Sommaire

1. [Recherche technique + plan implementation](#1-recherche-technique--plan-implementation)
2. [Comparatif decisionnel de technos](#2-comparatif-decisionnel-de-technos)
3. [Audit Linux centre Jarvis](#3-audit-linux-centre-jarvis)
4. [Cadrage de projet](#4-cadrage-de-projet)

---

### 1. Recherche technique + plan implementation

**Contexte** : Besoin de comprendre un sujet technique avant d'implementer
**Attente** : Synthese sourcee, pieges, plan concret
**Quand** : Avant un dev, choix techno, exploration

```text
Agis comme un chercheur + ingenieur.
Sujet : "<sujet technique>".

1) Fais une synthese technique courte (max 10 phrases) avec citations.
2) Liste les pieges/frictions principaux rencontres en pratique.
3) Propose un plan d'implementation concret etape par etape adapte a un projet reel.

Format : "Synthese" -> "Pieges" -> "Plan d'implementation".
```

---

### 2. Comparatif decisionnel de technos

**Contexte** : Choisir entre plusieurs solutions/technologies
**Attente** : Tableau comparatif, cas d'usage, recommandation
**Quand** : Decision d'architecture, choix de stack

```text
Tu es architecte technique.
Compare ces options : <liste>.

1) Fais un tableau avec criteres (maturite, perf, ecosysteme, complexite, cout, lock-in).
2) Explique en quelques phrases dans quels cas choisir chaque option.
3) Termine par une recommandation pour mon contexte : <decris ton contexte>.
```

---

### 3. Audit Linux centre Jarvis

**Contexte** : Verifier qu'une machine Linux est prete pour Jarvis
**Attente** : Commandes d'audit, analyse structuree, plan d'action
**Quand** : Avant installation Jarvis, apres changement systeme

```text
Tu es un ingenieur Linux senior charge de preparer une machine pour heberger mon orchestrateur Jarvis (assistant IA multi-modeles).

Contexte :
- Distro et version : <indiquer>
- Type : <bare metal / VM / WSL / container>
- Ressources : <CPU, RAM, disques, GPU>
- Usage prevu de Jarvis : <ops, dev, desktop assistant, cluster IA, etc.>

Tache :
1) Realiser un AUDIT de l'OS Linux sous l'angle :
   - demarrage et services (systemd)
   - reseau et securite
   - stack IA / GPU
   - outils de dev et d'automatisation
   - logs, monitoring, observabilite
   - comptes, permissions, sudo
2) Identifier ce qui manque ou ce qui doit etre ajuste pour que Jarvis fonctionne de facon fiable et securisee.
3) Proposer un PLAN D'ACTION priorise (baseline -> avance).

Contraintes :
- Tu dois me donner la liste des commandes a executer pour chaque point d'audit, et ce qu'il faut regarder dans la sortie.
- Ne propose aucune commande destructive.
- Mets bien en evidence ce qui releve :
  - du "must have" (indispensable)
  - du "nice to have" (optionnel)
  - du "risque / a manipuler avec precaution".

Format de sortie :
## Synthese rapide
## Commandes d'audit a executer
## Analyse des resultats attendus
## Plan d'action Jarvis-ready (par etapes)
```

---

### 4. Cadrage de projet

**Contexte** : Demarrer un nouveau projet ou feature
**Attente** : Questions de cadrage, objectif SMART, backlog
**Quand** : Kickoff, nouveau sprint, nouvelle idee

```text
Tu es chef de projet technique.
Pour ce projet : "<description rapide>".

1) Clarifie les objectifs, non-objectifs, et les contraintes en posant 3-7 questions.
2) A partir des reponses, construis :
   - un objectif SMART
   - une liste de livrables
   - un decoupage en iterations (1-2 semaines) avec priorites.
3) Propose un premier backlog synthetique (liste de taches).
```
