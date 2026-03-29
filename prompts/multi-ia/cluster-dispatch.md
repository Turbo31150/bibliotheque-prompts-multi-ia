# Multi-IA — Cluster Dispatch

> Prompts et strategies pour dispatcher les taches entre les modeles du cluster IA.

---

## Architecture du cluster

```
┌─────────────────────────────────────────────────┐
│                 JARVIS Router                     │
│          (src/config.py + src/commander.py)       │
├─────────────┬──────────┬──────────┬──────────────┤
│     M1      │    M2    │    M3    │     OL1      │
│  qwen3-8b   │deepseek  │deepseek  │ gpt-oss:120b │
│  46 tok/s   │  r1 44/s │r1 fallbk │  51 tok/s    │
│  127.0.0.1  │192.168.26│192.168.113│ 127.0.0.1   │
│   :1234     │  :1234   │  :1234   │  :11434      │
└─────────────┴──────────┴──────────┴──────────────┘
```

---

## Prompt de dispatch intelligent

```
Tu es le routeur JARVIS. Dispatch cette tache vers le modele optimal.

## Tache
[DECRIRE LA TACHE]

## Regles de routage

### Par type de tache
| Type | Modele prefere | Raison |
|------|----------------|--------|
| Code rapide | M1 (qwen3-8b) | 46 tok/s, excellent en code |
| Reasoning complexe | M2 (deepseek-r1) | Specialise reasoning |
| Tache longue | OL1 (gpt-oss:120b) | Context 120K, tres precis |
| Tache critique | Consensus (3+ modeles) | Fiabilite maximale |
| Tache simple | M1 (qwen3-8b) | Plus rapide |

### Par charge
| Condition | Action |
|-----------|--------|
| M1 GPU > 75C | Re-router vers M2 |
| M2 offline | Fallback vers M3 |
| M3 offline | Fallback vers OL1 |
| Tous > 75C | Attendre ou reduire la charge |
| Tous offline | Alerte critique Telegram |

### Par contraintes
| Contrainte | Modele |
|------------|--------|
| /nothink (pas de reasoning) | M1 uniquement |
| think:false | OL1 uniquement |
| max_output_tokens > 4096 | M2 ou OL1 |
| Latence < 2s | M1 (le plus rapide) |

## Decision
Quel modele pour cette tache ? Justifie en une ligne.
```

### Ce que ca fait
Automatise le choix du meilleur modele pour chaque tache en fonction du type, de la charge et des contraintes.

### Effet sur le modele
- Le tableau de routage donne des regles claires et deterministes
- Les conditions de fallback garantissent la resilience
- La justification en une ligne force une decision rapide

---

## Prompt de pipeline parallele

```
Execute ce pipeline en parallele sur le cluster :

## Taches paralleles
1. M1 : [TACHE 1 — code rapide]
2. M2 : [TACHE 2 — reasoning]
3. OL1 : [TACHE 3 — analyse longue]

## Synchronisation
Quand les 3 taches sont terminees :
- Synthetise les resultats
- Identifie les contradictions
- Propose une conclusion unifiee

## Timeout
- Par tache : 60 secondes
- Global : 180 secondes
- Si timeout : utiliser les resultats partiels disponibles
```

---

## Prompt de re-routage cascade

```
Le noeud [NOEUD] est indisponible. Active le re-routage cascade :

1. Verifie les noeuds restants (ping + health check)
2. Redistribue la charge du noeud down :
   - Taches en cours → noeud le moins charge
   - Nouvelles taches → routage normal sans le noeud down
3. Si < 2 noeuds disponibles : mode degrade
   - Desactiver le consensus (pas assez de modeles)
   - Prioriser les taches critiques
   - File d'attente pour les taches non-critiques
4. Envoyer alerte avec :
   - Noeud down
   - Noeuds restants
   - Temps estime de degradation
   - Actions de reparation suggerees
```

---

## Metriques de routage

```
Pour chaque requete routee, enregistrer :
- Timestamp
- Tache (type, complexite)
- Modele choisi
- Latence (ms)
- Tokens consommes (input + output)
- Resultat (succes / erreur / timeout)
- Temperature GPU au moment du routage

Aggreger toutes les heures :
- Requetes par modele
- Latence moyenne par modele
- Taux de succes par modele
- Temperature moyenne par GPU
```

---

## Prerequis
- Cluster IA operationnel (4 noeuds)
- JARVIS router configure (src/config.py)
- Monitoring GPU actif (nvidia-smi)
- Alertes Telegram configurees
