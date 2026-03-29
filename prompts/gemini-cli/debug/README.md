# Gemini CLI — Debug

> Prompts optimises pour le debugging avec Gemini CLI : analyse de logs, diagnostics systeme.

---

## Description

Gemini CLI excelle en debug systeme grace a son acces direct au terminal Linux. Il peut lire les logs, analyser les sorties de commandes et diagnostiquer des problemes en temps reel.

## Configuration

- Gemini CLI installe et configure (voir `configuration/`)
- Modele : `gemini-2.5-pro` pour le debug complexe
- Acces aux logs systeme (`/var/log/`, `journalctl`)

## Prompts par type

### Debug d'erreur directe
```bash
gemini "Cette commande echoue :

$ [COMMANDE]
$(commande 2>&1)

Explique l'erreur et propose un fix."
```

### Analyse de logs systeme
```bash
gemini "Analyse ces logs et identifie les problemes :

$(journalctl -u [SERVICE] --since '1 hour ago' --no-pager)

Pour chaque probleme :
1. Quoi : description du probleme
2. Pourquoi : cause probable
3. Fix : commande ou action corrective
4. Prevention : comment eviter la recurrence"
```

### Diagnostic GPU
```bash
gemini "Diagnostic GPU :

$(nvidia-smi)
$(nvidia-smi -q -d TEMPERATURE,POWER,UTILIZATION)

Questions :
- Y a-t-il des GPUs en surchauffe ?
- L'utilisation est-elle normale ?
- Y a-t-il des processus zombies ?
- Recommendations ?"
```

### Debug de performance systeme
```bash
gemini "Mon systeme est lent. Voici les metriques :

$(top -bn1 | head -20)
$(free -h)
$(df -h)
$(iostat -x 1 1 2>/dev/null || echo 'iostat non disponible')

Diagnostic :
1. Quel est le goulot d'etranglement ?
2. Quels processus sont suspects ?
3. Actions correctives ?"
```

### Debug reseau
```bash
gemini "Probleme reseau :

$(ip addr show)
$(ss -tulnp)
$(ping -c 3 8.8.8.8 2>&1)
$(curl -s -o /dev/null -w '%{http_code}' https://api.example.com)

Le service [NOM] ne repond pas sur le port [PORT]. Diagnostic ?"
```

## Exemples concrets

```bash
gemini "Mon service JARVIS plante au demarrage :

$(journalctl -u jarvis.service --since '10 min ago' --no-pager | tail -50)
$(systemctl status jarvis.service)

Analyse les logs et propose un fix."
```

```bash
gemini "Ce script Python segfault :

$(python monitor.py 2>&1)
$(dmesg | tail -10)

Contexte : Python 3.13, utilise asyncio et multiprocessing.
Cause probable et fix ?"
```

## Effet sur le modele

- L'acces direct au terminal est la force majeure de Gemini CLI — il peut lire les sorties systeme en temps reel
- Le pattern `$(commande)` dans les prompts permet d'injecter les donnees live directement
- Gemini est bon en analyse de logs mais peut manquer de contexte specifique a des outils rares
- Le format "Quoi/Pourquoi/Fix/Prevention" force une analyse structuree au lieu d'un quick fix
- Pour les diagnostics GPU, nvidia-smi en mode query (`-q -d`) donne plus de details exploitables par le modele
