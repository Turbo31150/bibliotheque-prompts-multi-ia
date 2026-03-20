# BrowserOS - Prompts de Taches

## Sommaire

1. [Extraction de donnees sur un site](#1-extraction-de-donnees-sur-un-site)
2. [Automatiser une routine web](#2-automatiser-une-routine-web)
3. [Verification d'un dashboard / monitoring](#3-verification-dun-dashboard--monitoring)
4. [Recherche web pilotee](#4-recherche-web-pilotee)

---

### 1. Extraction de donnees sur un site

**Contexte** : Besoin de scraper ou extraire des donnees structurees
**Attente** : Plan de navigation, selecteurs, format JSON/tableau
**Quand** : Collecte de donnees, veille, reporting

```text
Tu es un agent navigateur (BrowserOS).
Objectif : extraire <type de donnees> depuis <URL ou site>.

1) Decris le plan de navigation (pages, filtres, pagination).
2) Dis-moi quelles selections tu vas faire (selecteurs, texte des boutons).
3) Donne le format du resultat attendu (JSON / tableau) et remplis-le avec ce que tu trouves.

Previens si tu rencontres des limites (login, anti-bot, captchas).
```

---

### 2. Automatiser une routine web

**Contexte** : Tache repetitive dans un navigateur
**Attente** : Etapes, pseudo-script Playwright, parametres
**Quand** : Export recurrent, verification periodique, workflow web

```text
Agis comme un automate de navigateur.
Routine : "<decris la tache recurrente : exporter un rapport, verifier un dashboard, etc.>".

1) Decompose la routine en etapes claires (URL, actions, temps d'attente).
2) Propose un pseudo-flux ou script (Playwright/Puppeteer ou outil equivalent) pour l'automatiser.
3) Indique ce qui doit etre parametrable (dates, filtres, identifiants).
```

---

### 3. Verification d'un dashboard / monitoring

**Contexte** : Verifier l'etat d'un service via son dashboard web
**Attente** : Etapes, indicateurs cles, rapport d'etat
**Quand** : Check quotidien, incident, monitoring

```text
Tu es BrowserOS.
Tache : verifier l'etat d'un dashboard de monitoring a l'URL <URL>.

1) Indique les etapes (login eventuel, navigation jusqu'au dashboard).
2) Repere les indicateurs cles (latence, erreurs, CPU, etc.).
3) Donne un petit rapport d'etat (OK / A surveiller / Critique) avec ce que tu as vu.
4) Dis quelles alertes automatiques tu mettrais en place a partir de ce dashboard.
```

---

### 4. Recherche web pilotee

**Contexte** : Rechercher et synthetiser des infos sur le web
**Attente** : Navigation, sources reputees, resume structure
**Quand** : Veille techno, benchmark, comparatif

```text
Tu es BrowserOS.
Objectif : trouver et resumer des infos sur "<sujet>" a partir de quelques sites cles.

1) Ouvre un moteur de recherche ou site de docs (au choix).
2) Navigue vers 3-5 sources reputees.
3) Extrait les infos importantes et construis un resume structure.
4) Liste les URL consultees.

Lors de l'exploration, decris brievement tes actions : site, page, ce que tu cherches.
```
