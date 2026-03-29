# Catalogue Complet des Outils MCP JARVIS

> Derniere mise a jour : 2026-03-28
> Serveurs MCP : BrowserOS, Claude-in-Chrome, Canva, Notion, Google Calendar

---

## BrowserOS MCP (58 outils)

### Navigation (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| navigate_page | Navigue vers une URL dans la page active | `url` (string) |
| new_page | Ouvre un nouvel onglet avec URL optionnelle | `url?` (string) |
| close_page | Ferme un onglet specifique | `page_id` (string) |
| list_pages | Liste tous les onglets ouverts avec titre et URL | aucun |
| show_page | Active et affiche un onglet specifique | `page_id` (string) |

### DOM et Contenu (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| take_snapshot | Capture le DOM accessible avec IDs d'elements interactifs | `page_id?` |
| get_dom | Recupere l'arbre DOM complet de la page | `page_id?`, `selector?` |
| search_dom | Recherche un element dans le DOM par texte ou selecteur | `query` (string), `page_id?` |
| get_page_content | Extrait le contenu texte principal de la page | `page_id?` |
| get_page_links | Liste tous les liens de la page avec texte et URL | `page_id?` |

### Interaction (13)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| click | Clique sur un element par son ID snapshot | `element_id` (string) |
| click_at | Clique a des coordonnees precises | `x` (number), `y` (number) |
| fill | Remplit un champ de formulaire | `element_id` (string), `value` (string) |
| select_option | Selectionne une option dans un dropdown | `element_id` (string), `value` (string) |
| check | Coche une case a cocher | `element_id` (string) |
| uncheck | Decoche une case a cocher | `element_id` (string) |
| hover | Survole un element | `element_id` (string) |
| drag | Glisse-depose d'un element vers un autre | `source_id`, `target_id` |
| scroll | Defilement de la page | `direction` (up/down/left/right), `amount?` |
| press_key | Simule l'appui sur une touche | `key` (string, ex: "Enter", "Tab") |
| focus | Donne le focus a un element | `element_id` (string) |
| clear | Vide le contenu d'un champ | `element_id` (string) |
| handle_dialog | Gere les dialogues natifs (alert, confirm, prompt) | `action` (accept/dismiss), `text?` |

### Fichiers (4)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| upload_file | Uploade un fichier via un input file | `element_id` (string), `file_path` (string) |
| download_file | Telecharge un fichier depuis une URL | `url` (string), `save_path?` |
| save_screenshot | Sauvegarde une capture d'ecran | `path` (string), `full_page?` (bool) |
| save_pdf | Sauvegarde la page en PDF | `path` (string) |

### Onglets et Groupes (6)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| group_tabs | Regroupe des onglets dans un groupe nomme | `page_ids` (array), `title` (string), `color?` |
| list_tab_groups | Liste tous les groupes d'onglets | aucun |
| close_tab_group | Ferme un groupe d'onglets entier | `group_id` (string) |
| ungroup_tabs | Retire des onglets d'un groupe | `page_ids` (array) |
| update_tab_group | Met a jour un groupe (titre, couleur) | `group_id`, `title?`, `color?` |
| move_page | Deplace un onglet vers une fenetre | `page_id` (string), `window_id` (string) |

### Fenetres (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| list_windows | Liste toutes les fenetres Chrome | aucun |
| create_window | Cree une nouvelle fenetre Chrome | `url?` (string), `incognito?` (bool) |
| create_hidden_window | Cree une fenetre masquee (headless) | `url?` (string) |
| activate_window | Active et met au premier plan une fenetre | `window_id` (string) |
| close_window | Ferme une fenetre Chrome | `window_id` (string) |

### Historique (4)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| search_history | Recherche dans l'historique par mot-cle | `query` (string), `max_results?` (number) |
| get_recent_history | Recupere l'historique recent | `max_results?` (number, defaut: 20) |
| delete_history_url | Supprime une URL de l'historique | `url` (string) |
| delete_history_range | Supprime l'historique sur une plage de dates | `start_time`, `end_time` |

### Signets (6)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| get_bookmarks | Recupere l'arbre des signets | `folder_id?` (string) |
| create_bookmark | Cree un nouveau signet | `title` (string), `url` (string), `parent_id?` |
| update_bookmark | Met a jour un signet | `bookmark_id` (string), `title?`, `url?` |
| remove_bookmark | Supprime un signet | `bookmark_id` (string) |
| move_bookmark | Deplace un signet vers un dossier | `bookmark_id` (string), `parent_id` (string) |
| search_bookmarks | Recherche dans les signets | `query` (string) |

