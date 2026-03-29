# Gemini App -- Securite

## Description

Prompts pour utiliser Gemini App dans l'analyse de securite, la conception de politiques et l'education aux bonnes pratiques. Gemini App est ideal pour la reflexion strategique sur la securite et la generation de documentation.

## Cas d'usage
- Conception de politiques de securite
- Analyse de risques et menaces
- Formation et sensibilisation securite
- Revue de configurations de securite
- Planification de tests d'intrusion

---

## Prompts prets a copier

### 1 -- Concevoir une politique de securite

```
Redige une politique de securite pour [ORGANISATION/PROJET] :

## SECTIONS
1. OBJECTIFS ET PERIMETRE
2. GESTION DES ACCES
   - Principe du moindre privilege
   - Authentification (MFA, cles SSH, tokens)
   - Revue periodique des acces
3. GESTION DES SECRETS
   - Stockage (vault, variables env, fichiers)
   - Rotation (frequence, procedure)
   - En cas de fuite (procedure d'urgence)
4. RESEAU
   - Segmentation
   - Chiffrement (TLS, VPN)
   - Exposition de services
5. DONNEES
   - Classification (public, interne, confidentiel)
   - Chiffrement au repos et en transit
   - Backup et retention
6. INCIDENTS
   - Detection et reporting
   - Procedure de reponse
   - Communication
7. CONFORMITE
   - Audits periodiques
   - Checklist de verification
```

---

### 2 -- Analyse de risques

```
Realise une analyse de risques pour cette infrastructure :

## INFRASTRUCTURE
[DECRIRE L'INFRASTRUCTURE]

## METHODE : matrice risques
Pour chaque menace identifiee :
| Menace | Probabilite (1-5) | Impact (1-5) | Score | Mitigation |
|--------|-------------------|--------------|-------|------------|

## MENACES A EVALUER
1. Acces non autorise (brute force, credentials volees)
2. Vulnerabilite logicielle (CVE non patchee)
3. Deni de service (DDoS, resource exhaustion)
4. Perte de donnees (corruption, suppression accidentelle)
5. Insider threat (erreur humaine, malveillance)
6. Supply chain (dependance compromise)
7. Physique (panne materielle, catastrophe)

## PLAN DE TRAITEMENT
Par ordre de score decroissant : actions, budget estime, timeline.
```

---

### 3 -- Planifier un test d'intrusion

```
Planifie un test d'intrusion (pentest) pour [CIBLE] :

## SCOPE
- Perimetre : [IPs, domaines, applications]
- Type : black box / grey box / white box
- Duree : [JOURS]

## METHODOLOGIE
1. RECONNAISSANCE
   - OSINT (informations publiques)
   - Scan reseau (nmap)
   - Enumeration des services

2. ANALYSE DE VULNERABILITES
   - Scan automatise (Nessus, OpenVAS)
   - Tests manuels par categorie OWASP

3. EXPLOITATION
   - Tentatives d'exploitation (dans le scope)
   - Escalade de privileges
   - Mouvement lateral

4. POST-EXPLOITATION
   - Evaluation de l'acces obtenu
   - Donnees accessibles
   - Persistance possible

5. RAPPORT
   - Vulnerabilites classees par CVSS
   - Preuves de concept
   - Remediations prioritisees
```

---

### 4 -- Former les equipes a la securite

```
Cree un programme de formation securite pour [AUDIENCE : devs / ops / tous] :

## MODULE 1 : Les bases (1h)
- Les 10 risques OWASP
- Hygiene des mots de passe
- Phishing : comment le detecter
- Quiz interactif

## MODULE 2 : Securite du code (2h)
- Injection SQL, XSS, CSRF
- Validation des entrees
- Gestion des secrets dans le code
- Exercice : trouver les failles dans un code exemple

## MODULE 3 : Securite ops (2h)
- Durcissement serveur
- Configuration firewall
- Gestion des certificats
- Exercice : securiser un serveur vulnerable

## MODULE 4 : Reponse aux incidents (1h)
- Que faire en cas de fuite de credentials
- Procedure en cas de ransomware
- Communication de crise
- Exercice : simulation d'incident

Pour chaque module : slides (contenu), exercice pratique, quiz de validation.
```

---

### 5 -- Revue de configuration de securite

```
Revue ces configurations et identifie les problemes de securite :

[COLLER LES CONFIGURATIONS : nginx, docker-compose, sshd_config, etc.]

## POUR CHAQUE FICHIER
1. Problemes trouves classes par severite
2. Ligne(s) concernee(s)
3. Risque concret (scenario d'exploitation)
4. Configuration corrigee
5. Verification post-correction

## CHECKLIST ADDITIONNELLE
- [ ] Headers de securite HTTP presents
- [ ] TLS 1.2+ uniquement
- [ ] Pas de credentials en dur
- [ ] Permissions fichiers correctes
- [ ] Logging active
- [ ] Rate limiting configure
```

---

## Exemples d'utilisation

### Exemple : Politique de securite
**Prompt** : "Redige la politique de gestion des secrets pour un projet avec Docker, GitHub et 3 serveurs."

**Resultat attendu** : Document de politique avec procedures de stockage, rotation et urgence.

### Exemple : Analyse de risques
**Prompt** : "Mon homelab est expose sur internet avec SSH et un reverse proxy. Analyse les risques."

**Resultat attendu** : Matrice de risques avec scores et plan de mitigation prioritise.

---

## Effet sur le modele
- Gemini App produit des documents de politique structures et complets
- Les matrices de risques avec scores numeriques facilitent la priorisation
- Les programmes de formation incluent des exercices pratiques pertinents
- Les revues de configuration identifient les problemes classiques de maniere fiable
