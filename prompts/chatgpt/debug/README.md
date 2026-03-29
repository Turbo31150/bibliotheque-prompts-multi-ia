# ChatGPT — Debug

> Prompts optimises pour le debugging avec ChatGPT.

---

## Description

ChatGPT est particulierement efficace pour le debugging grace a sa capacite multimodale (coller des screenshots d'erreurs), le Code Interpreter pour reproduire les bugs, et le web browsing pour chercher des solutions a jour.

## Configuration

- Modele : GPT-4o
- Code Interpreter actif (pour reproduire les bugs)
- Web Browsing actif (pour chercher les issues connues)

## Prompts par type

### Debug basique — coller et expliquer
```
Erreur rencontree :

[COLLER LE TRACEBACK COMPLET]

Contexte :
- Langage : [PYTHON/BASH/JS...]
- OS : Linux (Ubuntu/Fedora)
- Version : [VERSION]

Explique la cause et propose un fix.
```

### Debug avance — analyse de stack trace
```
Analyse cette stack trace en profondeur :

[COLLER LA STACK TRACE]

Pour chaque frame :
1. Que fait cette ligne ?
2. Pourquoi elle echoue ?
3. Quelle est la cause racine (pas le symptome) ?

Propose un fix et une strategie pour eviter ce type d'erreur.
```

### Debug de performance
```
Ce code est lent (mesure : [TEMPS]):

[COLLER LE CODE]

Profil :
- Quelles lignes sont les plus couteuses ?
- Pourquoi ?
- Comment optimiser sans changer l'API publique ?
- Benchmark avant/apres attendu
```

### Debug visuel (screenshot)
```
[JOINDRE UN SCREENSHOT DE L'ERREUR]

Explique cette erreur et propose un fix.
Contexte : [APPLICATION / FRAMEWORK / OS]
```

## Exemples concrets

```
Erreur rencontree :

Traceback (most recent call last):
  File "monitor.py", line 45, in <module>
    asyncio.run(main())
  File "/usr/lib/python3.13/asyncio/runners.py", line 194, in run
    return runner.run(main)
RuntimeError: This event loop is already running

Contexte : Python 3.13, script de monitoring GPU, Linux.
Explique et propose un fix.
```

```
Mon script bash plante silencieusement :

#!/bin/bash
set -e
result=$(curl -s https://api.example.com/data)
echo $result | jq '.items[]'

Parfois jq ne retourne rien. Pourquoi ? Comment rendre ca robuste ?
```

## Effet sur le modele

- ChatGPT est tres bon pour expliquer les erreurs connues — il a un enorme corpus de Stack Overflow et GitHub Issues
- Le format "cause racine, pas symptome" force une analyse profonde au lieu d'un quick fix
- GPT-4o peut lire les screenshots d'erreurs (terminaux, navigateurs, IDE)
- Le Code Interpreter permet de reproduire le bug en sandbox pour valider le fix
- Attention : ChatGPT peut halluciner des solutions pour des bugs rares — toujours verifier avec le web browsing
