# BrowserOS — Skills Pack

> 13 skills protocole + 40+ outils MCP + 45+ connexions Strata + 10 valises. Derniere mise a jour : 2026-03-28.

---

## Skills Protocole BrowserOS (13)

Declares dans `core/domino/router.py` sous `BROWSEROS_SKILLS`. Chaque skill correspond a un protocole d'action navigateur.

| # | Skill | Description | Protocole |
|---|-------|-------------|-----------|
| 1 | `navigate` | Navigation vers une URL ou recherche | `navigate_page` + attente chargement + `take_snapshot` |
| 2 | `click` | Clic sur element identifie par snapshot ID | `take_snapshot` → identifier [ID] → `click` → verifier |
| 3 | `fill` | Remplissage de champs de formulaire | `take_snapshot` → `focus` → `fill` → verifier valeur |
| 4 | `screenshot` | Capture d'ecran page ou element | `take_screenshot` ou `save_screenshot` vers fichier |
| 5 | `dom` | Inspection et manipulation DOM | `get_dom` / `search_dom` / `evaluate_script` |
| 6 | `gmail` | Operations Gmail (lire, envoyer, trier, archiver) | Strata Gmail + navigation web fallback |
| 7 | `slack` | Operations Slack (messages, channels, reactions) | Strata Slack + navigation web fallback |
| 8 | `github-web` | Operations GitHub via interface web (PRs, issues, reviews) | Navigation github.com + DOM interaction |
| 9 | `notion` | Operations Notion (pages, databases, blocs) | Strata Notion + navigation web fallback |
| 10 | `calendar` | Operations Google Calendar (evenements, rappels) | Strata Google Calendar + web fallback |
| 11 | `jira` | Operations Jira (tickets, boards, sprints) | Strata Jira + navigation web fallback |
| 12 | `linear` | Operations Linear (issues, projets, cycles) | Strata Linear + navigation web fallback |
| 13 | `telegram-web` | Operations Telegram via interface web | Navigation web.telegram.org + DOM interaction |

---

## Outils MCP par categorie (40+)

### Navigation et pages

| Outil | Fonction |
|-------|----------|
| `navigate_page` | Naviguer vers une URL |
| `new_page` | Ouvrir un nouvel onglet |
| `new_hidden_page` | Ouvrir un onglet cache |
| `close_page` | Fermer un onglet |
| `show_page` | Afficher un onglet specifique |
| `list_pages` | Lister tous les onglets ouverts |
| `get_active_page` | Obtenir l'onglet actif |
| `move_page` | Deplacer un onglet entre fenetres |

### Interaction utilisateur

| Outil | Fonction |
|-------|----------|
| `click` | Clic sur element par ID snapshot |
| `click_at` | Clic aux coordonnees x,y |
| `fill` | Remplir un champ texte |
| `hover` | Survol d'un element |
| `press_key` | Appuyer sur une touche clavier |
| `scroll` | Defiler la page |
| `drag` | Glisser-deposer |
| `focus` | Donner le focus a un element |
| `select_option` | Selectionner dans un dropdown |
| `check` / `uncheck` | Cocher/decocher une case |
| `handle_dialog` | Gerer les dialogues (alert, confirm, prompt) |
| `upload_file` | Uploader un fichier |

### Capture et lecture

| Outil | Fonction |
|-------|----------|
| `take_screenshot` | Capture ecran (retourne image) |
| `take_snapshot` | Snapshot DOM avec IDs elements [47] |
| `take_enhanced_snapshot` | Snapshot enrichi (metadata, accessibilite) |
| `save_screenshot` | Sauvegarder capture vers fichier |
| `save_pdf` | Sauvegarder page en PDF |
| `get_page_content` | Obtenir le contenu textuel de la page |
| `get_page_links` | Obtenir tous les liens de la page |
| `get_dom` | Obtenir l'arbre DOM complet |
| `search_dom` | Rechercher dans le DOM (CSS selector / XPath) |
| `evaluate_script` | Executer du JavaScript dans la page |

### Gestion onglets

| Outil | Fonction |
|-------|----------|
| `group_tabs` | Grouper des onglets par couleur/nom |
| `ungroup_tabs` | Degrouper des onglets |
| `list_tab_groups` | Lister les groupes d'onglets |
| `close_tab_group` | Fermer un groupe entier |
| `update_tab_group` | Modifier un groupe (nom, couleur) |

### Gestion fenetres

| Outil | Fonction |
|-------|----------|
| `create_window` | Creer une nouvelle fenetre |
| `create_hidden_window` | Creer une fenetre cachee |
| `list_windows` | Lister toutes les fenetres |
| `activate_window` | Activer/afficher une fenetre |
| `close_window` | Fermer une fenetre |

### Signets

| Outil | Fonction |
|-------|----------|
| `create_bookmark` | Creer un signet |
| `search_bookmarks` | Rechercher dans les signets |
| `get_bookmarks` | Obtenir l'arbre de signets |
| `update_bookmark` | Modifier un signet |
| `remove_bookmark` | Supprimer un signet |
| `move_bookmark` | Deplacer un signet |

### Historique

| Outil | Fonction |
|-------|----------|
| `get_recent_history` | Historique recent |
| `search_history` | Rechercher dans l'historique |
| `delete_history_url` | Supprimer une URL de l'historique |
| `delete_history_range` | Supprimer une plage d'historique |

### Fichiers et divers

