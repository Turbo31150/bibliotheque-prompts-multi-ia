# Codex CLI -- Migration

## Description

Prompts pour utiliser OpenAI Codex CLI dans les migrations de code, de configurations et de donnees.

## Cas d'usage
- Portage de code entre langages
- Migration de configurations
- Conversion de formats
- Mise a jour de dependances
- Migration de services

---

## Prompts prets a copier

### 1 -- Porter du code

```
Porte [CHEMIN]/*.ps1 de PowerShell en bash.
Conserve la logique, utilise les commandes Linux natives.
Teste chaque script porte.
```

### 2 -- Migrer des configs

```
Convertis les fichiers de configuration dans [CHEMIN]
de [FORMAT A] en [FORMAT B]. Valide la syntaxe.
```

### 3 -- Mettre a jour les dependances

```
Mets a jour les dependances du projet [CHEMIN].
Adapte le code aux breaking changes. Execute les tests.
```

### 4 -- Migrer un service

```
Migre le service [NOM] de [MACHINE A] vers [MACHINE B] :
Export configs, transfert, import, verification.
```

### 5 -- Convertir des donnees

```
Convertis [FICHIER] de [FORMAT A] en [FORMAT B].
Verifie l'integrite (nombre de lignes, checksums).
```

---

## Effet sur le modele
- Codex CLI lit et ecrit les fichiers pour un portage reel
- L'execution des tests valide les migrations
- L'acces SSH potentiel permet les migrations entre machines
