# Codex CLI -- Monitoring

## Description

Prompts pour utiliser OpenAI Codex CLI dans le monitoring systeme : diagnostic, creation de scripts de surveillance et analyse de metriques directement depuis le terminal.

## Cas d'usage
- Diagnostic systeme interactif
- Creation de scripts de monitoring
- Analyse de logs et metriques
- Generation de dashboards textuels
- Automatisation d'alertes

---

## Prompts prets a copier

### 1 -- Diagnostic systeme

```
Fais un diagnostic complet du serveur :
CPU, RAM, disque, GPU, services, Docker.
Resume avec statut OK/WARNING/CRITICAL.
```

### 2 -- Script de monitoring

```
Cree un script bash de monitoring qui surveille CPU, RAM, disque et GPUs.
Alerte via notify-send si un seuil est depasse.
Log dans /var/log/monitoring.log. Cron toutes les 5 min.
```

### 3 -- Analyser les logs

```
Analyse les logs systeme des dernieres 24h (journalctl).
Identifie les erreurs recurrentes, les patterns et propose des corrections.
```

### 4 -- Alertes GPU

```
Cree un script qui surveille les temperatures des 6 GPUs NVIDIA.
Alerte si > 80C. Log CSV dans ~/gpu-temps.csv.
```

### 5 -- Dashboard texte

```
Cree un dashboard texte (TUI) en bash qui affiche en temps reel :
CPU, RAM, disque, GPUs, services Docker. Rafraichi toutes les 5s.
```

---

## Effet sur le modele
- Codex CLI execute les commandes directement pour un diagnostic reel
- Les scripts generes sont testes dans le contexte du serveur
- L'acces au systeme permet des recommandations adaptees au materiel
