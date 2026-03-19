# Perplexity -- Automatisation

## Description

Prompts pour utiliser Perplexity dans la recherche de solutions d'automatisation, d'outils et de meilleures pratiques. Perplexity aide a identifier les outils existants et les approches eprouvees avant d'implementer.

## Cas d'usage
- Recherche d'outils d'automatisation par besoin
- Comparaison de solutions (Ansible vs Salt vs Puppet)
- Trouver des workflows et recettes existants
- Veille sur les nouvelles solutions d'automatisation
- Meilleures pratiques d'automatisation par domaine

---

## Prompts prets a copier

### 1 -- Trouver le bon outil d'automatisation

```
Recherche le meilleur outil pour automatiser [TACHE] :

## CONTEXTE
- OS : Linux (Ubuntu/Debian)
- Nombre de machines : [N]
- Frequence : [PONCTUEL / RECURRENT]
- Competences : [BASH / PYTHON / YAML]

## CRITERES
1. Facilite d'installation et de configuration
2. Courbe d'apprentissage
3. Communaute et documentation
4. Integration avec l'ecosysteme existant
5. Scalabilite (de 1 a 100 machines)

## CATEGORIES D'OUTILS A COMPARER
- Configuration management (Ansible, Salt, Puppet, Chef)
- Orchestration (Terraform, Pulumi, Crossplane)
- CI/CD (GitHub Actions, GitLab CI, Jenkins, Drone)
- Workflow (n8n, Airflow, Temporal, Prefect)
- Scripting (bash, Python, Go)

Recommandation pour mon cas specifique avec justification.
```

---

### 2 -- Trouver des recettes d'automatisation

```
Recherche des recettes / playbooks existants pour automatiser [TACHE] :

## SOURCES A CHERCHER
1. Ansible Galaxy (roles et collections)
2. GitHub (scripts, playbooks, workflows)
3. Blogs tech (tutoriels avec code)
4. Documentation officielle (guides d'automatisation)

## POUR CHAQUE RECETTE TROUVEE
- Lien source
- Description de ce qu'elle fait
- Prerequis
- Qualite (etoiles, maintenance, derniere MaJ)
- Adaptations necessaires pour mon cas
- Licence

Top 3 recommandees, pret a utiliser ou adapter.
```

---

### 3 -- Comparer les approches d'automatisation

```
Pour automatiser [TACHE], compare ces approches :

1. Script bash custom
2. Ansible playbook
3. n8n workflow
4. GitHub Actions
5. Cron + script Python

## CRITERES DE COMPARAISON
| Critere | Bash | Ansible | n8n | GH Actions | Cron+Python |
|---------|------|---------|-----|------------|-------------|
| Setup time | | | | | |
| Maintenabilite | | | | | |
| Monitoring | | | | | |
| Gestion erreurs | | | | | |
| Scalabilite | | | | | |
| Idempotence | | | | | |
| Courbe apprentissage | | | | | |

Recommandation basee sur mon contexte : [DECRIRE].
```

---

### 4 -- Rechercher les meilleures pratiques

```
Quelles sont les meilleures pratiques d'automatisation pour [DOMAINE] en [ANNEE] :

1. PRINCIPES
   - Idempotence (re-executable sans effet de bord)
   - Infrastructure as Code
   - GitOps
   - Test des automatisations

2. ANTI-PATTERNS A EVITER
   - Automatisation fragile (hardcode, pas de gestion d'erreur)
   - Over-engineering (automatiser ce qui ne devrait pas l'etre)
   - Manque de documentation

3. PATTERNS RECOMMANDES
   - Retry avec backoff exponentiel
   - Circuit breaker
   - Dry-run / mode preview
   - Logging et audit trail

4. REFERENCES
   - Livres / articles de reference
   - Talks de conferences
   - Projets exemplaires

Sources avec liens pour chaque recommandation.
```

---

### 5 -- Veille sur les nouvelles solutions

```
Quelles sont les nouvelles solutions d'automatisation sorties ou mises a jour recemment :

## DOMAINES
- Automatisation systeme / infra
- Automatisation de tests
- Automatisation de workflows (low-code/no-code)
- Automatisation avec IA (agents, copilots)

## POUR CHAQUE SOLUTION
1. Nom et lien
2. Quoi de neuf (feature principale)
3. Comparaison avec l'existant
4. Adoption actuelle (early stage, mature, mainstream)
5. Mon avis devrait-il s'y interesser pour [MON CAS D'USAGE]

Focus sur les solutions open source et self-hosted.
```

---

## Exemples d'utilisation

### Exemple : Outil pour backup
**Prompt** : "Meilleur outil open source pour automatiser les backups de 5 serveurs Linux en 2026."

**Resultat attendu** : Comparaison sourcee de Borgbackup, Restic, Duplicati avec recommandation.

### Exemple : Recettes Ansible
**Prompt** : "Playbook Ansible pour durcir un serveur Ubuntu, le meilleur sur Ansible Galaxy."

**Resultat attendu** : Lien vers le role le plus etoile avec instructions d'utilisation.

---

## Effet sur le modele
- Perplexity recherche les outils et solutions les plus recents
- Les comparaisons s'appuient sur des benchmarks et retours reels
- Les liens vers Ansible Galaxy, GitHub etc. permettent d'utiliser directement
- La veille est toujours a jour grace a la recherche web temps reel
