# ChatGPT — Guide complet

> OpenAI ChatGPT : configuration, Custom Instructions, GPTs, plugins et bonnes pratiques.

---

## Modèles disponibles

| Modèle | Vitesse | Capacité | Usage recommandé |
|---|---|---|---|
| **GPT-4o** | Rapide | Multimodal (texte, image, audio) | Usage principal, raisonnement avancé. |
| **GPT-4o mini** | Très rapide | Texte uniquement | Tâches simples, classement, tri. |
| **o1** | Lent | Raisonnement profond | Mathématiques, logique complexe, planification. |
| **o3** | Lent | Raisonnement expert | Problèmes scientifiques, architecture. |

## Custom Instructions

Les Custom Instructions définissent le comportement par défaut de ChatGPT pour toutes les conversations.

### Ce qu'il faut y mettre

```
Rôle : Développeur senior Python/TypeScript, expert Linux et IA.
Langue : Français pour les explications, anglais pour le code.
Style : Concis, direct, pas de bavardage.
Format : Code avec commentaires, tableaux pour les comparaisons.
Contraintes : Toujours proposer des tests, mentionner les edge cases.
```

### Ce qu'il ne faut pas y mettre
- Des instructions trop longues (limite de tokens).
- Des informations changeantes (utiliser la mémoire à la place).

## GPTs personnalisés

Créer un GPT spécialisé pour chaque domaine :

| GPT | Rôle | Instructions clés |
|---|---|---|
| **JARVIS Dev** | Développement JARVIS | Connaît l'architecture, les modules, les contraintes GPU. |
| **Trading Analyst** | Analyse technique | Formules, indicateurs, gestion du risque. |
| **Code Reviewer** | Review de code | Checklist qualité, sécurité, performance. |
| **Doc Writer** | Documentation | Style technique, structure, exemples. |

## Mémoire

ChatGPT peut retenir des informations entre les conversations :
- Dire : *« Retiens que je travaille sur JARVIS, un cluster IA de 3 machines. »*
- Vérifier : *Paramètres → Personnalisation → Mémoire*
- Supprimer : *« Oublie l'information sur X. »*

## Bonnes pratiques

1. **Structurer les prompts** : contexte → objectif → contraintes → format attendu.
2. **Utiliser les artefacts** : demander du code dans un artefact pour pouvoir le copier proprement.
3. **Itérer** : un premier prompt large, puis affiner avec des follow-ups.
4. **Joindre des fichiers** : uploader le code source plutôt que le coller (meilleure compréhension).
5. **Comparer les modèles** : utiliser GPT-4o pour le draft, o1 pour la vérification logique.
