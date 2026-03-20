# OpenClaw -- Securite

## Description

Prompts pour utiliser OpenClaw dans l'audit de securite de code et de configurations avec execution locale.

## Cas d'usage
- Audit de securite de code source
- Verification de configurations
- Detection de secrets commites
- Scan de vulnerabilites de dependances
- Durcissement de fichiers de configuration

---

## Prompts prets a copier

### 1 -- Audit de securite du code

```
Audite le code dans [CHEMIN] pour les vulnerabilites :
- Injection SQL, XSS, SSRF
- Credentials en dur
- Permissions trop larges
- Validation d'entrees manquante
Rapport avec severite et fix pour chaque probleme.
```

### 2 -- Detecter les secrets commites

```
Scanne [CHEMIN] pour les secrets :
- Cles API, tokens, mots de passe
- Fichiers .env commites
- Certificats et cles privees
- URLs avec credentials
Pour chaque secret : fichier, ligne, type, action recommandee.
```

### 3 -- Auditer les configurations

```
Audite les configurations dans [CHEMIN] :
- Docker : images, privileges, volumes
- Nginx/Apache : headers, TLS, permissions
- SSH : authentification, restrictions
- Base de donnees : acces, chiffrement
Score de securite et remediations.
```

### 4 -- Durcir les configurations

```
Durci les configurations dans [CHEMIN] :
1. Lis chaque fichier de configuration
2. Identifie les faiblesses
3. Applique les corrections (avec backup)
4. Verifie que les services fonctionnent encore
```

### 5 -- Scan de dependances

```
Scanne les dependances du projet [CHEMIN] :
- Dependances avec CVE connues
- Dependances obsoletes
- Dependances avec peu de mainteneurs
Rapport avec action recommandee par dependance.
```

---

## Exemples d'utilisation

### Exemple : Secrets
**Prompt** : "Scanne mon repo pour les secrets commites accidentellement"

**Resultat attendu** : Liste des secrets avec fichier, ligne et instruction de nettoyage.

---

## Effet sur le modele
- OpenClaw accede au code reel pour un audit fidele
- L'execution locale permet de tester les corrections immediatement
- La detection de secrets couvre tout l'historique git si necessaire
- Le durcissement avec verification evite de casser les services
