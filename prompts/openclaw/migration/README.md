# OpenClaw -- Migration

## Description

Prompts pour utiliser OpenClaw dans les migrations de code et de configurations avec execution locale et validation.

## Cas d'usage
- Portage de code automatise
- Migration de configurations
- Conversion de formats
- Mise a jour de dependances avec adaptation du code
- Refactoring pour nouvelle architecture

---

## Prompts prets a copier

### 1 -- Porter du code

```
Porte le code dans [CHEMIN] de [LANGAGE A] vers [LANGAGE B] :
1. Lis chaque fichier source
2. Porte en utilisant les idiomes du langage cible
3. Cree les fichiers de configuration du nouveau langage
4. Ecris les tests equivalents
5. Verifie que tout compile/s'execute
```

### 2 -- Migrer des configurations

```
Migre les configurations de [FORMAT A] vers [FORMAT B] :
1. Lis tous les fichiers de config dans [CHEMIN]
2. Convertis chaque fichier
3. Valide la syntaxe
4. Teste que les services fonctionnent avec la nouvelle config
```

### 3 -- Mettre a jour les dependances

```
Mets a jour les dependances du projet [CHEMIN] :
1. Identifie les mises a jour disponibles
2. Pour chaque mise a jour : lis le changelog
3. Adapte le code si breaking changes
4. Execute les tests
5. Rapporte les resultats
```

### 4 -- Refactorer pour nouvelle architecture

```
Refactore le projet [CHEMIN] de [ARCHI A] vers [ARCHI B] :
Exemple : monolithe → modules, callbacks → async/await
1. Planifie les changements
2. Applique module par module
3. Teste apres chaque changement
4. Verifie que le comportement est preserve
```

### 5 -- Convertir des formats de donnees

```
Convertis les fichiers [FORMAT A] en [FORMAT B] dans [CHEMIN] :
1. Lis chaque fichier source
2. Parse et transforme
3. Ecris dans le nouveau format
4. Verifie l'integrite (roundtrip si possible)
```

---

## Exemples d'utilisation

### Exemple : PS → Bash
**Prompt** : "Porte tous les scripts .ps1 dans ~/scripts/ en bash"

**Resultat attendu** : Scripts bash equivalents, testes et fonctionnels.

---

## Effet sur le modele
- OpenClaw lit et ecrit les fichiers directement pour un portage reel
- L'execution des tests valide le portage immediatement
- Le batch processing gere les migrations de projets entiers
- La validation post-migration confirme la parite fonctionnelle
