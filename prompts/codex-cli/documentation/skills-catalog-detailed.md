# Codex CLI - Catalogue detaille des skills

## Objectif

Donner la liste exploitable des skills disponibles dans Codex CLI sur cette machine, les trier par usage, expliquer leur efficacite pratique, et fournir un prompt court pour les activer proprement.

## Source reelle

- [`/home/turbo/.codex/skills`](/home/turbo/.codex/skills)
- [`/home/turbo/.codex/config.toml`](/home/turbo/.codex/config.toml)
- [`/home/turbo/.codex/rules/default.rules`](/home/turbo/.codex/rules/default.rules)

## Lecture rapide

- `35` skills installes
- usage principal de cette machine :
  - dev
  - audit
  - browser automation
  - documentation
  - deploy
  - media
  - securite
- efficacite la plus forte dans ce contexte :
  - `playwright`
  - `playwright-interactive`
  - `openai-docs`
  - `transcribe`
  - `speech`
  - `netlify-deploy`
  - `vercel-deploy`
  - `render-deploy`
  - `gh-fix-ci`
  - `security-best-practices`

## Tri par categorie

### Developpement et architecture

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `aspnet-core` | haute | app .NET web, API, SignalR, gRPC | reponses plus exactes sur structure .NET et configs Microsoft | `Utilise aspnet-core pour auditer et refactorer cette app .NET.` |
| `chatgpt-apps` | haute | widget + MCP + Apps SDK | structure mieux les apps outillees ChatGPT | `Utilise chatgpt-apps pour scaffold une app ChatGPT avec MCP et widget.` |
| `develop-web-game` | moyenne | jeux web HTML/JS | force une boucle rapide code + test + screenshot | `Utilise develop-web-game pour iterer ce jeu web avec tests Playwright.` |
| `figma` | haute | lecture design Figma | apporte contexte design reel, assets et variables | `Utilise figma pour extraire le contexte de ce design et ses assets.` |
| `figma-implement-design` | tres haute | implementation fidele d'un design | reduit les ecarts visuels et les interpretations vagues | `Utilise figma-implement-design pour coder ce composant a l'identique.` |
| `winui-app` | haute | app Windows native WinUI 3 | cadre propre pour applis desktop Windows modernes | `Utilise winui-app pour architecturer cette app WinUI 3.` |

### Deploy et hebergement

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `cloudflare-deploy` | haute | Workers, Pages, stack Cloudflare | guide le deploy et la config edge | `Utilise cloudflare-deploy pour publier cette app sur Cloudflare.` |
| `netlify-deploy` | haute | sites statiques et front apps | accelere le chemin repo -> site live | `Utilise netlify-deploy pour deployer ce repo.` |
| `render-deploy` | haute | apps full-stack sur Render | aide a produire `render.yaml` et services propres | `Utilise render-deploy pour preparer ce projet pour Render.` |
| `vercel-deploy` | haute | front, Next, apps Node sur Vercel | simplifie publication et previews | `Utilise vercel-deploy pour mettre cette app en prod.` |

### Documentation et contenu structure

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `doc` | haute | `.docx` avec mise en page | garde une sortie Word propre et editables | `Utilise doc pour generer ce document Word propre.` |
| `pdf` | haute | lecture ou generation PDF | meilleure fiabilite de rendu et d'extraction | `Utilise pdf pour auditer et reconstruire ce PDF.` |
| `slides` | haute | `.pptx` et decks | produit des slides editables au lieu d'images | `Utilise slides pour creer cette presentation.` |
| `spreadsheet` | haute | Excel, CSV, TSV | gere structure, formules et revue visuelle | `Utilise spreadsheet pour produire ce fichier xlsx.` |
| `jupyter-notebook` | moyenne | notebooks d'experimentation | aide a scaffold des notebooks propres et reutilisables | `Utilise jupyter-notebook pour creer un notebook d'analyse.` |

### Browser et interface reelle

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `playwright` | tres haute | browser automation terminal | permet tests reels, snapshots et debug UI | `Utilise playwright pour verifier cette interface dans un vrai navigateur.` |
| `playwright-interactive` | tres haute | debug navigateur persistant | iteration rapide sans relancer a chaque tour | `Utilise playwright-interactive pour deboguer ce flux UI en continu.` |
| `screenshot` | moyenne | capture desktop/systeme | permet preuve visuelle hors web pur | `Utilise screenshot pour capturer cet etat de l'application.` |

