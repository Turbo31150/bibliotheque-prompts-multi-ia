# BrowserOS -- Securite

## Description

Prompts pour utiliser BrowserOS MCP dans les tests de securite web : verification de headers, tests XSS, verification SSL et audit de securite front-end.

## Cas d'usage
- Verification des headers de securite HTTP
- Tests d'injection XSS basiques
- Verification de certificats SSL
- Audit de securite front-end
- Detection de mixed content

---

## Prompts prets a copier

### 1 -- Verifier les headers de securite

```
Verifie les headers de securite de [URL] :
1. Content-Security-Policy (present et restrictif ?)
2. X-Frame-Options (DENY ou SAMEORIGIN ?)
3. X-Content-Type-Options (nosniff ?)
4. Strict-Transport-Security (HSTS, max-age ?)
5. X-XSS-Protection
6. Referrer-Policy
7. Permissions-Policy
Rapport : present/absent/valeur pour chaque header.
Score de securite /100.
```

---

### 2 -- Verifier le certificat SSL

```
Verifie le certificat SSL de [URL] :
1. Valide (pas expire ?)
2. Emetteur (CA reconnue ?)
3. Date d'expiration (jours restants)
4. Algorithme de chiffrement
5. Chaine de certificats complete
6. TLS version (1.2 minimum)
Alerte si expiration dans moins de 30 jours.
```

---

### 3 -- Detecter le mixed content

```
Navigue vers [URL] et detecte le mixed content :
1. Charger la page en HTTPS
2. Lister toutes les ressources chargees en HTTP (images, scripts, CSS, iframes)
3. Pour chaque ressource HTTP : URL et type
4. Verifier les sous-pages (liens internes)
Rapport avec liste des ressources a corriger.
```

---

### 4 -- Test XSS basique

```
Teste la resistance aux XSS de [URL] :
1. Identifier les champs de saisie
2. Tester des payloads XSS basiques (non destructifs) :
   - <script>alert(1)</script>
   - <img src=x onerror=alert(1)>
   - "><script>alert(1)</script>
3. Verifier si le payload est execute ou echappe
4. Reporter les champs vulnerables
NOTE : test non destructif uniquement, sur ses propres applications.
```

---

### 5 -- Audit de securite front-end

```
Audit de securite front-end de [URL] :
1. JavaScript : librairies avec CVE connues ?
2. Cookies : flags Secure, HttpOnly, SameSite ?
3. LocalStorage : donnees sensibles stockees ?
4. Formulaires : CSRF token present ?
5. Liens externes : rel="noopener noreferrer" ?
Rapport avec severite par probleme.
```

---

## Exemples d'utilisation

### Exemple : Headers de securite
**Prompt** : "Verifie les headers de securite de mon site https://mon-site.com"

**Resultat attendu** : Rapport avec chaque header, valeur et recommandation.

---

## Effet sur le modele
- BrowserOS verifie la securite comme un vrai navigateur
- Les tests de headers sont non intrusifs et informatifs
- La detection de mixed content previent les failles
- L'audit front-end complete les audits serveur
