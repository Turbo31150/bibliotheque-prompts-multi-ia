# Claude Code — Securite

## Description
Prompts de securite pour Claude Code : gestion des tokens d'authentification, rate limiting, RBAC (controle d'acces par role), gestion des cles API, configuration HTTPS/TLS et audit de securite.

## Configuration requise
- Claude Code avec plugin `security-auditor`
- Permissions `deny` configurees pour les commandes destructives
- Fichier `.env` avec les secrets (jamais committe)
- HTTPS/TLS pour les endpoints exposes

---

## Prompts par type de tache

### Creation — Systeme d'authentification par tokens

```
Cree un systeme d'authentification par tokens pour l'API JARVIS :

## SPECIFICATION
1. Generation de tokens :
   - JWT (JSON Web Tokens) avec expiration configurable
   - Token de refresh (7 jours)
   - Token d'acces (1 heure)
   - Signature HMAC-SHA256 avec secret rotatif

2. Validation :
   - Middleware FastAPI pour valider chaque requete
   - Verification de l'expiration
   - Verification de la signature
   - Blacklist des tokens revoques

3. Endpoints :
   - POST /auth/login — obtenir un token
   - POST /auth/refresh — renouveler le token
   - POST /auth/revoke — revoquer un token
   - GET /auth/me — info utilisateur courant

4. Securite :
   - Tokens stockes cote client uniquement (stateless)
   - Rate limiting sur /auth/login (5 tentatives/minute)
   - Log de toutes les tentatives de connexion
   - Alerte Telegram sur 3 echecs consecutifs

## IMPLEMENTATION
- Librairie : python-jose pour JWT
- Stockage blacklist : Redis ou SQLite
- Tests : minimum 10 cas (nominal, token expire, token invalide, refresh, revocation)
```

---

### Creation — Rate limiting

```
Implemente un rate limiter pour l'API JARVIS :

## SPECIFICATION
- Algorithme : Token bucket avec sliding window
- Stockage : Redis (ou dictionnaire en memoire si Redis indisponible)

## LIMITES PAR ENDPOINT
| Endpoint | Limite | Fenetre | Burst |
|----------|--------|---------|-------|
| /api/* (general) | 100 req | 1 min | 20 |
| /auth/login | 5 req | 1 min | 0 |
| /trading/* | 30 req | 1 min | 5 |
| /health/* | 300 req | 1 min | 50 |
| /mcp/* | 50 req | 1 min | 10 |

## REPONSE SI LIMITE ATTEINTE
- Status : 429 Too Many Requests
- Headers : X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
- Body : {"error": "rate_limit_exceeded", "retry_after": N}

## IMPLEMENTATION
- Middleware FastAPI
- Cle de rate limiting : IP + token (si authentifie)
- Bypass pour les IPs locales (127.0.0.1, 192.168.1.*)
- Log des IPs qui atteignent les limites
```

---

### Creation — RBAC (Role-Based Access Control)

```
Implemente un systeme RBAC pour JARVIS :

## ROLES
| Role | Description | Permissions |
|------|-------------|------------|
| admin | Acces total | * |
| operator | Operations et monitoring | read, execute, monitor |
| viewer | Lecture seule | read, monitor |
| trading | Operations trading | read, trading.* |
| api | Acces API externe | read, api.* |

## PERMISSIONS GRANULAIRES
- read : lecture des donnees et status
- write : modification des configurations
- execute : execution de commandes et scripts
- monitor : acces aux metriques et dashboards
- trading.scan : scan du marche
- trading.execute : execution de trades
- trading.config : modification parametres trading
- admin.users : gestion des utilisateurs
- admin.config : modification configuration systeme
- admin.destroy : commandes destructives (protege)

## IMPLEMENTATION
- Decorateur @require_permission("trading.execute")
- Verification dans le middleware FastAPI
- Stockage des roles dans SQLite
- Cache des permissions (TTL 5 min)
- Audit log de toutes les actions privilegiees
```

---

### Amelioration / Refactoring — Audit de securite complet

