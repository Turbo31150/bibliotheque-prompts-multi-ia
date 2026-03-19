# ChatGPT -- Securite

## Description

Prompts pour utiliser ChatGPT dans l'audit, le renforcement et la surveillance de la securite de systemes Linux, reseaux et applications. ChatGPT aide a identifier les vulnerabilites, generer des configurations securisees et analyser des incidents.

## Cas d'usage
- Audit de securite de serveurs Linux
- Durcissement de configurations (SSH, firewall, services)
- Analyse d'incidents de securite
- Generation de politiques de securite
- Revue de code pour vulnerabilites

---

## Prompts prets a copier

### 1 -- Audit de securite d'un serveur Linux

```
Realise un audit de securite complet pour un serveur Linux (Ubuntu/Debian) :

## CHECKLIST A VERIFIER
1. ACCES
   - Configuration SSH (port, cles, root login, fail2ban)
   - Utilisateurs et groupes (comptes inutiles, privileges sudo)
   - Politique de mots de passe (PAM, complexite, expiration)

2. RESEAU
   - Ports ouverts (justification de chaque port)
   - Firewall (iptables/nftables/ufw : regles)
   - Services exposes (necessaire vs superflu)

3. SYSTEME
   - Mises a jour de securite pendantes
   - Permissions fichiers sensibles (/etc/shadow, /etc/sudoers, cles SSH)
   - SUID/SGID bits injustifies
   - Montages avec noexec, nosuid, nodev

4. APPLICATIONS
   - Docker (socket expose ? images vulnerables ?)
   - Services web (headers de securite, TLS)
   - Bases de donnees (authentification, bind address)

Pour chaque point : commande de verification + resultat attendu + remediation si non conforme.
```

---

### 2 -- Durcir la configuration SSH

```
Genere une configuration SSH durcie (/etc/ssh/sshd_config) pour un serveur de production :

## EXIGENCES
- Authentification par cle uniquement (pas de mot de passe)
- Pas de login root
- Port personnalise
- Limitation des utilisateurs autorises
- Timeout de session
- Limitation des tentatives
- Algorithmes cryptographiques modernes uniquement
- Banner de connexion legal

Fournis :
1. Le fichier sshd_config complet commente
2. Les commandes pour generer les cles ed25519
3. La configuration fail2ban associee
4. Le test de validation (ssh -T)
5. Le rollback en cas de lockout
```

---

### 3 -- Analyser un incident de securite

```
Analyse cet incident de securite et produis un rapport :

## CONTEXTE
[DECRIRE L'INCIDENT : connexion suspecte, fichier modifie, processus inconnu...]

## LOGS
[COLLER LES LOGS PERTINENTS]

## RAPPORT A PRODUIRE
1. TIMELINE : reconstitution chronologique de l'incident
2. VECTEUR : comment l'attaquant est entre (probable)
3. IMPACT : ce qui a ete compromis ou modifie
4. CONTAINMENT : actions immediates pour limiter les degats
5. ERADICATION : nettoyage complet
6. RECOVERY : retour a la normale
7. LESSONS LEARNED : mesures pour empecher la recurrence

Format : rapport structure avec severite (P1/P2/P3/P4).
```

---

### 4 -- Generer des regles firewall

```
Genere un jeu de regles nftables complet pour un serveur qui heberge :
- SSH (port custom [PORT])
- Serveur web (80, 443)
- API interne (port 8080, accessible uniquement depuis le LAN 192.168.1.0/24)
- Prometheus (9090, localhost uniquement)
- Grafana (3000, LAN uniquement)
- Ollama (11434, LAN uniquement)

## REGLES
- Politique par defaut : DROP (input), ACCEPT (output)
- Anti-DDoS : rate limiting sur SSH et HTTP
- Anti-scan : drop des paquets invalides
- Logging des paquets refuses
- Protection contre le spoofing (bogon networks)
- Support IPv6

Fournis les commandes nft + le fichier de persistance.
```

---

### 5 -- Scanner les vulnerabilites d'une application

```
Analyse ce code/cette configuration pour identifier les vulnerabilites de securite :

[COLLER LE CODE OU LA CONFIG]

## ANALYSE DEMANDEE
Pour chaque vulnerabilite trouvee :
1. Type (injection SQL, XSS, SSRF, path traversal, etc.)
2. Severite (CVSS score estime)
3. Ligne(s) concernee(s)
4. Exploit possible (scenario d'attaque)
5. Correction (code corrige)
6. Reference (CWE/OWASP correspondant)

Classe les vulnerabilites par severite decroissante.
```

---

## Exemples d'utilisation

### Exemple : Durcir un serveur frais
**Prompt** : "Je viens d'installer Ubuntu Server 24.04. Donne-moi le script de durcissement initial complet."

**Resultat attendu** : Script bash executant toutes les etapes de hardening (SSH, firewall, updates, permissions, audit).

### Exemple : Analyser des logs suspects
**Prompt** : "J'ai 500 tentatives SSH echouees depuis 3 IPs differentes en 1h. Analyse et recommande."

**Resultat attendu** : Analyse des IPs, configuration fail2ban adaptee, regles firewall, et recommandations de monitoring.

---

## Effet sur le modele
- ChatGPT produit des checklists de securite exhaustives quand on structure la demande par domaine
- Les prompts avec format de rapport (timeline, impact, remediation) donnent des analyses exploitables
- Demander les commandes de verification permet de valider chaque point de l'audit
- Le contexte serveur specifique (Ubuntu, ports, services) genere des regles directement applicables
