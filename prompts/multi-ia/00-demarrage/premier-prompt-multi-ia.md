# Premiers prompts Multi-IA — Prêts à copier

6 scénarios pour les usages les plus fréquents.

---

## 1 — Décision technique

Envoyer à : Claude + ChatGPT + deepseek-r1

```
Contexte : [DÉCRIS TON PROJET EN 2 LIGNES]
Question : [TA QUESTION]

Réponds en 3 points :
1. Recommandation principale
2. Conditions où elle tient
3. Alternative si conditions non réunies

Niveau de confiance : /10
```

Interprétation : convergence 3 IA = haute confiance. Divergence = lire les deux raisonnements.

---

## 2 — Code review multi-perspectif

Envoyer à : Claude (sécurité) + ChatGPT (lisibilité) + Gemini CLI (performance)

```
Revois ce code :
[COLLER LE CODE]

- Score qualité /10
- 3 problèmes principaux (CRITICAL / HIGH / MEDIUM)
- Amélioration prioritaire concrète
```

Règle : bug mentionné par 2 IA sur 3 = corriger immédiatement.

---

## 3 — Diagnostic de bug

Envoyer à : Claude + Perplexity

```
Bug : [COMPORTEMENT OBSERVÉ]
Erreur : [MESSAGE EXACT]
Contexte : [LANGAGE, VERSION, USAGE]

1. Hypothèse principale
2. Test pour la vérifier
3. Correctif si confirmé
```

Priorité : solution avec source Perplexity en premier.

---

## 4 — Choix d'architecture

Envoyer à : Claude + ChatGPT + deepseek-r1

```
Contexte : [DÉCRIRE]
Choix : [OPTION A] vs [OPTION B]

Critères (par ordre) :
1. [Performance]
2. [Maintenabilité]
3. [Coût]

Note chaque option /10 sur chaque critère.
Recommandation finale en une phrase.
```

Synthèse : tableau de scores → choisir l'option avec le meilleur score moyen.

---

## 5 — Recherche technique vérifiée

Envoyer à : Perplexity (prioritaire) + Claude (synthèse)

```
Recherche : [TA QUESTION TECHNIQUE]

Je veux :
- Informations à jour (2025-2026)
- Sources vérifiables
- Pièges ou limitations connues
- Exemple concret d'utilisation
```

Ne pas utiliser Claude seul pour les questions avec dates ou versions.

---

## 6 — Génération + validation de configuration

Workflow 4 étapes :

**Étape 1 — Claude Code (génération)**
```
Génère la configuration [TYPE] pour [SERVICE] :
- Version : [VERSION]
- Environnement : [DEV/PROD/LOCAL]
- Contraintes : [SÉCURITÉ/PERF/SIMPLICITÉ]
Commente les options importantes.
```

**Étape 2 — ChatGPT (revue sécurité)**
```
Revois cette configuration pour la sécurité :
- Credentials en dur ?
- Permissions trop larges ?
- Options dangereuses activées ?
```

**Étape 3 — Perplexity (validation)**
Ces options sont-elles valides pour [SERVICE] version [VERSION] ?

**Étape 4 — Gemini CLI**
Applique et teste la configuration.

---

## Commande cluster JARVIS

```bash
curl -X POST http://127.0.0.1:8000/api/consensus \\
  -H "Content-Type: application/json" \\
  -d '{"question": "[TA QUESTION]", "models": ["claude", "qwen3", "deepseek-r1"]}'
```

Via Claude Code :
```
/consensus "[TA QUESTION]"
```

---

*Étape suivante : [choisir-son-modele.md](choisir-son-modele.md)*
