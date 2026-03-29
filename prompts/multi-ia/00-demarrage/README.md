# 00 — Démarrage Multi-IA

> **Commence ici.** Ce dossier contient tout ce qu'il faut pour lancer ton premier prompt multi-IA en moins de 5 minutes, sans cluster, sans configuration complexe.

---

## ⚡ Démarrage immédiat — Sans cluster (2 minutes)

Copie ce prompt et envoie-le à **deux IA différentes** (ex: Claude + ChatGPT) :

```
Question : [REMPLACE PAR TA QUESTION]

Réponds en 3 points maximum.
Donne ton niveau de confiance de 1 à 10.
Signale tes incertitudes.
```

**Ensuite :** compare les deux réponses.
- Les points identiques → haute fiabilité, tu peux t'y fier
- Les points divergents → zone d'incertitude, creuse davantage
- Ce qu'une seule IA mentionne → angle unique, à vérifier

---

## 🔌 Démarrage avec le cluster JARVIS (5 minutes)

### Étape 1 — Vérifier que le cluster répond

```bash
# Santé du router
curl http://127.0.0.1:8000/health

# Liste des modèles disponibles
curl http://127.0.0.1:8000/api/models
```

Résultat attendu : `{"status": "ok", "nodes": 4}` (ou le nombre de noeuds actifs)

### Étape 2 — Premier consensus

```bash
curl -X POST http://127.0.0.1:8000/api/consensus \
  -H "Content-Type: application/json" \
    -d '{
        "question": "Quel est le meilleur langage pour un script de monitoring Linux ?",
            "models": ["claude", "qwen3", "deepseek-r1"]
              }'
              ```

              ### Étape 3 — Via Claude Code (le plus simple)

              ```
              /consensus "Quel est le meilleur langage pour un script de monitoring Linux ?"
              ```

              ---

              ## 🎯 Choisir le bon outil selon ta question

              | Type de question | Outil recommandé | Pourquoi |
              |-----------------|-----------------|---------|
              | Code à écrire vite | `qwen3-8b` seul | 65 tok/s, excellent en code |
              | Décision importante | Consensus 3+ modèles | Fiabilité maximale |
              | Bug difficile | Claude + Perplexity | Analyse + sources vérifiées |
              | Recherche technique | Perplexity seul | Sources récentes et vérifiées |
              | Architecture système | Claude + ChatGPT | Raisonnement + documentation |
              | Question factuelle simple | N'importe quel modèle seul | Inutile de multiplier |
              | Raisonnement long | `deepseek-r1` | Spécialisé chain-of-thought |
              | Synthèse de long texte | `gpt-oss:120b` | Contexte 120K |

              ---

              ## 📋 Checklist avant de lancer un consensus

              - [ ] La question est-elle bien formulée ? (précise, sans ambiguïté)
              - [ ] Est-ce vraiment utile d'interroger plusieurs modèles ? (voir tableau ci-dessus)
              - [ ] Ai-je le contexte nécessaire à fournir à chaque modèle ?
              - [ ] Cluster disponible ? (`curl http://127.0.0.1:8000/health`)

              ---

              ## 🔄 Interpréter les résultats

              ```
              Unanimité (4/4 modèles d'accord)   → Haute confiance → Appliquer directement
              Majorité forte (3/4)                → Bonne confiance → Vérifier le point dissonant
              Majorité simple (2/4)               → Confiance moyenne → Investigation supplémentaire
              Pas de majorité (2/2)               → Reformuler la question ou la décomposer
              ```

              ---

              ## ➡️ Prochaines étapes

              Une fois ce premier test réussi :

              1. **Comprendre le consensus** → [`../01-core/consensus-vote.md`](../consensus-vote.md)
              2. **Router intelligemment** → [`../01-core/cluster-dispatch.md`](../cluster-dispatch.md)
              3. **Configurer ton cluster** → [`../configuration/`](../configuration/)
              4. **Aller au cas d'usage** → [`../developpement/`](../developpement/), [`../debug/`](../debug/), etc.

              ---

              ## 🆘 Dépannage rapide

              | Problème | Solution |
              |----------|---------|
              | `curl: connection refused` | Vérifier que JARVIS tourne : `systemctl status jarvis` |
              | Modèle ne répond pas | `curl http://192.168.x.x:1234/health` (ping noeud direct) |
              | Consensus lent | Réduire à 2 modèles au lieu de 4 |
              | Résultats incohérents | Reformuler la question avec plus de contexte |

              ---

              *Fichiers dans ce dossier :*
              - `README.md` — ce guide (point d'entrée)
              - [`premier-prompt-multi-ia.md`](premier-prompt-multi-ia.md) — prompts prêts à copier pour 6 scénarios courants
              - [`choisir-son-modele.md`](choisir-son-modele.md) — arbre de décision détaillé
              - [`tester-le-cluster.md`](tester-le-cluster.md) — procédure de vérification complète du cluster
