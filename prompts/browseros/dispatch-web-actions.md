# BrowserOS — Dispatch Actions Web

> 66 outils MCP pour automatisation web.
> Acces : `jai browseros "action"` ou via MCP 127.0.0.1:9000/mcp

---

## Prompt — Publication LinkedIn

```bash
jai browseros "Ouvre LinkedIn, clique Commencer un post, tape ce contenu : [CONTENU]. Screenshot avant publication. ATTENDS confirmation."
```

## Prompt — Reponse Codeur.com

```bash
jai browseros "Ouvre le projet Codeur #[ID]. Clique Repondre. Montant : [MONTANT]. Delai : [JOURS] jours. Message : [PROPOSITION]. Screenshot avant envoi. ATTENDS confirmation."
```

## Prompt — Mise a jour profil

```bash
jai browseros "Ouvre mon profil Codeur (/edit). Remplace la section A propos par : [NOUVEAU_TEXTE]. Sauvegarde. Screenshot de verification."
```

## Prompt — Extraction de donnees

```bash
jai browseros "Ouvre [URL]. Extrais tous les elements [SELECTEUR_CSS]. Retourne en JSON. Sauvegarde dans /tmp/extraction.json."
```

## Prompt — Session web complete

```bash
jai browseros "Pipeline en 4 etapes :
1. Ouvre Codeur.com/projects (tab existant)
2. Extrais les 10 premiers projets IA (titre, budget, nombre offres)
3. Filtre ceux avec budget > 1000 EUR et < 30 offres
4. Sauvegarde dans /tmp/codeur-opportunities.json"
```
