# Jarvis Core - Prompts de Taches

## Sommaire

1. [Planification multi-outils](#1-planification-multi-outils)
2. [Securite et validation avant action](#2-securite-et-validation-avant-action)
3. [Conception flux multi-modeles](#3-conception-flux-multi-modeles)
4. [Prompt router (reformulation)](#4-prompt-router-reformulation)
5. [Plan d'action cross-outils](#5-plan-daction-cross-outils)
6. [Optimisation radicale OS](#6-optimisation-radicale-os)
7. [Gestion thermique et power GPU](#7-gestion-thermique-et-power-gpu)

---

### 1. Planification multi-outils

**Contexte** : Decomposer un objectif en sous-taches par outil
**Attente** : JSON structure, prompt par outil, strategie d'agregation
**Quand** : Tache complexe multi-domaines

```text
Tu es Jarvis, orchestrateur.
Tache utilisateur : "<objectif>".
Outils disponibles : [Claude Code, Gemini CLI, Codex, Perplexity, BrowserOS].

1) Reformule l'objectif.
2) Decompose-le en sous-taches.
3) Attribue chaque sous-tache a l'outil le plus adapte (avec justification).
4) Propose les prompts a envoyer a chaque outil (un bloc par outil).
5) Indique comment recoller les resultats pour me fournir une reponse finale.

Reponse en JSON pseudo-structurel :
{
  "goal": "...",
  "steps": [
    { "tool": "Perplexity", "purpose": "...", "prompt": "..." },
    { "tool": "Claude Code", "purpose": "...", "prompt": "..." }
  ],
  "final_aggregation_strategy": "..."
}
```

---

### 2. Securite et validation avant action

**Contexte** : Valider la securite de chaque action avant execution
**Attente** : Classification Safe/Risky/Dangerous, rollback
**Quand** : Toujours (pre-execution)

```text
Tu es Jarvis, agent responsable.
Pour chaque commande shell ou action systeme que tu proposes :

1) Classe-la en "Safe" / "Risky" / "Dangerous".
2) Explique pourquoi.
3) Propose, si possible, une alternative plus sure (dry-run, read-only).

Reponds toujours en listant les actions sous forme :
- [Niveau] Commande / Action
  - Justification
  - Rollback (si applicable)
```

---

### 3. Conception flux multi-modeles

**Contexte** : Concevoir l'architecture d'un workflow multi-LLM
**Attente** : Composants, flux, schema JSON, choix de modele
**Quand** : Nouveau workflow Jarvis, integration LLM

```text
Tu es architecte d'agent IA (Jarvis).
Je veux orchestrer plusieurs LLM (Perplexity, Claude, Gemini, OpenAI) pour ce but :
"<decris ton objectif>".

1) Propose une architecture de haut niveau (composants, flux, stockage d'etat).
2) Dis quel modele tu utiliserais pour chaque sous-tache, et pourquoi.
3) Propose un schema de messages/API JSON entre Jarvis et chaque modele.
```

---

### 4. Prompt router (reformulation)

**Contexte** : Transformer une demande utilisateur en prompt optimise pour un outil cible
**Attente** : Prompt reformule avec role/contexte/tache/contraintes/format
**Quand** : Routing intelligent, delegation

```text
Tu es un "prompt router" pour Jarvis.
A partir de ma demande utilisateur :

1) Reformule-la comme un prompt optimise pour l'outil cible : <Claude / Gemini / Perplexity / OpenAI>.
2) Ajoute : role, contexte, tache, contraintes, format de sortie.
3) Donne la version finale prete a envoyer, dans un bloc de texte unique.
```

---

### 5. Plan d'action cross-outils

**Contexte** : Organiser une tache complexe sur plusieurs outils
**Attente** : Tableau etape/tache/outil/entree/sortie
**Quand** : Projets multi-domaines, coordination

```text
Tu es chef d'orchestre pour mes outils IA (Claude Code, Gemini, Codex, Perplexity, BrowserOS).
Objectif : "<decris l'objectif>".

1) Decompose l'objectif en taches elementaires.
2) Pour chaque tache, indique quel outil est le plus adapte et pourquoi.
3) Propose la sequence d'appels outilles (ordre, inputs/outputs).

Format : tableau Markdown avec colonnes [Etape, Tache, Outil, Entree, Sortie attendue].
```

---

### 6. Optimisation radicale OS

**Contexte** : Transformer Linux en bete de course pour workloads IA
**Attente** : Kernel tuning, mitigations, Nice -20, IPC +15%
**Quand** : Tuning performance avance, mode YOLO

```text
Act en tant qu'Architecte Systeme Senior & Expert Kernel Linux.
MISSION : Optimisation RADICALE de JARVIS-OS.

Contexte :
- CPU : Ryzen 7 5700X3D
- RAM : 46GB + ZRAM 12GB (zstd)
- GPU : 5 GPUs (RTX 2060 12GB, 3x GTX 1660S 6GB, RTX 3080 10GB)
- OS : Ubuntu/Debian Linux

Objectifs :
1) Kernel tuning : governor performance, IRQ affinity, scheduleur BORE/EEVDF
2) Memory : swappiness=5, dirty_ratio=40, THP=madvise, overcommit=1
3) I/O : mq-deadline ou none pour NVMe, noatime, discard
4) Network : BBR, tcp_fastopen=3, buffers max
5) Services : Nice -20 pour jarvis-*, desactiver services inutiles
6) GPU : persistence mode, power limit max, fan curve aggressive

Pour chaque modification :
- Commande exacte
- Fichier de config
- Rollback
- Risque (low/medium/high)
- Impact attendu

ATTENTION : produire les deux variantes :
- "Safe baseline" (risque faible, gain modere)
- "Aggressive YOLO" (risque moyen-haut, gain maximal)
```

---

### 7. Gestion thermique et power GPU

**Contexte** : Maximiser le compute sans cramer le hardware
**Attente** : Monitoring, alertes, power limits, fan curves
**Quand** : Jobs longs GPU, inference, training

```text
Tu es Jarvis, expert gestion thermique GPU.

Contexte cluster :
- RTX 2060 12GB, 3x GTX 1660S 6GB, RTX 3080 10GB
- Jobs IA longs (inference, whisper, LLM local)

Taches :
1) Script de monitoring thermique (nvidia-smi polling, seuils)
2) Alertes : 75C warning, 85C emergency kill
3) Power limits optimaux par GPU (equilibre perf/thermique)
4) Fan curve agressive si possible (nvidia-settings ou coolbits)
5) Rotation des jobs entre GPUs pour eviter la surchauffe

Output : script complet + unit systemd + commandes de verification
```
