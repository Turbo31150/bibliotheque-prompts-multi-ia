# n8n - Securite

## Vue d'ensemble

Workflows n8n dedies a la securite du cluster JARVIS : audit quotidien, analyse d'erreurs dans les logs, detection de derives de configuration.

## Workflows securite

### Security Audit (tous les jours a 1h)

**Schedule** : `0 1 * * *`

```
Cron -> SSH (audit complet)
  -> Code (analyse multi-criteres)
  -> IF (anomalie detectee ?)
    -> OUI : Email rapport urgent + Slack
    -> NON : Email rapport OK
```

**Points d'audit** :

| Categorie | Verification | Commande |
|-----------|-------------|----------|
| Utilisateurs | Comptes avec shell actif | `cat /etc/passwd \| grep -v nologin` |
| Sudo | Acces sudo non autorises | `cat /etc/sudoers.d/*` |
| SSH | Connexions recentes | `last -n 50` |
| SSH | Cles autorisees | `cat ~/.ssh/authorized_keys` |
| Ports | Ports ouverts inattendus | `ss -tlnp` |
| Firewall | Regles iptables/nftables | `nft list ruleset` |
| Docker | Containers privilegies | `docker inspect --format='{{.HostConfig.Privileged}}'` |
| Fichiers | Fichiers SUID suspects | `find / -perm -4000 -type f` |
| Packages | Mises a jour securite | `apt list --upgradable 2>/dev/null` |
| Logs | Tentatives auth echouees | `journalctl -u sshd --since yesterday \| grep Failed` |

**Rapport genere** :
- Score de securite global (0-100)
- Liste des anomalies par severite
- Recommandations d'actions
- Comparaison avec l'audit precedent

### Log Error Analyzer (toutes les 3h)

**Schedule** : `0 */3 * * *`

```
Cron -> SSH (collecte logs 3 dernieres heures)
  -> Code (parser et categoriser erreurs)
  -> Code (deduplication et comptage)
  -> IF (nouvelles erreurs critiques ?)
    -> OUI : Slack avec details + contexte
  -> Set (formater rapport)
  -> Slack (resume erreurs)
```

**Sources de logs analysees** :
| Source | Chemin/Commande | Filtres |
|--------|----------------|---------|
| Syslog | `journalctl --since "3h ago"` | ERROR, CRITICAL, FATAL |
| Docker | `docker logs --since 3h` | Tous containers |
| OpenClaw | Logs applicatifs | Erreurs API, timeout |
| n8n | `~/.n8n/logs/` | Workflow failures |
| Nginx | `/var/log/nginx/error.log` | 5xx, timeout |

**Categorisation automatique** :
- **Securite** : tentatives d'acces non autorisees, bruteforce
- **Performance** : timeout, OOM, CPU throttling
- **Disponibilite** : service down, connection refused
- **Donnees** : corruption, disk full, backup failure

### Cluster Drift Detector (tous les jours a 6h)

**Schedule** : `0 6 * * *`

```
Cron -> SSH (snapshot configuration actuelle)
  -> Code (comparer avec baseline)
  -> IF (derive detectee ?)
    -> OUI : Slack alerte + details des changements
    -> Code (generer diff detaille)
    -> Email (rapport de derive)
  -> Set (mettre a jour baseline si approuve)
```

**Elements surveilles pour derive** :

| Element | Baseline | Detection |
|---------|----------|-----------|
| Docker Compose | `docker-compose.yml` hash | Fichier modifie |
| Variables env | `.env` hash | Variables ajoutees/supprimees |
| Configs systeme | `/etc/` fichiers cles | Modification inattendue |
| Crontab | Export crontab | Jobs ajoutes/supprimes |
| Ports ouverts | Liste reference | Nouveau port expose |
| Packages | Liste dpkg/pip/npm | Package ajoute/supprime |
| Users/Groups | `/etc/passwd` + `/etc/group` | Compte ajoute/modifie |
| Firewall rules | Export nftables | Regle ajoutee/supprimee |

**Workflow de remise en conformite** :
1. Derive detectee -> notification Slack
2. Operateur verifie : changement voulu ou non ?
3. Si voulu : mise a jour de la baseline
4. Si non voulu : rollback automatique ou manuel

## Bonnes pratiques

- Les rapports de securite sont envoyes par email (pas seulement Slack)
- Les credentials sont chiffrees dans n8n, jamais en clair dans les workflows
- L'audit tourne a 1h du matin pour minimiser l'impact performance
- Les baselines de drift sont versionnees dans git
