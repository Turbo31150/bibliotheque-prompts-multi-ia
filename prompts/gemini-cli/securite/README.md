# Gemini CLI -- Securite

## Description

Prompts pour utiliser Gemini CLI dans l'audit de securite, le durcissement systeme et la detection d'intrusions. Gemini CLI peut executer des commandes de scan et d'audit directement, permettant une analyse de securite interactive et en temps reel.

## Cas d'usage
- Audit de securite interactif depuis le terminal
- Scan de vulnerabilites avec execution directe
- Durcissement automatise de serveurs Linux
- Analyse de logs d'authentification
- Detection d'anomalies en temps reel

---

## Prompts prets a copier

### 1 -- Audit de securite interactif

```
Lance un audit de securite complet de ce serveur :

1. Verifie la configuration SSH (/etc/ssh/sshd_config)
2. Liste les ports ouverts (ss -tlnp)
3. Verifie les permissions des fichiers sensibles
4. Cherche les binaires SUID/SGID suspects
5. Verifie les mises a jour de securite pendantes
6. Analyse les derniers logs d'authentification
7. Verifie la configuration du firewall
8. Scan les conteneurs Docker pour les images vulnerables

Pour chaque verification :
- Execute la commande
- Analyse le resultat
- Donne un score (passe/echec/warning)
- Propose la remediation si echec

Score global de securite sur 100 a la fin.
```

---

### 2 -- Scanner les ports et services

```
Analyse les ports ouverts sur ce serveur et evalue la surface d'attaque :

1. Execute ss -tlnp et ss -ulnp
2. Pour chaque port ouvert :
   - Service associe
   - Version si detectable
   - Bind address (0.0.0.0 = expose, 127.0.0.1 = local)
   - Risque (faible/moyen/eleve)
   - Justification de l'exposition ou recommandation de fermeture
3. Genere les regles nftables pour n'exposer que le necessaire
4. Identifie les services qui devraient etre en local uniquement
```

---

### 3 -- Analyser les tentatives d'intrusion

```
Analyse les tentatives d'intrusion des dernieres 48h :

1. Parse /var/log/auth.log (ou journalctl -u sshd)
2. Identifie :
   - IPs avec le plus de tentatives echouees
   - Usernames tentes (root, admin, etc.)
   - Heures de pic d'attaques
   - Geolocalisation des IPs (via API ipinfo.io)
3. Verifie si des tentatives ont reussi (connexions inconnues)
4. Genere :
   - Liste d'IPs a bannir
   - Configuration fail2ban adaptee
   - Regles firewall de protection
5. Evalue si le serveur est cible (attaque ciblee vs scan generique)
```

---

### 4 -- Durcir le systeme automatiquement

```
Genere et execute un script de durcissement pour ce serveur Linux :

## ACTIONS (demander confirmation avant chaque action destructive)
1. Desactiver les services inutiles
2. Configurer le firewall (politique deny par defaut)
3. Durcir SSH (cles only, pas de root, port custom)
4. Configurer fail2ban
5. Mettre a jour les paquets de securite
6. Configurer les permissions des fichiers sensibles
7. Activer l'audit (auditd)
8. Configurer les limites de ressources (ulimits)
9. Desactiver les protocoles reseau inutiles (IPv6 si non utilise)
10. Configurer les logs centralises

Pour chaque action : etat avant, commande, etat apres, verification.
```

---

### 5 -- Verifier l'integrite du systeme

```
Verifie l'integrite du systeme pour detecter des modifications suspectes :

1. Comparer les checksums des binaires critiques (/usr/bin, /usr/sbin)
   avec les packages installes (dpkg --verify ou rpm -Va)
2. Chercher les fichiers modifies recemment dans /etc (< 7 jours)
3. Verifier les crontabs de tous les utilisateurs
4. Lister les processus avec des connexions reseau sortantes
5. Chercher les rootkits (rkhunter / chkrootkit)
6. Verifier les modules kernel charges vs autorises
7. Scanner les fichiers web pour les webshells

Rapport avec niveau de confiance et actions recommandees.
```

---

## Exemples d'utilisation

### Exemple : Audit rapide
**Commande** : `gemini "Mon serveur est-il securise ? Fais un audit rapide."`

**Resultat attendu** : Execution des checks de securite avec score et recommandations prioritaires.

### Exemple : Apres un incident
**Commande** : `gemini "J'ai vu une connexion SSH suspecte a 3h du matin. Investigue."`

**Resultat attendu** : Analyse des logs, identification de l'IP, verification des actions effectuees, et remediation.

---

## Effet sur le modele
- Gemini CLI execute les commandes d'audit directement sur le serveur
- L'analyse interactive permet de creuser les anomalies en temps reel
- La confirmation avant actions destructives protege contre les faux positifs
- L'acces aux fichiers systeme permet une analyse complete sans copier-coller
