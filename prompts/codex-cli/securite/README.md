# Codex CLI -- Securite

## Description

Prompts pour utiliser OpenAI Codex CLI dans l'audit de securite : scan de code, verification de configurations et detection de vulnerabilites.

## Cas d'usage
- Scan de securite du code source
- Audit de configurations serveur
- Detection de secrets commites
- Verification des permissions
- Durcissement automatise

---

## Prompts prets a copier

### 1 -- Audit de securite serveur

```
Audite la securite de ce serveur Linux :
SSH, firewall, ports ouverts, permissions, mises a jour.
Score /100 avec remediations par priorite.
```

### 2 -- Scanner le code

```
Scanne [CHEMIN] pour les vulnerabilites :
Injections, XSS, secrets en dur, permissions.
Rapport avec severite et fix par probleme.
```

### 3 -- Detecter les secrets

```
Cherche les secrets dans [CHEMIN] :
Cles API, tokens, mots de passe, fichiers .env.
Pour chaque : fichier, ligne, type.
```

### 4 -- Durcir SSH

```
Durci la configuration SSH de ce serveur :
Genere sshd_config securise, cles ed25519, fail2ban.
Applique avec backup de l'ancien fichier.
```

### 5 -- Verifier les permissions

```
Verifie les permissions des fichiers sensibles :
/etc/shadow, /etc/sudoers, cles SSH, .env
Corrige les permissions incorrectes.
```

---

## Effet sur le modele
- Codex CLI execute les commandes d'audit directement
- Les corrections sont appliquees avec verification
- L'acces au systeme permet un audit complet et reel
