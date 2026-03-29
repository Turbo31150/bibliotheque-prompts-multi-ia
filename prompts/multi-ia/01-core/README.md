# 01-core — Les fondamentaux Multi-IA

Les deux mécanismes centraux du système multi-IA : le consensus et le dispatch.
Lire ces deux fichiers avant d'utiliser n'importe quel autre prompt multi-IA.

---

## Fichiers dans ce dossier

### consensus-vote.md
**Ce que c'est :** Le mécanisme de vote pondéré entre 5 modèles.

**Quand l'utiliser :**
- Décision importante (architecture, technologie, sécurité)
- Code review critique avant merge
- Analyse de risque sur une question complexe

**Résumé :** Chaque modèle répond indépendamment avec un score de confiance. La moyenne pondérée détermine la réponse finale. Seuil d'acceptation : 0,7.

Poids des modèles : Claude (0.30) > Gemini (0.25) > Qwen3 (0.20) > DeepSeek (0.15) > GPT-OSS (0.10)

→ [Lire consensus-vote.md](../consensus-vote.md)

---

### cluster-dispatch.md
**Ce que c'est :** Le routeur intelligent qui choisit le bon modèle pour chaque tâche.

**Quand l'utiliser :**
- Avant chaque requête pour choisir le meilleur modèle
- En cas de surcharge d'un noeud
- Pour optimiser vitesse vs qualité

**Résumé :** Matrice de routage selon le type de tâche, la température GPU et la latence. Fallback automatique si un noeud est offline.

Règles clés :
- Code rapide → M1 qwen3-8b (65 tok/s)
- Reasoning complexe → M2 deepseek-r1
- Tâche longue → OL1 gpt-oss:120b
- Tâche critique → Consensus 3+ modèles

→ [Lire cluster-dispatch.md](../cluster-dispatch.md)

---

## Ordre de lecture recommandé

1. [00-demarrage/](../00-demarrage/) — Premier contact et test du cluster
2. **[consensus-vote.md](../consensus-vote.md)** — Comprendre le vote pondéré ← Tu es ici
3. **[cluster-dispatch.md](../cluster-dispatch.md)** — Comprendre le routage ← Tu es ici
4. [configuration/](../configuration/) — Configurer ton installation
5. Dossier selon ton besoin → [developpement/](../developpement/), [debug/](../debug/), etc.

---

*Ces deux fichiers sont les briques fondamentales utilisées par tous les autres prompts de ce dépôt.*
