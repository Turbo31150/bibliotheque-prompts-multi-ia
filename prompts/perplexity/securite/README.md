# Perplexity -- Securite

## Description

Prompts pour utiliser Perplexity dans la recherche de vulnerabilites, de solutions de securite et de bonnes pratiques. Perplexity identifie les CVE, les advisories et les recommandations les plus recentes.

## Cas d'usage
- Recherche de CVE et vulnerabilites
- Veille securite (nouvelles menaces)
- Trouver les guides de durcissement officiels
- Comparaison d'outils de securite
- Verification de la securite de dependances

---

## Prompts prets a copier

### 1 -- Rechercher des vulnerabilites

```
Recherche les vulnerabilites connues pour [LOGICIEL] version [VERSION] :

1. CVE listees (NVD, CVE.org)
   - ID CVE, score CVSS, description
   - Exploitabilite (exploit public disponible ?)
   - Correction (version qui corrige)

2. Advisories de securite
   - Advisories du fournisseur
   - Advisories des distributions (Ubuntu, Debian)

3. EVALUATION
   - Risque pour mon cas d'usage : [DECRIRE]
   - Urgence de mise a jour (critique/haute/moyenne/basse)
   - Workaround si mise a jour impossible

Sources avec liens vers les CVE et advisories.
```

---

### 2 -- Veille securite hebdomadaire

```
Resume les evenements de securite informatique de la semaine :

1. VULNERABILITES CRITIQUES
   - Nouvelles CVE avec score >= 8.0
   - Logiciels concernes
   - Exploits publics

2. INCIDENTS
   - Breaches et fuites de donnees
   - Attaques notables (ransomware, supply chain)
   - Reponses des editeurs

3. MISES A JOUR DE SECURITE
   - Patches critiques publies
   - Zero-days corriges

4. OUTILS ET TECHNIQUES
   - Nouveaux outils de securite
   - Nouvelles techniques d'attaque/defense

5. POUR MON HOMELAB
   - Ce que je dois patcher cette semaine
   - Ce que je dois surveiller

Format : newsletter securite, 500 mots.
```

---

### 3 -- Trouver le guide de durcissement officiel

```
Recherche le guide de durcissement officiel pour [OS/LOGICIEL] :

1. Guide CIS Benchmark (Center for Internet Security)
   - Lien vers le PDF
   - Resume des recommandations cles

2. Guide du fournisseur
   - Documentation officielle de securite
   - Checklist de hardening

3. Guides communautaires
   - Blogs tech reconnus
   - Scripts de durcissement (GitHub)

4. SYNTHESE
   - Top 10 des actions les plus impactantes
   - Ordre de priorite
   - Commandes pour chaque action

Sources avec liens directs.
```

---

### 4 -- Comparer les outils de securite

```
Compare les outils de [TYPE : scanner, WAF, IDS, etc.] pour Linux :

## OUTILS A COMPARER
[LISTER OU DEMANDER LES MEILLEURS]

## CRITERES
1. Efficacite (taux de detection, faux positifs)
2. Performance (impact sur le systeme)
3. Installation et configuration
4. Maintenance (mises a jour des signatures)
5. Integration (APIs, alerting, SIEM)
6. Cout (open source vs commercial)
7. Communaute et support

Tableau comparatif avec sources (benchmarks, reviews).
Recommandation pour un homelab / petite infra.
```

---

### 5 -- Verifier la securite d'un projet open source

```
Evalue la securite de ce projet open source avant de l'utiliser :

## PROJET : [NOM / LIEN GITHUB]

## RECHERCHE
1. HISTORIQUE DE SECURITE
   - CVE passees
   - Incidents de securite
   - Temps de correction moyen

2. PRATIQUES DE SECURITE
   - Security policy (SECURITY.md)
   - Bug bounty programme
   - Audits de securite passes
   - Dependabot / renovate active

3. CODE
   - Derniere analyse de securite connue
   - Dependances vulnerables (Snyk, npm audit)
   - Pratiques de code securise

4. CONFIANCE
   - Nombre de mainteneurs
   - Sponsors / backing
   - Historique des contributions
   - Red flags eventuels

Verdict : SECURISE / ACCEPTABLE / RISQUE avec justification.
```

---

## Exemples d'utilisation

### Exemple : CVE check
**Prompt** : "CVE critiques pour OpenSSH 9.6 et Nginx 1.25 cette annee."

**Resultat attendu** : Liste des CVE avec scores, descriptions et versions de correction.

### Exemple : Outil de scan
**Prompt** : "Meilleur scanner de vulnerabilites gratuit pour un homelab Linux en 2026."

**Resultat attendu** : Comparaison de Nessus Essentials, OpenVAS, Trivy avec recommandation.

---

## Effet sur le modele
- Perplexity accede aux bases de CVE en temps reel pour des donnees a jour
- Les liens vers NVD et les advisories sont verifiables
- La veille securite est toujours actuelle grace a la recherche web
- Les comparaisons d'outils s'appuient sur des reviews et benchmarks recents
