# Modeles Locaux — Dispatch GPU Cluster

> Utiliser M1/OL1/M2/M3 via `jai` pour inference locale 0 cout.
> M1 : 127.0.0.1:1234 | OL1 : 127.0.0.1:11434

---

## Prompt — Triage rapide (OL1, <2s)

```bash
jai ol1 "Classifie cette tache en une des categories : code, debug, analyse, contenu, monitoring, trading. Tache : [DESCRIPTION]"
```

## Prompt — Analyse profonde (M1, GPU)

```bash
jai m1 "/nothink Analyse ce fichier Python. Identifie les bugs, les problemes de performance, les risques de securite. Retourne un JSON avec : {bugs: [], perf: [], security: [], score: N/10}"
```

## Prompt — Consensus local (M1 + OL1 + M2 + M3)

```bash
jai all-local "Est-ce que cette architecture est scalable ? [DESCRIPTION]. Reponds par oui/non avec 3 arguments."
```

## Prompt — Generation code (M1)

```bash
jai m1 "/nothink Genere un script Python stdlib-only qui [DESCRIPTION]. Format : docstring, argparse --once, JSON output, __main__ guard."
```

## Prompt — Analyse de logs (M1)

```bash
jai m1 "/nothink Analyse ces logs d'erreur et identifie la root cause : $(tail -50 /var/log/syslog)"
```

## Regles GPU obligatoires

```
- LM Studio : --gpu max TOUJOURS (jamais CPU)
- M1 flag : /nothink (desactive le thinking de qwen3)
- OL1 flag : think:false dans le body JSON
- Timeout : 30s pour OL1, 60s pour M1
- Failover : M1 → OL1 → M2 → M3 → GEMINI → CLAUDE
```