```
Lance un audit de securite complet du projet :

## CHECKLIST
1. SECRETS
   - Recherche de secrets dans le code (tokens, passwords, API keys)
   - Verification que .env n'est pas committe
   - Verification de .gitignore
   - Rotation des secrets expires

2. DEPENDANCES
   - Scan des vulnerabilites connues (pip audit, npm audit)
   - Mise a jour des dependances critiques
   - Verification des licences

3. CONFIGURATION
   - Permissions des fichiers sensibles (600 pour .env, clefs SSH)
   - Ports exposes inutilement
   - Services qui ecoutent sur 0.0.0.0 au lieu de 127.0.0.1
   - CORS trop permissif

4. AUTHENTIFICATION
   - Tokens avec expiration correcte
   - Rate limiting actif
   - Tentatives de brute force detectees
   - Logs d'authentification complets

5. RESEAU
   - HTTPS/TLS pour les endpoints publics
   - Certificats valides et non expires
   - Headers de securite (HSTS, CSP, X-Frame-Options)
   - Firewall configure

## FORMAT DE SORTIE
| Categorie | Issue | Severite | Fix | Status |
|-----------|-------|----------|-----|--------|
```

---

### Debug — Token invalide ou expire

```
Un utilisateur recoit "401 Unauthorized". Diagnostique :

## INFORMATIONS
- Endpoint appele : [URL]
- Token fourni : [OUI/NON]
- Message d'erreur exact : [MESSAGE]

## CHECKLIST
1. Le token est-il present dans le header Authorization ?
2. Le format est-il correct ? (Bearer <token>)
3. Le token est-il decode correctement ? (JWT valide)
4. Le token est-il expire ? (champ exp)
5. La signature est-elle valide ? (secret correct)
6. Le token est-il dans la blacklist ?
7. Le role a-t-il la permission pour cet endpoint ?

## ACTIONS
- Si expire : guider vers /auth/refresh
- Si invalide : verifier la generation du token
- Si blackliste : verifier pourquoi il a ete revoque
- Si permission insuffisante : verifier le role
```

---

### Documentation — Politique de securite

```
Genere la documentation de securite du projet JARVIS :

## FORMAT
### 1. Gestion des secrets
- Ou sont stockes les secrets
- Comment les rotationner
- Procedure en cas de leak

### 2. Authentification
- Flux d'authentification (diagramme)
- Types de tokens et leur duree de vie
- Procedure de revocation

### 3. Autorisation (RBAC)
- Roles disponibles et leurs permissions
- Comment ajouter un nouveau role
- Audit des acces

### 4. Securite reseau
- Ports ouverts et leur justification
- Configuration TLS
- Headers de securite

### 5. Monitoring securite
- Logs a surveiller
- Alertes configurees
- Procedure d'incident
```

---

## Exemples concrets

### Exemple 1 : Audit de securite
```bash
claude "/security"
```

**Resultat attendu** : Tableau avec toutes les issues trouvees, classees par severite, avec fix propose.

### Exemple 2 : Verification des secrets exposes
```bash
claude "Scanne le repo pour les secrets exposes : API keys, tokens, passwords dans le code"
```

**Resultat attendu** : Liste des fichiers contenant des patterns de secrets, avec recommandation de les deplacer dans .env.

### Exemple 3 : Configuration HTTPS
```bash
claude "Configure HTTPS avec Let's Encrypt pour l'API JARVIS sur le port 443"
```

**Resultat attendu** : Script certbot, configuration nginx/caddy, renouvellement automatique, test de la chaine TLS.

---

## Effet sur le modele
- L'audit structure en 5 categories couvre tous les angles de securite
- Les limites de rate limiting explicites evitent les erreurs de configuration
- Le RBAC avec permissions granulaires force une reflexion sur les acces
- Les checklists de debug accelerent le diagnostic des problemes d'auth
- Le modele refuse les commandes dans la liste `deny` des permissions Claude Code
- La separation des secrets dans .env empeche les fuites accidentelles dans le code