### Scripts et Divers (4)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| evaluate_script | Execute du JavaScript dans la page | `script` (string), `page_id?` |
| take_enhanced_snapshot | Snapshot enrichi avec metadonnees supplementaires | `page_id?` |
| take_screenshot | Capture d'ecran rapide (retour base64) | `page_id?`, `full_page?` |
| browseros_info | Informations sur le serveur BrowserOS | aucun |

### Integrations Externes (2)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| suggest_app_connection | Suggere la connexion a un service externe | `app_name` (string) |
| suggest_schedule | Suggere un planning base sur le contexte | `context` (string) |

**Services disponibles via suggest_app_connection :** Gmail, Slack, GitHub, Notion, LinkedIn, Jira, Linear, Figma, Canva, Salesforce, HubSpot, Asana, Trello, Discord, Zoom, Google Drive, Dropbox, Airtable, Intercom, Zendesk, et 20+ autres.

---

## Claude-in-Chrome MCP (18 outils)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| read_page | Lit le contenu visible de la page active avec elements interactifs | aucun |
| get_page_text | Extrait le texte brut de la page | aucun |
| navigate | Navigue vers une URL | `url` (string) |
| find | Recherche du texte dans la page | `query` (string) |
| form_input | Remplit un champ de formulaire identifie | `field_id` (string), `value` (string) |
| computer | Action souris/clavier de bas niveau | `action` (string), `x?`, `y?`, `text?` |
| javascript_tool | Execute du JavaScript dans la page | `code` (string) |
| read_console_messages | Lit les messages de la console navigateur | `max_messages?` (number) |
| read_network_requests | Lit les requetes reseau capturees | `filter?` (string) |
| gif_creator | Cree un GIF anime a partir de screenshots | `frames` (number), `interval` (ms) |
| resize_window | Redimensionne la fenetre du navigateur | `width` (number), `height` (number) |
| tabs_context_mcp | Recupere le contexte de tous les onglets ouverts | aucun |
| tabs_create_mcp | Cree un nouvel onglet | `url` (string) |
| upload_image | Uploade une image dans un input | `file_path` (string) |
| shortcuts_list | Liste les raccourcis clavier disponibles | aucun |
| shortcuts_execute | Execute un raccourci clavier | `shortcut` (string) |
| switch_browser | Bascule entre navigateurs (Chrome, Firefox) | `browser` (string) |
| update_plan | Met a jour le plan d'actions en cours | `plan` (object) |

---

## Claude AI Native - Canva MCP (28 outils)

### Design (8)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| generate-design | Genere un design a partir d'un prompt textuel | `prompt` (string), `template?` |
| generate-design-structured | Genere un design avec structure detaillee | `structure` (object) |
| create-design-from-candidate | Cree un design depuis un candidat genere | `candidate_id` (string) |
| get-design | Recupere les metadonnees d'un design | `design_id` (string) |
| get-design-content | Recupere le contenu complet d'un design | `design_id` (string) |
| get-design-pages | Liste les pages d'un design | `design_id` (string) |
| get-design-thumbnail | Recupere la miniature d'un design | `design_id` (string) |
| resize-design | Redimensionne un design | `design_id` (string), `width`, `height` |

### Edition (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| start-editing-transaction | Demarre une transaction d'edition | `design_id` (string) |
| perform-editing-operations | Execute des operations d'edition | `transaction_id` (string), `operations` (array) |
| commit-editing-transaction | Valide une transaction d'edition | `transaction_id` (string) |
| cancel-editing-transaction | Annule une transaction d'edition | `transaction_id` (string) |
| request-outline-review | Demande une revue du plan de design | `outline` (object) |

### Export et Assets (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| export-design | Exporte un design (PNG, PDF, SVG, etc.) | `design_id` (string), `format` (string) |
| get-export-formats | Liste les formats d'export disponibles | `design_id` (string) |
| get-assets | Recupere les assets du compte Canva | `query?` (string), `type?` |
| upload-asset-from-url | Uploade un asset depuis une URL | `url` (string), `name` (string) |
| import-design-from-url | Importe un design depuis une URL | `url` (string) |

