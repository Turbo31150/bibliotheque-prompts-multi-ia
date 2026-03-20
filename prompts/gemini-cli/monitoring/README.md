# Gemini CLI -- Monitoring

## Description

Prompts pour utiliser Gemini CLI dans la surveillance de systemes Linux, l'analyse de metriques et la creation d'outils de monitoring. Gemini CLI peut executer des commandes systeme directement, ce qui en fait un outil puissant pour le diagnostic en temps reel.

## Cas d'usage
- Diagnostic systeme interactif depuis le terminal
- Creation de scripts de surveillance
- Analyse de logs en temps reel
- Generation de dashboards textuels
- Alertes et notifications automatisees

---

## Prompts prets a copier

### 1 -- Diagnostic systeme complet

```
Execute un diagnostic complet de ce serveur Linux :

1. CPU : charge, top processus, frequence, temperature
2. RAM : utilisation, swap, top consumers
3. Disque : espace par partition, I/O, SMART status
4. GPU : nvidia-smi (temperature, utilisation, VRAM pour chaque GPU)
5. Reseau : interfaces, connexions actives, bandwidth
6. Services : systemd units en erreur
7. Docker : containers actifs, utilisation ressources
8. Securite : derniers logins, tentatives echouees

Presente un resume avec statut global (OK/WARNING/CRITICAL) et les actions recommandees.
```

---

### 2 -- Creer un monitoring en mode texte

```
Cree un script bash de monitoring en mode texte (TUI) qui affiche en temps reel :

## LAYOUT (terminal 80x24)
+------ CPU ------+------ RAM ------+
| [barres usage]  | [usage/total]   |
+----- DISQUE ----+------ GPU ------+
| [% par mount]   | [temp x6 GPUs]  |
+------ SERVICES ------+
| [vert/rouge par service] |
+--- ALERTES ---+
| [dernieres alertes]|

## FEATURES
- Rafraichissement toutes les 5 secondes
- Couleurs : vert < 60%, jaune < 80%, rouge >= 80%
- Historique des alertes (dernieres 10)
- Touche 'q' pour quitter, 'd' pour details, 'l' pour logs
- Pas de dependances externes (bash pur + tput)
```

---

### 3 -- Analyser les logs des dernieres 24h

```
Analyse les logs systeme des dernieres 24 heures :

1. Lis journalctl --since "24 hours ago" --priority=err
2. Lis les logs Docker des containers actifs
3. Lis /var/log/auth.log pour les tentatives de connexion

Pour chaque source :
- Nombre d'erreurs par categorie
- Tendance (en augmentation, stable, en baisse)
- Top 5 des erreurs les plus frequentes
- Correlations temporelles entre les erreurs
- Actions correctives recommandees

Format : rapport structure avec sections par source.
```

---

### 4 -- Surveiller les performances GPU

```
Cree un script de monitoring GPU specialise pour un cluster de 6 GPUs NVIDIA :

## METRIQUES
- Temperature (C) avec seuils d'alerte (75C warning, 85C critique)
- Utilisation GPU (%)
- VRAM utilisee / totale
- Puissance (W) vs TDP
- Fan speed (%)
- Processus utilisant chaque GPU

## FEATURES
- Logging CSV dans ~/gpu-metrics/ avec rotation journaliere
- Alerte TTS quand temperature critique
- Export Prometheus format (textfile collector)
- Graphique ASCII de l'historique des temperatures (derniere heure)
- Detection automatique du nombre de GPUs
```

---

### 5 -- Creer des alertes intelligentes

```
Cree un systeme d'alertes intelligent en bash :

## REGLES
- CPU > 90% pendant > 5 minutes → alerte
- RAM > 85% → alerte
- Disque > 90% → alerte + nettoyage auto (logs, tmp, docker prune)
- GPU temp > 80C → alerte + reduction du workload
- Service down → alerte + tentative de restart (max 3)
- Trop de connexions SSH echouees (> 10/min) → ban IP

## NOTIFICATIONS
- Desktop : notify-send
- Vocal : TTS via jarvis-tts.sh
- Log : fichier structure JSON dans /var/log/alertes/
- Historique : SQLite avec timestamp, severite, message, action prise

## ANTI-SPAM
- Cooldown de 15 minutes entre alertes identiques
- Escalade : 1er = desktop, 2eme = vocal, 3eme = email
```

---

## Exemples d'utilisation

### Exemple : Diagnostic rapide
**Commande** : `gemini "Diagnostique mon serveur, dis-moi si tout va bien"`

**Resultat attendu** : Execution de commandes systeme et rapport avec statut par composant.

### Exemple : Analyse de logs
**Commande** : `gemini "Pourquoi mon serveur est lent depuis ce matin ? Regarde les logs et metriques."`

**Resultat attendu** : Investigation automatique des logs, identification de la cause, et recommandations.

---

## Effet sur le modele
- Gemini CLI execute directement les commandes systeme pour un diagnostic reel
- L'acces au filesystem permet de lire et analyser les logs sans copier-coller
- Les scripts generes sont testes et valides dans le contexte du serveur
- La combinaison diagnostic + action corrective est naturelle en mode CLI
