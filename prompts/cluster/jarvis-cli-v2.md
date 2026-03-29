# Cluster — JARVIS CLI v2.0

> CLI unifie pour piloter tout le systeme JARVIS Linux.
> Commande : `jarvis <commande>`
> Fichier : `/home/turbo/jarvis-linux/scripts/jarvis-cli.py`

---

## Commandes disponibles

```bash
jarvis status       # Etat complet (load, RAM, GPU, cluster, LM Studio, zombies, services)
jarvis health       # Health check rapide (UP/DOWN par noeud)
jarvis gpu          # GPU status detaille + thermal guard + consommation watts
jarvis security     # Audit securite (ports, fichiers sensibles, root check, thermal)
jarvis clean        # Nettoyage zombies + reset services failed + stale workers
jarvis load [model] # Charger un modele avec --gpu max (thermal guard integre)
jarvis ask "prompt" # Envoyer un prompt au cluster (via jai dispatch)
jarvis dispatch     # Lister les 23 targets IA disponibles
jarvis skills       # Lister tous les skills Gemini + Claude
```

## Couches de securite integrees

### Thermal Guard
```
Avant chaque operation GPU : verifie temperature < 85 degres C.
Si depasse : BLOQUE l'operation et affiche l'alerte.
```

### Action Policy
```
Patterns dangereux detectes et bloques : rm -rf, DROP, DELETE, kill -9, mkfs
Confirmation requise pour : docker restart, git push, send email
```

### Port Audit
```
Verifie que les services critiques ecoutent en LOCAL (127.0.0.1).
Alerte si un service est EXPOSED (0.0.0.0).
```

## Integration avec jai (AI Dispatch)

```bash
# jarvis ask utilise jai en backend
jarvis ask "Analyse ce code Python" --target m1
jarvis ask "Recherche tarifs IA France" --target perplexity
jarvis ask "Consensus sur cette architecture" --target consensus
```

## Prompts d'administration

### Prompt — Diagnostic complet post-incident
```bash
jarvis status && jarvis gpu && jarvis security && jarvis clean
```

### Prompt — Chargement modele securise
```bash
jarvis load deepseek/deepseek-r1-0528-qwen3-8b
# Thermal guard + GPU max + context 26K automatique
```

### Prompt — Health check JSON pour monitoring
```bash
jarvis health --json | python3 -c "import sys,json; d=json.load(sys.stdin); print('ALERTE' if d['level']=='RED' else 'OK')"
```
