# Prompt - Construire la bibliotheque Codex CLI

## But

Prompt maitre pour demander a Codex CLI de documenter ses skills, sa configuration et son usage reel dans une bibliotheque partageable.

```text
Tu es Codex CLI sur une machine Linux de production.

Mission :
Construire une bibliotheque exploitable pour un autre utilisateur a partir de la configuration locale de Codex CLI.

Lis et classe :
- ~/.codex/config.toml
- ~/.codex/rules/default.rules
- ~/.codex/skills/
- ~/.codex/log/
- les dossiers de bibliotheque existants

Livrables obligatoires :
1. un catalogue detaille des skills installes
2. un document de configuration complete de A a Z
3. une synthese des effets apres mise en marche
4. des prompts courts pour :
   - choisir le bon skill
   - auditer Codex CLI
   - reconstruire Codex CLI sur une nouvelle machine
   - sanitiser ce qui ne doit pas etre publie

Contraintes :
- ne publie aucun secret
- separe clairement :
  - ce qui est publiable
  - ce qui est prive
  - ce qui est migrable
- classe les skills par usage :
  - developpement
  - documentation
  - browser
  - deploy
  - securite
  - media
  - workflow

Format de sortie :
- Goal
- Sources
- Skills classes
- Configuration A a Z
- Effets pratiques
- Prompts reutilisables
- Fichiers a publier
```
