# Claude Code — Migration

## Description
Guide complet de migration en 7 etapes pour reproduire un environnement Claude Code + JARVIS sur une nouvelle machine. Couvre l'inventaire, l'export, l'installation, l'import, la validation, l'optimisation et la documentation.

## Configuration requise
- Acces SSH aux deux machines (source et cible)
- Espace disque suffisant sur la cible (minimum 100 GB)
- Meme reseau local pour le cluster (192.168.1.x)
- Cles API a portee de main (Anthropic, Gemini, MEXC, CoinEx, Telegram, Discord)

---

## Prompts par type de tache

### Creation — Plan de migration complet (7 etapes)

```
Je migre mon environnement de developpement vers une nouvelle machine.

Machine source : [SPECS ACTUELLES]
Machine cible : [SPECS NOUVELLES]

Execute le plan de migration suivant :

## PHASE 1 — INVENTAIRE
1. Liste tous les outils installes (claude, uv, node, python, docker, ollama)
2. Liste les versions exactes
3. Liste les fichiers de configuration a migrer
4. Liste les bases de donnees a copier
5. Estime l'espace disque total necessaire

## PHASE 2 — EXPORT
1. Exporte les configurations Claude Code (~/.claude/)
2. Exporte les fichiers memoire
3. Exporte les MCP servers configs
4. Exporte les .env (sans les secrets — remplacer par des placeholders)
5. Sauvegarde les bases de donnees (63 bases, 160 MB)
6. Exporte la crontab
7. Exporte les workflows n8n

## PHASE 3 — INSTALL (sur la nouvelle machine)
1. Installe les prerequis systeme (apt update, build-essential, git)
2. Installe Python 3.13 + uv
3. Installe Node.js 20+
4. Installe Docker + docker-compose
5. Installe Ollama
6. Installe Claude Code (npm install -g @anthropic-ai/claude-code)
7. Installe JARVIS (git clone + uv sync)
8. Installe n8n (npm install -g n8n)
9. Installe LM Studio (si noeud cluster)
10. Installe BrowserOS (docker)

## PHASE 4 — IMPORT
1. Restaure les configurations Claude Code
2. Restaure les fichiers memoire
3. Restaure les MCP servers
4. Restaure les bases de donnees
5. Restaure la crontab
6. Restaure les workflows n8n
7. Configure les .env avec les vrais secrets

## PHASE 5 — VALIDATION
1. Lance /cluster-check
2. Lance /audit
3. Lance les tests (uv run pytest)
4. Verifie chaque MCP server
5. Verifie les crons
6. Verifie n8n
7. Test vocal (TTS + STT)

## PHASE 6 — OPTIMISATION
1. Tune le kernel Linux (sysctl, governor CPU)
2. Configure les cgroups pour JARVIS
3. Optimise les GPUs (power limits, fan curves)
4. Configure le reseau cluster (IPs statiques)

## PHASE 7 — DOCUMENTATION
1. Documente les differences entre l'ancienne et la nouvelle machine
2. Met a jour les fichiers memoire Claude Code
3. Met a jour le CLAUDE.md du projet
4. Cree un script de re-migration pour la prochaine fois
```

---

### Amelioration / Refactoring — Script de migration automatise

```
Cree un script de migration automatise base sur le plan de migration :

## SPECIFICATION
- Langage : Bash
- Fichier : scripts/migrate.sh
- Modes : --export (depuis la source) et --import (vers la cible)

## FONCTIONNALITES
1. --export :
   - Cree une archive tar.gz de toutes les configs
   - Remplace les secrets par des placeholders dans les .env
   - Exporte les bases SQLite
   - Exporte la crontab
   - Genere un manifest.json avec checksums

2. --import :
   - Verifie les prerequis systeme
   - Extrait l'archive
   - Restaure les configs dans les bons chemins
   - Demande les secrets interactivement
   - Verifie les checksums
   - Lance les validations automatiques

## SECURITE
- Ne jamais inclure les vrais secrets dans l'archive
- Verifier les checksums a l'import
- Log toutes les operations
```

