# Multi-IA -- Securite

## Description

Prompts pour orchestrer plusieurs IA dans l'audit et le renforcement de la securite : scan par Gemini CLI, analyse par Claude, recherche de CVE par Perplexity, et generation de rapports par ChatGPT.

## Cas d'usage
- Audit de securite multi-IA
- Detection de vulnerabilites avec validation croisee
- Reponse aux incidents orchestree
- Durcissement valide par consensus
- Veille securite multi-sources

---

## Prompts prets a copier

### 1 -- Audit de securite multi-IA

```
## Gemini CLI (scan)
Execute un audit de securite du serveur :
- Ports ouverts, services, permissions, SSH, firewall
- Sauvegarder les resultats dans /tmp/audit.json

## Claude (analyse)
Analyse les resultats de l'audit :
- Classe les vulnerabilites par severite
- Propose des remediations
- Score de securite global

## Perplexity (CVE)
Pour chaque service expose :
- Recherche les CVE connues pour cette version
- Verifie si des exploits publics existent
- Recommande les mises a jour

## ChatGPT (rapport)
Redige le rapport d'audit :
- Resume executif
- Vulnerabilites par severite
- Plan de remediation priorise
```

---

### 2 -- Reponse a incident multi-IA

```
## Gemini CLI (collecte)
Collecte les preuves :
- Logs d'authentification
- Processus suspects
- Connexions reseau anormales
- Fichiers modifies recemment

## Claude (analyse)
Analyse les preuves :
- Timeline de l'incident
- Vecteur d'attaque probable
- Impact estime
- Recommandations immediates

## Perplexity (contexte)
Recherche :
- L'IP source est-elle connue (blacklists, threat intel)
- La technique d'attaque est-elle documentee
- D'autres incidents similaires recemment

## ChatGPT (communication)
Redige :
- Rapport d'incident interne
- Communication aux parties affectees si necessaire
- Plan de remediation et prevention
```

---

### 3 -- Durcissement valide par consensus

```
Configuration a durcir : [SERVICE/SYSTEME]

## Claude
"Genere la configuration durcie avec toutes les recommandations de securite."

## ChatGPT
"Revois cette configuration durcie. Identifie les manques et les exces."

## Perplexity
"Recherche le CIS Benchmark officiel pour [SERVICE/VERSION].
La configuration generee est-elle conforme ?"

## Gemini CLI
"Applique la configuration validee. Teste que le service fonctionne.
Verifie que les points de securite sont effectifs."
```

---

### 4 -- Veille securite multi-IA

```
## Perplexity
"CVE critiques de la semaine. Exploits publics. Incidents majeurs."

## Claude
"Pour chaque CVE : suis-je concerne ? (basé sur mon stack : [LISTER])
Priorite de patch. Actions immediates."

## ChatGPT
"Resume en newsletter securite :
- 3 evenements cles
- Actions requises
- Conseils de la semaine"
```

---

### 5 -- Test d'intrusion assiste multi-IA

```
## Perplexity (reconnaissance)
"Recherche les informations publiques sur [DOMAINE/IP].
Technologies detectees, sous-domaines, points d'entree."

## Claude (planning)
"Planifie le test d'intrusion :
- Vecteurs d'attaque a tester
- Outils a utiliser
- Ordre des tests"

## Gemini CLI (execution)
"Execute les tests non destructifs :
- Scan de ports, enumeration
- Test des configurations
- Verification des permissions"

## Claude (rapport)
"Redige le rapport de pentest :
- Vulnerabilites trouvees
- Preuves de concept
- Remediations"
```

---

## Exemples d'utilisation

### Exemple : Audit rapide
**Workflow** : Gemini CLI (scan) → Claude (analyse) → Perplexity (CVE) → ChatGPT (rapport)

**Resultat attendu** : Rapport d'audit complet avec vulnerabilites, CVE et plan de remediation.

---

## Effet sur le modele
- Le scan reel par Gemini CLI donne des donnees factuelles
- L'analyse Claude identifie les risques conceptuels
- Perplexity valide avec les bases de CVE en temps reel
- La combinaison produit un audit plus complet qu'une seule IA
