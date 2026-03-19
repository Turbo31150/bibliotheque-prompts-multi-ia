# Multi-IA -- Monitoring

## Description

Prompts pour orchestrer plusieurs IA dans le monitoring : combiner les forces de chaque IA (analyse de logs par Claude, recherche de solutions par Perplexity, execution par Gemini CLI) pour un monitoring plus complet.

## Cas d'usage
- Diagnostic multi-IA (analyse + recherche + execution)
- Comparaison des analyses de differentes IA
- Pipeline de monitoring automatise multi-IA
- Validation croisee des alertes
- Post-mortem collaboratif multi-IA

---

## Prompts prets a copier

### 1 -- Pipeline de diagnostic multi-IA

```
## ETAPE 1 : Gemini CLI (collecte)
Execute un diagnostic systeme complet : CPU, RAM, disque, GPU, services, Docker.
Sauvegarde les resultats dans /tmp/diagnostic.json

## ETAPE 2 : Claude (analyse)
Analyse les resultats du diagnostic dans /tmp/diagnostic.json :
- Identifie les anomalies
- Classe par severite
- Propose des hypotheses de cause racine
- Suggere des actions correctives

## ETAPE 3 : Perplexity (recherche)
Pour chaque anomalie identifiee par Claude :
- Recherche si c'est un probleme connu
- Trouve les solutions verifiees
- Verifie les CVE si pertinent

## ETAPE 4 : Claude Code (correction)
Applique les corrections recommandees :
- Genere les scripts de correction
- Execute avec confirmation
- Verifie le resultat
```

---

### 2 -- Validation croisee des analyses

```
Soumets ces metriques aux 3 IA et compare les analyses :

[COLLER LES METRIQUES]

## IA 1 : Claude
"Analyse ces metriques systeme. Identifie les anomalies et propose un diagnostic."

## IA 2 : ChatGPT
"Analyse ces metriques systeme. Identifie les anomalies et propose un diagnostic."

## IA 3 : Gemini
"Analyse ces metriques systeme. Identifie les anomalies et propose un diagnostic."

## SYNTHESE
Comparer les 3 analyses :
- Points d'accord (haute confiance)
- Points de desaccord (investiguer plus)
- Insights uniques de chaque IA
- Diagnostic final consolide
```

---

### 3 -- Post-mortem multi-IA

```
## INCIDENT : [DESCRIPTION]

## ETAPE 1 : Gemini CLI
Collecte les logs, metriques et timeline de l'incident.
Sauvegarde dans ~/postmortem/data/

## ETAPE 2 : Claude
Redige le post-mortem :
- Timeline, cause racine, impact
- 5 Whys analysis
- Actions correctives

## ETAPE 3 : Perplexity
Recherche si l'incident est connu :
- Bugs similaires dans d'autres projets
- Best practices pour eviter la recurrence
- Outils de prevention

## ETAPE 4 : ChatGPT
Redige la communication :
- Message pour l'equipe
- Lecons apprises en format presentation
```

---

### 4 -- Alerting intelligent multi-IA

```
Systeme d'alertes avec validation multi-IA :

## DETECTION (Gemini CLI)
Script de monitoring qui detecte les anomalies.
Quand anomalie detectee → envoyer les donnees aux IA.

## ANALYSE (Claude)
Recevoir les donnees d'anomalie.
Evaluer : vrai positif ou faux positif ?
Si vrai positif : severite et urgence.

## ENRICHISSEMENT (Perplexity)
Rechercher le contexte :
- Bug connu ?
- Maintenance planifiee ?
- Evenement externe (attaque, pic de trafic) ?

## DECISION
Si les 2 IA confirment le probleme → alerte
Si desaccord → escalade pour review humaine
Si faux positif confirme → ajuster les seuils
```

---

### 5 -- Dashboard de sante multi-IA

```
Cree un workflow qui genere un rapport de sante quotidien avec plusieurs IA :

## MATIN (6h) : Gemini CLI
- Collecter toutes les metriques des dernières 24h
- Generer les graphiques (ASCII ou PNG)
- Sauvegarder dans ~/rapports/YYYY-MM-DD/

## MATIN (6h15) : Claude
- Analyser les metriques collectees
- Identifier les tendances (amelioration/degradation)
- Predire les problemes potentiels (disque plein dans X jours, etc.)

## MATIN (6h30) : ChatGPT
- Formater le rapport en format newsletter lisible
- Ajouter des recommandations actionables
- Generer un resume vocal (texte optimise TTS)

## LIVRAISON
- Email du rapport complet
- TTS du resume vocal via jarvis-tts.sh
- Notification desktop
```

---

## Exemples d'utilisation

### Exemple : Diagnostic multi-IA
**Workflow** : Gemini CLI collecte → Claude analyse → Perplexity recherche → Claude Code corrige

**Resultat attendu** : Diagnostic complet avec correction automatique et validation.

---

## Effet sur le modele
- La combinaison de plusieurs IA reduit les angles morts de chaque modele
- La validation croisee augmente la confiance dans les diagnostics
- Chaque IA est utilisee dans son domaine d'excellence
- Le pipeline multi-IA produit des resultats plus fiables qu'une seule IA
