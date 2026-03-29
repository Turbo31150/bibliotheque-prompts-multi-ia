# Gemini CLI — Creation

> Prompts optimises pour la creation de scripts, d'automatisation et d'infrastructure avec Gemini CLI.

---

## Description

Gemini CLI permet de creer des composants systeme complets directement depuis le terminal : scripts, services systemd, configurations, infrastructure Docker. Son acces au filesystem et son contexte de 1M tokens permettent de generer des projets complets en une seule requete.

## Configuration

- Gemini CLI installe et configure (voir `configuration/`)
- Modele : `gemini-2.5-pro` pour les creations complexes
- GEMINI.md avec le contexte du projet

## Prompts par type

### Creation de script systeme
```bash
gemini "Cree un script bash/Python pour [OBJECTIF] :

## Fonctionnalites
1. [FEATURE 1]
2. [FEATURE 2]
3. [FEATURE 3]

## Contraintes
- Idempotent (peut etre relance sans risque)
- Logging dans /var/log/[nom].log
- Exit codes significatifs
- Compatible systemd

Livrable : script + fichier .service + commande d'installation."
```

### Creation de service systemd
```bash
gemini "Cree un service systemd complet pour [APPLICATION] :

## Parametres
- Executable : [CHEMIN]
- User : [USER]
- Restart policy : always
- Dependances : network-online.target, [AUTRES]

## Livrable
1. Fichier .service
2. Fichier .timer (si tache periodique)
3. Script d'installation
4. Commandes de verification"
```

### Creation d'infrastructure Docker
```bash
gemini "Cree l'infrastructure Docker pour [PROJET] :

## Services
- [SERVICE_1] : [DESCRIPTION]
- [SERVICE_2] : [DESCRIPTION]
- [SERVICE_3] : [DESCRIPTION]

## Livrable
- Dockerfile par service
- docker-compose.yml
- .env.example
- Script de demarrage
- Health checks"
```

### Creation de pipeline CI/CD
```bash
gemini "Cree un pipeline CI/CD pour [PROJET] :

## Stack
- Git : GitHub
- CI : GitHub Actions
- Tests : pytest
- Deploy : [CIBLE]

## Etapes
1. Lint + type check
2. Tests unitaires
3. Build Docker
4. Deploy staging
5. Tests integration
6. Deploy production (manual gate)"
```

## Exemples concrets

```bash
gemini "Cree un systeme de backup incremental pour mon cluster :
- 6 GPUs avec des modeles IA locaux
- Backup des configs dans /etc/jarvis/
- Backup des modeles dans /data/models/ (>100GB, incremental)
- Retention : 7 daily, 4 weekly, 12 monthly
- Notification Discord en cas d'erreur
Script Python + service systemd + timer."
```

```bash
gemini "Cree un reverse proxy Nginx pour exposer :
- Port 8080 → dashboard JARVIS
- Port 8081 → API monitoring
- Port 8082 → Grafana
Avec : SSL auto (Let's Encrypt), rate limiting, headers securite.
Docker compose + configs Nginx."
```

## Effet sur le modele

- Gemini CLI genere des fichiers complets et exploitables — le format "livrable" evite les snippets incomplets
- Le contexte 1M tokens permet de generer des projets multi-fichiers coherents
- Les references filesystem (`@fichier`) permettent de creer des composants compatibles avec l'existant
- Gemini a tendance a generer des configs trop simples — specifier les contraintes de production (health checks, restart policy) force la qualite
- Le pattern "idempotent" est crucial pour les scripts systeme — Gemini le respecte bien quand c'est demande