### Collaboration (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| comment-on-design | Ajoute un commentaire sur un design | `design_id` (string), `message` (string) |
| list-comments | Liste les commentaires d'un design | `design_id` (string) |
| list-replies | Liste les reponses a un commentaire | `comment_id` (string) |
| reply-to-comment | Repond a un commentaire | `comment_id` (string), `message` (string) |
| get-presenter-notes | Recupere les notes de presentation | `design_id` (string), `page_id?` |

### Organisation (5)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| search-designs | Recherche dans les designs | `query` (string) |
| search-folders | Recherche dans les dossiers | `query` (string) |
| create-folder | Cree un nouveau dossier | `name` (string), `parent_id?` |
| move-item-to-folder | Deplace un item dans un dossier | `item_id` (string), `folder_id` (string) |
| list-folder-items | Liste le contenu d'un dossier | `folder_id` (string) |

### Divers (2)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| list-brand-kits | Liste les kits de marque disponibles | aucun |
| resolve-shortlink | Resout un lien court Canva | `shortlink` (string) |

---

## Claude AI Native - Notion MCP (13 outils)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| search | Recherche dans les pages et bases Notion | `query` (string), `filter?` |
| fetch | Recupere le contenu d'une page ou bloc | `page_id` ou `block_id` (string) |
| notion-create-pages | Cree une ou plusieurs pages | `pages` (array), `parent_id` (string) |
| notion-create-database | Cree une nouvelle base de donnees | `parent_id` (string), `title`, `properties` |
| notion-create-view | Cree une vue sur une base de donnees | `database_id` (string), `type`, `filter?`, `sort?` |
| notion-create-comment | Ajoute un commentaire | `page_id` (string), `rich_text` (array) |
| notion-get-comments | Recupere les commentaires d'une page | `page_id` (string) |
| notion-get-users | Liste les utilisateurs du workspace | aucun |
| notion-get-teams | Liste les equipes du workspace | aucun |
| notion-update-page | Met a jour une page (proprietes, contenu) | `page_id` (string), `properties?`, `content?` |
| notion-update-view | Met a jour une vue | `view_id` (string), `filter?`, `sort?` |
| notion-update-data-source | Met a jour une source de donnees | `database_id` (string), `properties` |
| notion-move-pages | Deplace des pages vers un parent | `page_ids` (array), `parent_id` (string) |
| notion-duplicate-page | Duplique une page | `page_id` (string), `title?` |

---

## Claude AI Native - Google Calendar MCP (9 outils)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| gcal_list_calendars | Liste les calendriers disponibles | aucun |
| gcal_list_events | Liste les evenements d'un calendrier | `calendar_id?`, `time_min?`, `time_max?`, `max_results?` |
| gcal_get_event | Recupere les details d'un evenement | `event_id` (string), `calendar_id?` |
| gcal_create_event | Cree un nouvel evenement | `summary`, `start`, `end`, `description?`, `attendees?` |
| gcal_update_event | Met a jour un evenement existant | `event_id` (string), `summary?`, `start?`, `end?` |
| gcal_delete_event | Supprime un evenement | `event_id` (string), `calendar_id?` |
| gcal_respond_to_event | Repond a une invitation (accepter/refuser) | `event_id` (string), `response` (accepted/declined/tentative) |
| gcal_find_meeting_times | Trouve des creneaux communs pour reunion | `attendees` (array), `duration` (minutes) |
| gcal_find_my_free_time | Trouve les creneaux libres de l'utilisateur | `time_min?`, `time_max?`, `duration?` |

---

## Comet MCP (6 outils)

| Outil | Description | Parametres cles |
|-------|-------------|-----------------|
| comet_connect | Connecte au serveur Comet | `url` (string) |
| comet_ask | Envoie une requete au serveur Comet | `prompt` (string) |
| comet_poll | Interroge l'etat du serveur | aucun |
| comet_screenshot | Capture d'ecran via Comet | aucun |
| comet_mode | Change le mode d'operation | `mode` (string) |
| comet_stop | Arrete la connexion Comet | aucun |

---

## Statistiques Globales

| Serveur MCP | Nombre d'outils |
|-------------|-----------------|
| BrowserOS | 58 |
| Claude-in-Chrome | 18 |
| Canva | 28 |
| Notion | 14 |
| Google Calendar | 9 |
| Comet | 6 |
| **Total** | **133** |
