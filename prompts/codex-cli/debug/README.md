# Codex CLI — Debug

## Description
Prompts de debugging avec Codex CLI : diagnostic systematique, analyse de logs, debug de cluster, debug de services Linux et correction de bugs. Codex excelle dans le diagnostic terminal et l'analyse de stack traces.

## Configuration requise
- Codex CLI installe et configure
- Acces aux logs systeme (`journalctl`)
- Acces aux outils de diagnostic (`ss`, `ps`, `top`, `nvidia-smi`)
- Suite de tests disponible (`uv run pytest`)

---

## Prompts par type de tache

### Creation — Test de reproduction de bug

```
Tu es Codex CLI en mode debug.
Probleme : [BUG, ERREUR, LOG, COMPORTEMENT]

1) Reproduis ou inspecte le bug avec les fichiers et logs lies.
2) Ecris un test qui reproduit le bug exactement.
3) Nomme-le test_reproduce_bug_[NOM_DESCRIPTIF].
4) Place-le dans tests/test_[module].py.
5) Verifie que le test echoue bien.

Ne corrige PAS le bug encore. Test de reproduction seulement.
Structure : Goal/Analysis/Changes/Tests.
```

---

### Debug — Processus systematique complet

```
Tu es Codex CLI en mode debug.
Probleme : [BUG, ERREUR, LOG, COMPORTEMENT]
1) Reproduis ou inspecte le bug avec les fichiers et logs lies.
2) Liste les causes probables par ordre de vraisemblance.
3) Corrige la cause racine, pas seulement le symptome.
4) Verifie avec tests, commandes ou checks runtime.
Structure : Goal/Analysis/Changes/Tests.
```

---

### Debug — Analyse de stack trace

```
Analyse cette stack trace et trouve la cause racine :

[COLLER LA STACK TRACE]

## PROCESSUS
1. Lis la stack trace de bas en haut
2. Identifie :
   - Type d'exception
   - Fichier et ligne exacte
   - Fonction appelante
   - Valeurs des variables si disponibles
3. Remonte la chaine d'appels
4. Identifie la cause racine (pas le symptome)
5. Propose le fix minimal
6. Ecris un test qui aurait attrape ce bug
```

---

### Debug — Service Linux en echec

```
Un service Linux ne fonctionne pas. Diagnostique :

Service : [NOM]
Commande : systemctl status [NOM]
Sortie : [COLLER LA SORTIE]

## CHECKLIST SYSTEMATIQUE
1. Status du service : active/inactive/failed ?
2. Logs recents : journalctl -u [NOM] --since "30 min ago" -n 50
3. Processus : ps aux | grep [NOM]
4. Ports : ss -tlnp | grep [PORT]
5. Fichier unit : cat /etc/systemd/system/[NOM].service
6. Dependances : systemctl list-dependencies [NOM]
7. Permissions : ls -la [BINARY_PATH]
8. Resources : free -h && df -h

Pour chaque probleme trouve :
- Cause
- Fix (commande exacte)
- Verification (commande de test)
- Rollback (si le fix echoue)
```

---

### Debug — Probleme cluster JARVIS

```
Debug un probleme sur le cluster JARVIS :

Symptome : [DECRIRE]
Noeud concerne : [M1/M2/M3/OL1]
URL : [IP:PORT]

Verifie dans l'ordre :
1. Ping reseau (le noeud repond-il ?)
2. Service IA (LM Studio / Ollama demarre ?)
3. Modele charge (quel modele, quelle VRAM ?)
4. API fonctionnelle (requete test)
5. Performance (latence, tokens/s)

Si le noeud est down :
- Propose un fix
- Active le fallback vers le noeud suivant
- Envoie une alerte Telegram
```

---

### Debug — Probleme de performance terminal

```
Une commande ou un script est trop lent. Diagnostique :

Commande : [COMMANDE]
Temps observe : [DUREE]
Temps attendu : [DUREE]

## PROCESSUS
1. Profile la commande :
   - time [COMMANDE]
   - strace -c [COMMANDE] (appels systeme)
   - python -m cProfile script.py (si Python)

2. Identifie les goulots :
   - I/O disque ? (iostat pendant l'execution)
   - CPU ? (top pendant l'execution)
   - Reseau ? (latence des appels externes)
   - Memoire ? (free -h, swap utilise ?)

3. Optimise le plus gros goulot d'abord

4. Mesure avant/apres
```

---

### Amelioration / Refactoring — Ameliorer les messages d'erreur

```
Ameliore les messages d'erreur dans [FICHIER] :

1. Identifie tous les except et error handling
2. Pour chaque handler :
   - Le message est-il informatif ? (fichier, ligne, valeurs, contexte)
   - Le type d'exception est-il specifique ? (pas bare except)
   - Y a-t-il du logging ? (level, format, context)
3. Ameliore chaque message avec :
   - Contexte : "Erreur lors de [ACTION] sur [OBJET]"
   - Details : variables pertinentes, valeurs, types
   - Suggestion : "Verifier [COMPOSANT] ou essayer [ACTION]"
4. Verifie que les tests passent
```

---

### Documentation — Rapport de debug

```
Genere un rapport de debug pour le probleme resolu :

## FORMAT
### Probleme
- Description
- Date de detection
- Impact

### Diagnostic
- Symptomes observes
- Causes investiguees
- Cause racine identifiee

### Resolution
- Fix applique (diff)
- Tests ajoutes
- Verification

### Prevention
- Comment eviter ce probleme a l'avenir
- Monitoring a ajouter
- Documentation a mettre a jour
```

---

## Exemples concrets

### Exemple 1 : Debug rapide
```bash
codex "Le endpoint /health retourne 500. Diagnostique avec les logs de journalctl"
```

**Resultat attendu** : Analyse des logs, identification de la cause (ex: dependance down), fix propose.

### Exemple 2 : Debug service
```bash
codex "Le service jarvis-mcp.service est en failed. Diagnostique et corrige."
```

**Resultat attendu** : Analyse du status, des logs, du fichier unit, correction et restart.

### Exemple 3 : Debug performance
```bash
codex "Le script autonomy_pulse.py met 45s au lieu de 5s. Profile et optimise."
```

**Resultat attendu** : Profiling avec cProfile, identification du goulot (ex: requete reseau lente), fix avec timeout/cache.

---

## Effet sur le modele
- La structure Goal/Analysis/Changes/Tests empeche le "shotgun debugging"
- La checklist systematique pour les services Linux couvre tous les angles
- L'ordre de verification (reseau → service → modele → API → perf) isole efficacement
- L'exigence de "cause racine, pas le symptome" force une analyse en profondeur
- Le rollback pour chaque fix permet de revenir en arriere en cas de probleme
- Codex excelle dans l'analyse de logs et stack traces grace a son optimisation pour le code