### GitHub et workflow d'equipe

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `gh-address-comments` | haute | traiter commentaires PR | structure la reponse aux reviews GitHub | `Utilise gh-address-comments pour traiter les commentaires de cette PR.` |
| `gh-fix-ci` | haute | CI GitHub cassée | aide a diagnostiquer vite logs/actions | `Utilise gh-fix-ci pour analyser les checks en echec.` |
| `linear` | moyenne | tickets Linear | facilite tri et mise a jour du pilotage | `Utilise linear pour ranger cette tache en ticket exploitable.` |
| `yeet` | haute | stage + commit + push + PR | accelere la fin de cycle quand tout est valide | `Utilise yeet pour publier cette branche proprement.` |

### Notion et capitalisation

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `notion-knowledge-capture` | moyenne | wiki, how-to, FAQ | transforme le travail en memoire exploitable | `Utilise notion-knowledge-capture pour enregistrer cette decision.` |
| `notion-meeting-intelligence` | moyenne | preparation de reunions | structure agendas et prereads | `Utilise notion-meeting-intelligence pour preparer cette reunion.` |
| `notion-research-documentation` | moyenne | recherche depuis Notion | consolide plusieurs sources internes | `Utilise notion-research-documentation pour faire ce brief.` |
| `notion-spec-to-implementation` | haute | PRD -> plan d'execution | relie spec, taches et implementation | `Utilise notion-spec-to-implementation pour transformer cette spec en plan.` |

### Securite

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `security-best-practices` | haute | revue secure-by-default | fait remonter les manques de securite evidents | `Utilise security-best-practices pour revoir ce module JS.` |
| `security-ownership-map` | moyenne | ownership securite via git | revele code sensible orphelin et bus factor | `Utilise security-ownership-map pour cartographier la propriete securite du repo.` |
| `security-threat-model` | haute | menace et abus path | force une vision systeme des frontieres de confiance | `Utilise security-threat-model pour modeliser les risques de ce service.` |

### Media, voix et contenu multimodal

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `imagegen` | haute | generation ou edition d'images | fournit un pipeline image pilotable depuis l'API | `Utilise imagegen pour produire ce visuel produit.` |
| `speech` | haute | text-to-speech | genere des voix de sortie propres et reutilisables | `Utilise speech pour narrer ce texte.` |
| `transcribe` | tres haute | transcription audio/video | convertit vite audio en texte avec diarisation | `Utilise transcribe pour transcrire cet enregistrement.` |
| `sora` | moyenne | generation/remix video | ajoute une brique video creative pilotable | `Utilise sora pour generer une video de demo.` |

### Recherche, observabilite, outils specialises

| Skill | Efficacite | Quand l'utiliser | Effet apres mise en marche | Prompt court |
|---|---|---|---|---|
| `openai-docs` | tres haute | docs OpenAI officielles | ancre les reponses dans la doc a jour | `Utilise openai-docs pour verifier la meilleure API OpenAI pour ce cas.` |
| `sentry` | moyenne | erreurs prod via Sentry | tire des signaux reels plutot que de supposer | `Utilise sentry pour lire les erreurs de production recentes.` |

## Skills les plus utiles sur cette machine

### Top priorite Codex CLI

- `playwright`
- `playwright-interactive`
- `openai-docs`
- `transcribe`
- `speech`
- `gh-fix-ci`
- `security-best-practices`
- `netlify-deploy`
- `vercel-deploy`
- `render-deploy`

### Pourquoi

- ils collent a ton usage reel Linux + JARVIS + navigateur + publication
- ils donnent des preuves concretes :
  - capture
  - test
  - deploy
  - transcription
  - documentation officielle
- ils reduisent fortement les reponses vagues ou purement theorique

## Effets concrets apres activation d'un skill

- meilleure structure de travail
- meilleur choix d'outils
- reduction des suppositions
- plus de sorties directement executables
- moins de code invente quand un workflow dedie existe deja

## Prompt maitre pour choisir les bons skills

```text
Tu es Codex CLI sur une machine Linux avec skills locaux.
Tache : "<objectif>".
1. Identifie les 1 a 3 skills les plus adaptes.
2. Explique pourquoi chacun est pertinent.
3. Dis l'ordre d'utilisation optimal.
4. Execute ensuite la tache en suivant ces skills sans inventer de workflow si un skill existe deja.
Format :
- Skills choisis
- Pourquoi
- Ordre
- Execution
```
