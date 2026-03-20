# Claude Code — Debug

## Description
Prompts de debugging systematique pour Claude Code. Methodologie Reproduce/Isolate/Fix/Verify appliquee a tous les types de bugs : runtime, configuration, cluster, API, performance.

## Configuration requise
- Claude Code avec permissions `journalctl`, `systemctl status`, `grep`, `find`
- Suite de tests existante (`uv run pytest`)
- Acces aux logs systeme et applicatifs
- Plugin `log-analyzer` recommande pour l'analyse automatisee

---

## Prompts par type de tache

### Creation — Ecriture d'un test de reproduction

```
Ecris un test de reproduction pour le bug suivant :

Symptome : [DECRIRE]
Fichier concerne : [CHEMIN]
Conditions : [QUAND CA SE PRODUIT]

Le test doit :
1. Reproduire exactement les conditions du bug
2. Echouer avec le meme message d'erreur
3. Etre nomme test_reproduce_bug_[NOM_DESCRIPTIF]
4. Etre place dans tests/test_[module].py
5. Inclure un commentaire expliquant le bug attendu

Ne corrige PAS le bug. Ecris seulement le test.
```

---

### Amelioration / Refactoring — Ameliorer la gestion d'erreurs

```
Analyse le fichier [CHEMIN] et ameliore la gestion d'erreurs :

1. Identifie tous les points de failure potentiels
2. Pour chaque point :
   - Quel type d'erreur peut survenir ?
   - Est-elle attrapee correctement ?
   - Le message d'erreur est-il utile pour le diagnostic ?
   - Y a-t-il un fallback ou un retry ?
3. Propose des ameliorations :
   - Remplace les bare except par des except specifiques
   - Ajoute du contexte aux messages d'erreur (fichier, ligne, valeurs)
   - Ajoute des retries avec backoff pour les erreurs reseau
   - Ajoute du logging structure (pas print)
4. Verifie que les tests passent apres modification
```

---

### Debug — Processus systematique complet

```
Un bug a ete detecte. Suis ce processus de debug systematique :

## BUG REPORT
- Symptome : [DECRIRE LE SYMPTOME]
- Contexte : [QUAND CA SE PRODUIT]
- Logs/erreur : [COLLER L'ERREUR]

## REPRODUCE
1. Trouve la sequence exacte qui reproduit le bug
2. Ecris un test qui echoue (test_reproduce_bug_XXX)
3. Confirme que le test echoue bien

## ISOLATE
1. Trace l'execution depuis le point d'entree
2. Identifie la ligne exacte qui cause le probleme
3. Explique POURQUOI ca bugge (cause racine, pas le symptome)

## FIX
1. Propose le fix minimal (moins de changements = moins de risque)
2. Applique le fix
3. Explique pourquoi ce fix resout la cause racine

## VERIFY
1. Relance le test de reproduction — il doit passer
2. Relance la suite de tests complete — rien ne doit regresser
3. Verifie manuellement si possible

Ne propose JAMAIS un fix sans avoir identifie la cause racine.
```

---

### Debug — Analyse de logs

```
Analyse ces logs et identifie le probleme :

```
[COLLER LES LOGS ICI]
```

## PROCESSUS
1. Identifie les lignes d'erreur (ERROR, CRITICAL, Exception, Traceback)
2. Reconstruit la chronologie des evenements
3. Identifie le premier point de defaillance (root cause)
4. Distingue les erreurs primaires des erreurs en cascade
5. Propose un diagnostic avec niveau de confiance (%)

## FORMAT DE SORTIE
| Timestamp | Niveau | Composant | Message | Analyse |
|-----------|--------|-----------|---------|---------|
| ... | ... | ... | ... | ... |

Cause racine probable : [DESCRIPTION]
Confiance : [XX%]
Fix propose : [DESCRIPTION]
```

---

### Debug — Stack trace Python

```
Analyse cette stack trace et resous le probleme :

```
[COLLER LA STACK TRACE]
```

## PROCESSUS
1. Lis la stack trace de bas en haut (la derniere frame est la plus proche de l'erreur)
2. Identifie :
   - Le type d'exception (TypeError, ValueError, ConnectionError, etc.)
   - Le fichier et la ligne exacte
   - La fonction appelante
   - Les valeurs des variables si disponibles
3. Remonte la chaine d'appels pour trouver la cause racine
4. Propose le fix minimal
5. Ecris un test qui aurait attrape ce bug
```

