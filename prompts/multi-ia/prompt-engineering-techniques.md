# Techniques de Prompt Engineering Avancées

> 🔵 Bleu — IA, analyse, optimisation  
> Référence des techniques pour maximiser la qualité des réponses IA  
> Source: Awesome Prompt Engineering + recherche

## Chain of Thought (CoT)
```text
Résous ce problème étape par étape. Montre ton raisonnement complet avant de donner la réponse finale.

Problème: [description]

Raisonnement:
1. D'abord, j'identifie...
2. Ensuite, j'analyse...
3. Puis je calcule...
4. Donc la réponse est...
```

## Tree of Thoughts (ToT)
```text
Explore 3 approches différentes pour résoudre ce problème. Pour chaque approche:
1. Décris la stratégie
2. Évalue les avantages et inconvénients
3. Score de confiance (0-100%)

Puis choisis la meilleure approche et exécute-la complètement.

Problème: [description]
```

## ReAct (Reasoning + Acting)
```text
Tu dois alterner entre PENSER et AGIR pour résoudre ce problème.

Format:
PENSÉE: [analyse de la situation]
ACTION: [action à prendre]
OBSERVATION: [résultat de l'action]
PENSÉE: [analyse du résultat]
... répéter jusqu'à la solution

Problème: [description]
```

## Self-Consistency
```text
Résous ce problème 3 fois avec des approches différentes. Si les 3 réponses concordent, c'est la bonne. Si divergence, analyse pourquoi et choisis la meilleure.

Approche 1: [méthode directe]
Approche 2: [méthode inverse]
Approche 3: [méthode par analogie]

Consensus: [réponse finale]
```

## Meta-Prompting
```text
Tu es un expert en prompt engineering. Avant de répondre à la question suivante, écris d'abord le prompt optimal que tu utiliserais pour y répondre parfaitement. Puis exécute ce prompt.

Question: [question de l'utilisateur]

Prompt optimal généré:
[ton prompt amélioré]

Exécution:
[réponse basée sur le prompt optimal]
```

## Few-Shot avec Exemples Structurés
```text
Voici des exemples du format attendu:

Input: "Le chat dort sur le canapé"
Output: {"sujet": "chat", "action": "dort", "lieu": "canapé", "sentiment": "neutre"}

Input: "Marie court joyeusement dans le parc"
Output: {"sujet": "Marie", "action": "court", "lieu": "parc", "sentiment": "positif"}

Input: "[nouvelle phrase]"
Output:
```

## Constitutional AI Prompting
```text
Réponds à cette question en suivant ces principes:
1. Être utile et informatif
2. Ne jamais donner de conseils dangereux
3. Admettre les incertitudes
4. Citer les sources quand possible
5. Être respectueux de toutes les perspectives

Si ta réponse viole un principe, reformule-la.

Question: [question]
```

## Skeleton-of-Thought (Parallélisme)
```text
Étape 1: Crée un plan/squelette de la réponse avec les sections principales.
Étape 2: Développe chaque section indépendamment.

Sujet: [sujet]

SQUELETTE:
1. [Section 1]
2. [Section 2]
3. [Section 3]

DÉVELOPPEMENT:
[contenu détaillé pour chaque section]
```
