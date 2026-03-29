# Gemini App (bureau) - Prompts de Taches

## Sommaire

1. [Recherche technique approfondie](#1-recherche-technique-approfondie)
2. [Design d'interface et UX](#2-design-dinterface-et-ux)
3. [Documentation technique](#3-documentation-technique)
4. [Brainstorming architecture](#4-brainstorming-architecture)

---

### 1. Recherche technique approfondie

**Contexte** : Besoin de comprendre un sujet en profondeur
**Attente** : Synthese structuree, sources, plan
**Quand** : Avant un choix technique, veille

```text
<task>
Sujet de recherche : "<sujet>".
</task>

<instructions>
1) Fais une synthese technique (max 15 phrases).
2) Liste les avantages, inconvenients et pieges.
3) Propose un plan d'implementation concret.
4) Cite tes sources.
</instructions>

<output_format>
## Synthese
## Avantages / Inconvenients
## Pieges courants
## Plan d'implementation
## Sources
</output_format>
```

---

### 2. Design d'interface et UX

**Contexte** : Concevoir une interface utilisateur
**Attente** : Wireframe textuel, composants, flux utilisateur
**Quand** : Nouveau dashboard, UI, page web

```text
<task>
Concevoir l'interface pour : "<description du besoin>".
</task>

<instructions>
1) Identifie les utilisateurs cibles et leurs besoins principaux.
2) Propose un wireframe textuel (layout des composants).
3) Decris le flux utilisateur principal (etapes).
4) Propose les technologies frontend adaptees.
</instructions>
```

---

### 3. Documentation technique

**Contexte** : Ecrire de la documentation pour un projet
**Attente** : Structure claire, exemples, installation
**Quand** : README, guides, API docs

```text
<task>
Ecrire la documentation technique pour : "<projet/module>".
</task>

<instructions>
1) Structure : Introduction / Installation / Usage / API / Exemples / Troubleshooting.
2) Inclus des exemples de code concrets.
3) Ajoute une section FAQ si pertinent.
4) Garde un ton clair et direct.
</instructions>
```

---

### 4. Brainstorming architecture

**Contexte** : Explorer plusieurs approches pour un probleme technique
**Attente** : Options, trade-offs, recommandation
**Quand** : Phase de conception, decision d'architecture

```text
<task>
Brainstorm d'architecture pour : "<objectif>".
</task>

<instructions>
1) Propose 3 architectures differentes (avec noms descriptifs).
2) Pour chaque architecture :
   - Schema haut niveau (composants, flux)
   - Avantages
   - Inconvenients
   - Complexite de mise en oeuvre (faible/moyenne/haute)
3) Recommande celle qui convient le mieux a mon contexte : <contexte>.
</instructions>
```