---

### Debug — Probleme de connexion cluster

```
Debug un probleme de connexion sur le cluster JARVIS :

Symptome : [DECRIRE — ex: noeud M2 ne repond plus]
Noeud : [M1/M2/M3/OL1]
IP:Port : [ex: 192.168.1.26:1234]

Verifie dans l'ordre :
1. Ping reseau : le noeud repond-il ?
2. Port ouvert : le service ecoute sur le bon port ?
3. Service IA : LM Studio / Ollama est demarre ?
4. Modele charge : quel modele, quelle VRAM utilisee ?
5. API fonctionnelle : requete test GET /health
6. Performance : latence, tokens/s

Si le noeud est down :
- Propose un fix (restart service, reload model, reboot)
- Active le fallback vers le noeud suivant
- Envoie une alerte Telegram via /notify
```

---

### Debug — Probleme de performance

```
L'application est lente. Diagnostique le probleme de performance :

Symptome : [DECRIRE — ex: endpoint /health met 15s au lieu de 2s]
Environnement : [SPECS MACHINE]

## PROCESSUS
1. MESURER — Prends les metriques avant toute modification :
   - Temps de reponse des endpoints critiques
   - Utilisation CPU/RAM/GPU (top, nvidia-smi)
   - I/O disque (iostat)
   - Connexions reseau (ss -tlnp)

2. PROFILER — Identifie les goulots d'etranglement :
   - Requetes sequentielles qui pourraient etre paralleles ?
   - Requetes N+1 vers la base de donnees ?
   - Calculs bloquants dans le thread principal ?
   - Memory leaks (RSS qui augmente) ?

3. OPTIMISER — Fix par ordre d'impact :
   - Le plus gros goulot d'abord
   - Mesurer apres chaque modification
   - Arreter quand l'objectif est atteint

4. VALIDER — Confirmer l'amelioration :
   - Benchmark avant/apres
   - Tests de charge si pertinent
   - Aucune regression fonctionnelle
```

---

### Documentation — Rapport de bug

```
Genere un rapport de bug complet pour [BUG_DESCRIPTION].

Format :
## Bug Report
- **Titre** : [Court et descriptif]
- **Severite** : CRITICAL / HIGH / MEDIUM / LOW
- **Composant** : [Module/fichier concerne]
- **Version** : [Version du code]
- **Date** : [Date de detection]

## Reproduction
1. [Etape 1]
2. [Etape 2]
3. [Etape 3]

## Comportement observe
[Description + logs]

## Comportement attendu
[Description]

## Cause racine
[Analyse technique]

## Fix applique
[Description du fix + commit/PR]

## Tests ajoutes
[Liste des tests]
```

---

## Exemples concrets

### Exemple 1 : Bug de connexion
```
## BUG REPORT
- Symptome : Le endpoint /health/full retourne 500 au lieu de 200
- Contexte : Quand le noeud M2 est offline
- Logs : "ConnectionError: 192.168.1.26:1234 refused"
```

**Resultat attendu** :
- REPRODUCE : Test qui simule M2 offline
- ISOLATE : Le health_aggregator n'a pas de try/except autour de la requete vers M2
- FIX : Ajouter try/except avec status "offline" au lieu de propager l'exception
- VERIFY : Test passe, suite complete OK

### Exemple 2 : Analyse de stack trace
```
Traceback (most recent call last):
  File "src/mcp_server.py", line 4521, in handle_trading_scan
    result = await scanner.scan_all_pairs()
  File "src/trading_scanner.py", line 89, in scan_all_pairs
    data = await self.fetch_mexc_pairs()
  File "src/trading_scanner.py", line 45, in fetch_mexc_pairs
    response = await self.client.get(url, timeout=5)
httpx.ReadTimeout: timed out
```

**Resultat attendu** : Identification du timeout MEXC API, proposition d'augmenter le timeout ou ajouter un retry avec backoff.

---

## Effet sur le modele
- Le processus Reproduce/Isolate/Fix/Verify empeche le "shotgun debugging"
- L'etape REPRODUCE avec un test ecrit est cruciale — elle ancre le diagnostic
- L'etape ISOLATE force une analyse en profondeur au lieu de deviner
- L'exigence de "fix minimal" evite le over-engineering
- Le format structure pour les logs force une analyse chronologique rigoureuse
- La distinction "cause primaire vs erreurs en cascade" evite de traiter les symptomes