---

### Debug — Migration incomplete

```
La migration n'est pas complete. Certains composants ne fonctionnent pas.

## DIAGNOSTIC
Lance les verifications suivantes et reporte le status :

| Composant | Commande de test | Status attendu |
|-----------|-----------------|----------------|
| Claude Code | claude --version | Version affichee |
| Python/uv | uv run pytest --quick | Tests passent |
| LM Studio | curl 127.0.0.1:1234/health | 200 OK |
| Ollama | curl 127.0.0.1:11434/api/tags | Liste des modeles |
| n8n | curl 127.0.0.1:5678 | Dashboard accessible |
| Canvas | curl 127.0.0.1:18800 | Page chargee |
| GPUs | nvidia-smi | 6 GPUs detectes |
| MCP servers | Test chaque MCP | Tous repondent |

Pour chaque composant en echec :
1. Identifie la cause (pas installe, mauvaise config, service arrete)
2. Corrige
3. Verifie
```

---

### Documentation — Rapport de migration

```
Genere un rapport de migration complet :

## FORMAT
### Resume
- Date de migration
- Machine source → Machine cible
- Duree totale
- Status : complete/partielle

### Composants migres
| Composant | Status | Notes |
|-----------|--------|-------|
| ... | OK/PARTIAL/FAIL | ... |

### Fichiers migres
| Chemin | Taille | Checksum | Status |
|--------|--------|----------|--------|
| ... | ... | ... | OK/DIFF |

### Problemes rencontres
| Probleme | Resolution | Temps |
|----------|-----------|-------|
| ... | ... | ... |

### Differences entre machines
| Aspect | Source | Cible | Impact |
|--------|--------|-------|--------|
| CPU | ... | ... | ... |
| GPU | ... | ... | ... |
| RAM | ... | ... | ... |

### Validations
| Test | Resultat |
|------|----------|
| /cluster-check | ... |
| /audit | ... |
| pytest | ... |
```

---

## Checklist de migration

### Fichiers a copier

```bash
# Configurations Claude Code
~/.claude/settings.json
~/.claude/mcp-servers.json
~/.claude/memory/*.md
~/.claude/plugins/

# JARVIS
~/jarvis-linux/.env
~/jarvis-linux/data/*.db          # 63 bases
~/jarvis-linux/system/crontab-jarvis.txt
~/jarvis-linux/configs/

# n8n
~/.n8n/                            # Workflows et credentials

# Ollama
~/.ollama/                         # Modeles telecharges

# SSH et Git
~/.ssh/
~/.gitconfig
```

### Ordre d'installation

```
1. Systeme de base (apt update, build-essential, git)
2. Python 3.13 + uv
3. Node.js 20+
4. Docker + docker-compose
5. Ollama
6. Claude Code (npm install -g @anthropic-ai/claude-code)
7. JARVIS (git clone + uv sync)
8. n8n (npm install -g n8n)
9. LM Studio (si noeud cluster)
10. BrowserOS (docker)
```

---

## Exemples concrets

### Exemple 1 : Lancer la migration
```bash
claude "Migre mon environnement vers la nouvelle machine M2 (Ryzen 7900X, RTX 4090, 64GB RAM)"
```

**Resultat attendu** : Plan de migration adapte aux specs, avec estimation du temps et de l'espace disque.

### Exemple 2 : Validation post-migration
```bash
claude "/cluster-check && /audit"
```

**Resultat attendu** : Status complet du cluster et du systeme sur la nouvelle machine.

---

## Effet sur le modele
- Le plan en 7 phases structurees empeche Claude d'oublier des etapes
- Les phases ordonnees garantissent que les dependances sont respectees
- L'etape VALIDATION finale confirme que tout fonctionne
- La checklist de fichiers a copier sert de reference exhaustive
- Le script de migration automatise rend le processus reproductible
- La documentation des differences entre machines aide le modele a adapter ses recommandations
