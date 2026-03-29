# Gemini CLI — Automatisation

> Prompts optimises pour l'automatisation avec Gemini CLI : cron jobs, taches planifiees, monitoring systeme.

---

## Description

Gemini CLI est particulierement adapte a l'automatisation systeme grace a son integration terminale native. Il peut generer des cron jobs, des timers systemd, des scripts de monitoring et des pipelines d'automatisation.

## Configuration

- Gemini CLI installe et configure (voir `configuration/`)
- Acces aux outils systeme : `crontab`, `systemd`, `at`
- GEMINI.md avec le contexte infrastructure

## Prompts par type

### Creation de cron job
```bash
gemini "Cree un cron job pour [TACHE] :

## Planning
- Frequence : [TOUTES LES X MINUTES / HEURES / JOURS]
- Horaire : [HEURE SI APPLICABLE]

## Script
- Langage : bash ou Python
- Logging : /var/log/[nom]-cron.log
- Lock file : eviter les executions concurrentes
- Notification en cas d'erreur

Livrable : script + ligne crontab + commande d'installation."
```

### Timer systemd (alternative a cron)
```bash
gemini "Cree un timer systemd pour [TACHE] :

## Planning : [EXPRESSION ONCALENDAR]
## Service associe : [SCRIPT/COMMANDE]

Avantages sur cron :
- Journalctl pour les logs
- Dependencies
- Resource limits

Livrable : fichier .timer + .service + commandes d'activation."
```

### Monitoring automatise
```bash
gemini "Cree un systeme de monitoring automatise :

## Metriques
- CPU / RAM / Disk usage
- Temperatures GPU (nvidia-smi)
- Services actifs (systemctl)
- Ports ouverts

## Alertes
- Seuils configurables
- Notification : [WEBHOOK/EMAIL/SMS]
- Cooldown entre alertes : [MINUTES]

## Execution
- Toutes les [N] minutes via systemd timer
- Historique en JSON/SQLite
```

### Pipeline d'automatisation
```bash
gemini "Cree un pipeline d'automatisation pour [WORKFLOW] :

## Etapes
1. [TRIGGER] → detecter [EVENEMENT]
2. [PROCESS] → executer [ACTION]
3. [NOTIFY] → notifier [CANAL]
4. [LOG] → enregistrer le resultat

## Contraintes
- Resilient (retry sur erreur)
- Idempotent
- Observable (metriques/logs)

Livrable : script principal + configs + installation."
```

## Exemples concrets

```bash
gemini "Cree un systeme de monitoring GPU automatise :
- Verifie les 6 GPUs toutes les 5 minutes
- Alerte Discord si temp > 80C ou VRAM > 90%
- Log les metriques en SQLite
- Rapport quotidien a 8h
Timer systemd + script Python + webhook Discord."
```

```bash
gemini "Cree un cron job de nettoyage automatique :
- Supprime les fichiers > 30 jours dans /tmp et /var/log/jarvis/
- Compresse les logs > 7 jours
- Verifie l'espace disque apres nettoyage
- Alerte si disque > 85% apres nettoyage
Script bash, execution quotidienne a 3h du matin."
```

## Effet sur le modele

- Gemini CLI comprend bien les patterns d'automatisation Linux (cron, systemd, at)
- Le format "timer systemd" est preferable a cron — Gemini genere de bons fichiers .timer/.service
- La gestion du lock file (flock) doit etre demandee explicitement sinon Gemini l'oublie
- Les webhooks Discord/Slack sont bien geres — Gemini connait les formats de payload
- Specifier "idempotent" et "resilient" evite les scripts fragiles qui plantent sur les cas limites