| Outil | Fonction |
|-------|----------|
| `download_file` | Telecharger un fichier |
| `browseros_info` | Informations sur l'instance BrowserOS |
| `suggest_app_connection` | Suggerer une connexion Strata |
| `suggest_schedule` | Suggerer un planning |

---

## Connexions Strata (45+ services)

BrowserOS integre Klavis Strata pour se connecter a 45+ services externes. Protocole de decouverte :

```
1. discover_server_categories_or_actions  → lister les categories
2. get_category_actions                    → lister les actions d'une categorie
3. get_action_details                      → obtenir les parametres
4. execute_action                          → executer avec include_output_fields
5. search_documentation                    → recherche fallback
```

### Services principaux

| Service | Categorie | Actions principales |
|---------|-----------|-------------------|
| Gmail | Email | Lire, envoyer, rechercher, labeller, archiver |
| Slack | Messagerie | Messages, channels, reactions, threads |
| GitHub | Dev | Repos, issues, PRs, reviews, actions |
| Notion | Productivite | Pages, databases, blocs, commentaires |
| Google Calendar | Agenda | Evenements, rappels, disponibilites |
| Jira | Gestion projet | Tickets, boards, sprints, epics |
| Linear | Gestion projet | Issues, projets, cycles, labels |
| Figma | Design | Fichiers, composants, commentaires |
| Salesforce | CRM | Contacts, opportunites, rapports |
| Trello | Kanban | Cartes, listes, tableaux |
| Google Drive | Stockage | Fichiers, dossiers, partage |
| Google Sheets | Tableur | Lecture, ecriture, formules |
| Google Docs | Document | Creation, edition, commentaires |
| Dropbox | Stockage | Fichiers, dossiers, partage |
| Asana | Gestion taches | Taches, projets, sections |
| HubSpot | CRM/Marketing | Contacts, deals, emails |
| Zendesk | Support | Tickets, agents, macros |
| Intercom | Support | Conversations, contacts, articles |
| Airtable | Base donnees | Tables, records, vues |
| Monday.com | Gestion projet | Items, boards, updates |
| Discord | Messagerie | Messages, channels, serveurs |
| Twilio | Communication | SMS, appels, WhatsApp |
| SendGrid | Email | Envoi email transactionnel |
| Stripe | Paiement | Clients, factures, paiements |
| Shopify | E-commerce | Produits, commandes, clients |

### Authentification Strata

En cas d'erreur d'authentification :
1. `handle_auth_failure(server_name, intention: "get_auth_url")`
2. `new_page(auth_url)` — ouvrir dans le navigateur
3. Attendre confirmation utilisateur
4. Retry l'action

---

## Valises Browser (10 packs pre-compiles)

Packs d'actions pre-compiles pour des workflows courants. Chaque valise enchaine plusieurs outils MCP en sequence optimisee.

| # | Valise | Contenu | Usage |
|---|--------|---------|-------|
| 1 | **LinkedIn Publish** | navigate → fill → upload → click publish → screenshot | Publication post LinkedIn avec image |
| 2 | **Gmail Quick Reply** | navigate gmail → search → click thread → fill reply → send | Reponse rapide email |
| 3 | **GitHub PR Review** | navigate PR → read diff → get_page_content → comment | Review de Pull Request |
| 4 | **Notion Daily Log** | navigate workspace → create page → fill template → save | Journal quotidien Notion |
| 5 | **Calendar Check** | navigate calendar → take_snapshot → extract events → format | Verification agenda du jour |
| 6 | **Slack Digest** | navigate channels → read unread → summarize → post digest | Resume des messages non lus |
| 7 | **Web Research** | navigate search → extract results → visit top 5 → compile | Recherche web structuree |
| 8 | **Screenshot Audit** | list_pages → take_screenshot each → save to folder | Capture de toutes les pages ouvertes |
| 9 | **Form Filler** | navigate form → take_snapshot → fill all fields → submit | Remplissage formulaire automatise |
| 10 | **Tab Cleanup** | list_pages → group by domain → close duplicates → organize | Nettoyage et organisation onglets |

---

## Protocole Observe → Act → Verify

Chaque action BrowserOS suit ce cycle :

```
1. OBSERVE : take_snapshot → obtenir les IDs elements [47]
2. ACT     : click/fill/navigate avec l'ID obtenu
3. VERIFY  : take_snapshot → confirmer le resultat
```

### Gestion des obstacles

| Obstacle | Action |
|----------|--------|
| Banniere cookies | Fermer et continuer |
| Popup login | Notifier utilisateur, continuer si credentials fournis |
| CAPTCHA / 2FA | Pause, demander resolution manuelle |
| Element non trouve | Scroll down, re-snapshot, retry (max 2 tentatives) |
| Page non chargee | Attendre, retry navigate, timeout 30s |

---

## Chemins cles

```
~/Workspaces/jarvis-linux/core/agents/browseros_operator.py  # Agent BrowserOS
~/Workspaces/jarvis-linux/core/domino/router.py              # BROWSEROS_SKILLS set
~/Workspaces/jarvis-linux/scripts/install_browseros_stack.sh  # Installation stack
~/Workspaces/jarvis-linux/scripts/export_browseros_workflow_pack.sh  # Export workflows
```

## Endpoint BrowserOS

```
API HTTP : http://127.0.0.1:9001/api/action
Chrome headless : port 9222
CDP : ws://127.0.0.1:9222/devtools/browser
```
