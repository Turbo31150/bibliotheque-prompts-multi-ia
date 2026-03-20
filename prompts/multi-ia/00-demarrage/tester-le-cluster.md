# Tester le cluster JARVIS — Procédure complète

Avant d'utiliser le multi-IA, vérifier que tous les noeuds répondent correctement.

---

## Vérification en 3 minutes

### Étape 1 — Router principal (M1 local)

```bash
# Test de santé du router JARVIS
curl http://127.0.0.1:8000/health

# Résultat attendu :
# {"status": "ok", "nodes": 4, "router": "active"}

# Liste des modèles actifs
curl http://127.0.0.1:8000/api/models
```

### Étape 2 — Noeuds locaux

```bash
# M1 — qwen3-8b (127.0.0.1:1234)
curl http://127.0.0.1:1234/health
# ou
curl http://127.0.0.1:1234/v1/models

# M2 — deepseek-r1 (192.168.26.x:1234)
curl http://192.168.26.x:1234/health

# M3 — deepseek-r1 fallback (192.168.113.x:1234)
curl http://192.168.113.x:1234/health

# OL1 — gpt-oss:120b (127.0.0.1:11434)
curl http://127.0.0.1:11434/api/tags
```

### Étape 3 — Test d'inférence réelle

```bash
# Test minimal sur qwen3 (le plus rapide)
curl -X POST http://127.0.0.1:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-8b",
    "messages": [{"role": "user", "content": "Réponds juste : OK"}],
    "max_tokens": 10
  }'

# Test consensus via JARVIS
curl -X POST http://127.0.0.1:8000/api/consensus \
  -H "Content-Type: application/json" \
  -d '{"question": "Réponds juste OK", "models": ["claude", "qwen3"]}'
```

---

## Commande de diagnostic complète

```bash
# Script de vérification globale (à copier dans un fichier check-cluster.sh)

echo "=== JARVIS Cluster Health Check ==="

echo -n "Router (8000) : "
curl -s http://127.0.0.1:8000/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','ERROR'))" 2>/dev/null || echo "OFFLINE"

echo -n "M1 qwen3 (1234) : "
curl -s http://127.0.0.1:1234/health | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK')" 2>/dev/null || echo "OFFLINE"

echo -n "OL1 ollama (11434) : "
curl -s http://127.0.0.1:11434/api/tags | python3 -c "import sys,json; d=json.load(sys.stdin); print(str(len(d.get('models',[]))) + ' modèles')" 2>/dev/null || echo "OFFLINE"

echo -n "GPU temp M1 : "
nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader 2>/dev/null | head -1 | xargs -I{} echo "{}C" || echo "N/A"

echo "=== Fin du check ==="
```

---

## Interprétation des résultats

| Statut | Ce que ça signifie | Action |
|--------|-------------------|--------|
| Tous OK | Cluster opérationnel | Utiliser normalement |
| 1 noeud offline | Mode dégradé | Le routeur redirige automatiquement |
| Router offline | Pas de consensus possible | Utiliser les modèles directement |
| GPU > 75°C | Warning thermique | Réduire la charge, attendre |
| GPU > 85°C | Critique | Arrêter les inférences |
| Tous offline | Cluster down | Redémarrer les services |

---

## Redémarrage rapide

```bash
# Redémarrer JARVIS (si systemd)
sudo systemctl restart jarvis

# Ou via commande directe
cd /home/turbo/jarvis-linux && python3 -m src.main &

# Redémarrer LM Studio (modèles locaux)
# → Interface graphique LM Studio > Server > Start

# Redémarrer Ollama
ollama serve &
```

---

## Mode dégradé — Utiliser sans cluster

Si le cluster n'est pas disponible, utiliser les IA directement :

| Remplace | Par | Comment |
|----------|-----|---------|
| Consensus JARVIS | 2-3 onglets navigateur | Claude.ai + ChatGPT + Perplexity |
| qwen3 local | Claude API | Plus lent mais équivalent |
| /consensus | Copier-coller manuel | Envoyer le même prompt dans chaque IA |

---

*Retour : [README.md](../README.md) — Voir aussi : [../cluster/dispatch-engine/](../../cluster/dispatch-engine/)*
