# Multi-IA -- Configuration

## Description

Prompts pour orchestrer plusieurs IA dans la configuration de systemes : generation par une IA, validation par une autre, test par une troisieme. Approche defense-en-profondeur appliquee a la configuration.

## Cas d'usage
- Configuration validee par consensus multi-IA
- Generation + revue de fichiers de configuration
- Migration de configurations avec double verification
- Optimisation de configurations existantes
- Documentation automatique des configurations

---

## Prompts prets a copier

### 1 -- Configuration avec validation croisee

```
## ETAPE 1 : Claude Code (generation)
Genere la configuration [TYPE] pour [SERVICE] :
- Fichier de configuration complet
- Commentaires explicatifs
- Valeurs optimisees pour [CONTEXTE]

## ETAPE 2 : ChatGPT (revue securite)
Revois cette configuration pour la securite :
- Credentials en dur ?
- Permissions trop larges ?
- Options dangereuses activees ?
- Best practices manquantes ?

## ETAPE 3 : Perplexity (validation)
Verifie que les options utilisees sont :
- Valides pour la version [VERSION]
- Non depreciees
- Conformes aux recommandations officielles

## ETAPE 4 : Gemini CLI (test)
Applique et teste la configuration :
- Validation syntaxique
- Test de fonctionnement
- Rollback si echec
```

---

### 2 -- Optimisation de configuration existante

```
Configuration actuelle : [COLLER]

## Claude
"Analyse cette configuration et propose des optimisations :
- Performance
- Securite
- Maintenabilite"

## ChatGPT
"Compare cette configuration avec les best practices actuelles.
Identifie les ecarts et propose les corrections."

## Perplexity
"Recherche les recommandations officielles pour [SERVICE] version [VERSION].
Les options obsoletes ou risquees."

## Synthese
Appliquer les optimisations unanimes. Discuter les divergences.
```

---

### 3 -- Documentation de configuration multi-IA

```
## Gemini CLI (collecte)
Liste toutes les configurations actives :
- /etc/ (fichiers modifies)
- Docker configs
- Services systemd
- Crontabs

## Claude (documentation)
Documente chaque configuration :
- Ce qu'elle fait
- Pourquoi elle est configuree ainsi
- Impact si modification

## ChatGPT (guide)
Transforme la documentation en guide operationnel :
- Comment modifier chaque config
- Procedure de test apres modification
- Rollback en cas de probleme
```

---

### 4 -- Migration de configuration

```
## ETAPE 1 : Claude Code
Exporte la configuration de [SERVICE A].
Convertis au format de [SERVICE B].

## ETAPE 2 : ChatGPT
Valide la conversion :
- Toutes les options sont-elles mappees ?
- Les valeurs sont-elles equivalentes ?
- Des options manquent-elles dans la cible ?

## ETAPE 3 : Perplexity
Recherche les differences de comportement entre A et B :
- Options avec le meme nom mais un comportement different
- Valeurs par defaut differentes
- Fonctionnalites absentes

## ETAPE 4 : Gemini CLI
Deploie et teste la nouvelle configuration.
Compare le comportement avant/apres.
```

---

### 5 -- Troubleshooting de configuration

```
Probleme : [DESCRIPTION DU PROBLEME LIE A LA CONFIG]

## Claude
"Analyse la configuration [COLLER] et identifie les erreurs potentielles."

## ChatGPT
"Quelles sont les causes courantes de [PROBLEME] avec [SERVICE] ?
Quelles options de configuration sont generalement en cause ?"

## Perplexity
"Recherche ce probleme specifique : [ERREUR EXACTE].
Solutions verifiees et configurations correctes."

## Synthese
Corriger en priorite les causes identifiees par les 3 IA.
```

---

## Exemples d'utilisation

### Exemple : Config Nginx
**Workflow** : Claude Code (genere) → ChatGPT (revue secu) → Perplexity (valide options) → Gemini CLI (teste)

**Resultat attendu** : Configuration Nginx validee, securisee et testee.

---

## Effet sur le modele
- La validation croisee elimine les erreurs de configuration
- Chaque IA apporte un angle different (generation, securite, conformite, test)
- Le test final par Gemini CLI valide dans le contexte reel
- Les configurations multi-IA validees sont plus fiables
