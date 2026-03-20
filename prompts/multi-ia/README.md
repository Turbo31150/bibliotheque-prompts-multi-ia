# Multi-IA — Guide de démarrage et navigation

Orchestrer plusieurs modèles IA ensemble pour des résultats plus fiables qu'un seul modèle.

---

## 🚀 Par où commencer ?

| Étape | Dossier | Ce que tu fais |
|-------|---------|----------------|
| **1** | [`00-demarrage/`](00-demarrage/) | Teste ton premier prompt multi-IA en 5 minutes |
| **2** | [`01-core/`](01-core/) | Comprends le consensus et le dispatch intelligent |
| **3** | [`02-configuration/`](configuration/) | Configure ton cluster ou tes APIs |
| **4** | Selon ton besoin | Dev, debug, automatisation, trading… |

---

## 🤖 Les modèles et leurs rôles

| Modèle | Rôle principal | Vitesse | Quand l'utiliser |
|--------|---------------|---------|-----------------|
| **Claude** | Analyse, architecture, rédaction | — | Tâches complexes, raisonnement |
| **qwen3-8b** | Code rapide, tâches simples | 65 tok/s | Rapidité, première passe |
| **deepseek-r1** | Raisonnement, chain-of-thought | 40 tok/s | Problèmes complexes, logique |
| **gpt-oss:120b** | Analyse longue, précision | 51 tok/s | Contexte long, synthèse |
| **ChatGPT** | Documentation, lisibilité | — | Rédaction, explication |
| **Gemini CLI** | Exécution système, tests | — | Validation, commandes shell |
| **Perplexity** | Recherche, veille technique | — | Sources vérifiées, actualité |

---

## 📂 Structure du dossier

```
multi-ia/
├── 00-demarrage/          ← COMMENCER ICI — premier contact
├── 01-core/               ← Consensus et dispatch (les fondamentaux)
├── configuration/         ← Config validée par consensus multi-IA
├── developpement/         ← Cycle dev complet, code review, TDD
├── debug/                 ← Diagnostic multi-perspectif, post-mortem
├── automatisation/        ← CI/CD, backup, monitoring, maintenance
├── consensus-vote/        ← Implémentation technique (Python, LangChain)
├── creation/              ← Création de contenu et assets
├── documentation/         ← Documentation technique multi-IA
├── migration/             ← Migration de configs et systèmes
├── monitoring/            ← Surveillance et alertes
├── recherche/             ← Veille et recherche technique
├── securite/              ← Audit et hardening
├── trading/               ← Analyse financière multi-modèle
├── vocal/                 ← Commandes vocales et TTS
└── web-social/            ← Automatisation web et réseaux sociaux
```

---

## ⚡ Cas d'usage rapides

- **Premier test rapide** → `00-demarrage/`
- **Code review robuste** → `developpement/` (prompt 2)
- **Bug difficile à résoudre** → `debug/` (prompt 1 ou 2)
- **Décision d'architecture** → `01-core/consensus-vote.md`
- **Router vers le bon modèle** → `01-core/cluster-dispatch.md`
- **Automatiser une tâche** → `automatisation/`
- **Analyse trading** → `trading/`

---

## 🔗 Liens utiles

- Configuration du cluster JARVIS → [`prompts/cluster/`](../cluster/)
- Modèles locaux disponibles → [`prompts/models-locaux/`](../models-locaux/)
- Plugins Claude Code → [`configs/claude-code-complet/`](../../configs/claude-code-complet/)

---

*Dernière mise à jour : 20 mars 2026 — JARVIS M1*
