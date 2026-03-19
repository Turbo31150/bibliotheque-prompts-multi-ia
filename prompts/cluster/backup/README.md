# Cluster — Backup

## Pipeline de Sauvegarde

Le systeme de backup JARVIS protege l'ensemble des donnees du cluster avec une pipeline automatisee quotidienne.

## Composants Sauvegardes

| Type | Quantite | Description |
|------|----------|-------------|
| Bases SQLite | **103** | Metriques, cache, feedback, routage, logs |
| Git bundles | Tous les repos | Snapshot complet des repositories |
| Configurations | Toutes | LM Studio, Ollama, JARVIS, systemd |
| Prompts | Bibliotheque complete | Ce repository |

## Planning

```
Execution : tous les jours a 03:00
Duree moyenne : 15-25 minutes
```

## Etapes du Pipeline

### 1. Dump SQLite

```bash
# Pour chaque base de donnees
for db in /home/turbo/jarvis-linux/data/*.db; do
    sqlite3 "$db" ".backup /backup/sqlite/$(basename $db)"
done
```

### 2. Git Bundle

```bash
# Snapshot complet de chaque repo
cd /home/turbo/jarvis-linux
git bundle create /backup/git/jarvis-linux-$(date +%Y%m%d).bundle --all
```

### 3. Sync vers HDD Externe

```bash
rsync -avz --delete /backup/ /mnt/hdd-backup/jarvis/
```

### 4. Verification d'Integrite

```bash
# Verifier chaque base SQLite sauvegardee
for db in /backup/sqlite/*.db; do
    sqlite3 "$db" "PRAGMA integrity_check;" | grep -q "ok" || echo "ERREUR: $db"
done

# Verifier les bundles git
for bundle in /backup/git/*.bundle; do
    git bundle verify "$bundle" || echo "ERREUR: $bundle"
done
```

### 5. Notification Telegram

```bash
# Envoi du rapport de backup
curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
  -d chat_id="${CHAT_ID}" \
  -d text="Backup JARVIS OK — 103 DBs, $(du -sh /backup/ | cut -f1) total"
```

## Procedure de Restauration

### Restaurer une base SQLite

```bash
cp /backup/sqlite/metrics.db /home/turbo/jarvis-linux/data/metrics.db
```

### Restaurer un repo git

```bash
git clone /backup/git/jarvis-linux-20260319.bundle jarvis-linux-restored
```

### Restauration complete

```bash
# 1. Arreter JARVIS
sudo systemctl stop jarvis

# 2. Restaurer les bases
cp /backup/sqlite/*.db /home/turbo/jarvis-linux/data/

# 3. Restaurer les configs
cp /backup/configs/* /home/turbo/jarvis-linux/configs/

# 4. Redemarrer
sudo systemctl start jarvis
```

## Retention

- **7 jours** de backups quotidiens conserves
- **4 semaines** de backups hebdomadaires (dimanche)
- **3 mois** de backups mensuels (1er du mois)
