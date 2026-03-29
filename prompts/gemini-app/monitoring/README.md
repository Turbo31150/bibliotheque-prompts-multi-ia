# Gemini App -- Monitoring

## Description

Prompts pour utiliser Gemini App dans la conception de systemes de monitoring, l'analyse de metriques et la creation de dashboards. Gemini App est ideal pour la reflexion sur l'architecture de monitoring et l'interpretation de donnees.

## Cas d'usage
- Conception de strategies de monitoring
- Interpretation de metriques et graphiques
- Creation de requetes PromQL/Grafana
- Definition de SLIs/SLOs/SLAs
- Post-mortem et analyse d'incidents

---

## Prompts prets a copier

### 1 -- Concevoir une strategie de monitoring

```
Concois une strategie de monitoring complete pour cette infrastructure :

## INFRASTRUCTURE
[DECRIRE : serveurs, services, bases de donnees, etc.]

## STRATEGIE A DEFINIR
1. METRIQUES (les 4 Golden Signals par service)
   - Latence
   - Traffic
   - Erreurs
   - Saturation

2. SEUILS D'ALERTE par metrique
   - Warning vs Critique
   - Duree avant declenchement
   - Escalade

3. DASHBOARDS
   - Vue executive (1 ecran, statut global)
   - Vue operationnelle (par service, detail)
   - Vue debug (metriques raw, logs)

4. ON-CALL
   - Runbooks par type d'alerte
   - Arbre de decision (qui appeler quand)
   - SLIs/SLOs pour chaque service

5. OUTILS
   - Stack recommandee (Prometheus, Grafana, Alertmanager...)
   - Configuration de chaque outil
```

---

### 2 -- Ecrire des requetes PromQL

```
Ecris les requetes PromQL pour ces metriques :

1. Taux d'erreur HTTP (5xx) sur les 5 dernieres minutes
2. P95 de latence par endpoint
3. Utilisation CPU moyenne par container
4. Prediction d'espace disque (quand sera-t-il plein ?)
5. Taux de saturation des connexions base de donnees
6. Ratio requetes cache hit vs miss
7. Debit reseau par interface

Pour chaque requete :
- PromQL exact
- Explication de la logique
- Seuils d'alerte recommandes
- Panneau Grafana adapte (type et configuration)
```

---

### 3 -- Analyser un incident post-mortem

```
Redige un post-mortem pour cet incident :

## CHRONOLOGIE
[DECRIRE LES EVENEMENTS]

## METRIQUES PENDANT L'INCIDENT
[COLLER OU DECRIRE LES GRAPHIQUES]

## FORMAT POST-MORTEM
1. RESUME (3 phrases max)
2. IMPACT (utilisateurs affectes, duree, pertes)
3. TIMELINE detaillee (heure par heure)
4. CAUSE RACINE (les 5 pourquoi)
5. CE QUI A BIEN FONCTIONNE
6. CE QUI A MAL FONCTIONNE
7. POINTS DE CHANCE (ce qui aurait pu etre pire)
8. ACTIONS CORRECTIVES
   - Immediates (deja faites)
   - Court terme (cette semaine)
   - Long terme (ce mois)
   Chaque action : responsable, deadline, priorite
9. LECONS APPRISES

Ton : blame-free, factuel, orienté amelioration.
```

---

### 4 -- Definir des SLIs/SLOs

```
Definis les SLIs et SLOs pour ces services :

## SERVICES
[LISTER LES SERVICES]

Pour chaque service :
1. SLIs (Service Level Indicators)
   - Disponibilite : comment la mesurer (requete PromQL)
   - Latence : quels percentiles (p50, p95, p99)
   - Correction : taux de reponses correctes
   - Fraicheur : age des donnees servies

2. SLOs (Service Level Objectives)
   - Objectif par SLI (ex: 99.9% disponibilite)
   - Fenetre de mesure (30 jours glissants)
   - Budget d'erreur calcule
   - Politique quand le budget est epuise

3. ALERTES SLO-based
   - Burn rate alerts (consommation rapide du budget)
   - Multi-window alerts (court terme + long terme)
   - Requetes PromQL pour chaque alerte
```

---

### 5 -- Interpreter des metriques anormales

```
Voici des metriques anormales que j'observe :

[DECRIRE LES METRIQUES : valeurs, tendances, graphiques]

## ANALYSE DEMANDEE
1. Quelles metriques sont reellement anormales vs bruit normal
2. Correlations entre les metriques (cause → effet)
3. Hypotheses de cause racine (3 minimum)
4. Pour chaque hypothese :
   - Metriques supplementaires a verifier
   - Commandes de diagnostic
   - Probabilite estimee
5. Actions recommandees par ordre de priorite
6. Metriques a surveiller dans les prochaines heures
```

---

## Exemples d'utilisation

### Exemple : Requetes PromQL
**Prompt** : "Ecris la requete PromQL pour alerter quand le taux d'erreur 5xx depasse 1% sur 5 minutes."

**Resultat attendu** : `sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) > 0.01` avec explication.

### Exemple : Post-mortem
**Prompt** : "Le service etait down 2h hier. Voici la timeline [coller]. Redige le post-mortem."

**Resultat attendu** : Document post-mortem complet avec actions correctives et responsables.

---

## Effet sur le modele
- Gemini App est efficace pour structurer des strategies de monitoring complexes
- Les prompts avec les 4 Golden Signals cadrent bien l'analyse
- Le format post-mortem blame-free produit des documents constructifs
- Les requetes PromQL generees sont generalement correctes syntaxiquement
