# Cluster — Dispatch Engine

## Pipeline en 9 Etapes

Le dispatch engine JARVIS route chaque requete a travers un pipeline sequentiel de 9 etapes :

### 1. Cache Check

Verifie si une reponse identique ou similaire existe en cache (SQLite). Hash de la requete + embeddings pour la similarite semantique. Hit rate cible : > 40%.

### 2. Health Check

Interroge chaque noeud du cluster :
- Ping reseau (< 50ms)
- Charge GPU (% utilisation)
- VRAM disponible
- Temperature GPU
- Modeles charges en memoire

### 3. Auto-Load

Si le modele optimal n'est charge sur aucun noeud disponible, declenche un chargement automatique sur le noeud le plus adapte (VRAM libre, temperature basse).

### 4. Route Selection

Applique la matrice de routage (17 domaines x 6 noeuds) pour selectionner le meilleur noeud. Facteurs : poids du noeud, specialite domaine, latence, temperature GPU.

### 5. Prompt Enrichment

Enrichit le prompt avec :
- Contexte utilisateur (historique recent)
- Prefixes modele (`/nothink` pour Qwen3)
- Contraintes de sortie (`max_tokens` pour DeepSeek-R1)
- System prompt adapte au domaine

### 6. Dispatch

Envoie la requete au noeud selectionne via l'API (OpenAI-compatible ou Ollama). Timeout configurable (defaut : 120s).

### 7. Quality Gates

Valide la reponse :
- Longueur minimale (pas de reponse vide)
- Coherence avec la question (embedding similarity > 0.6)
- Absence de patterns d'erreur (hallucinations connues, repetitions)
- Si echec : retry sur un noeud different

### 8. Feedback Loop

Enregistre les metriques :
- Latence totale
- Tokens generes
- Score qualite
- Noeud utilise
- Alimentation de l'auto-apprentissage du routeur

### 9. Post-Processing

- Formatage de la reponse (Markdown, JSON)
- Cache de la reponse pour les requetes futures
- Notification si latence > seuil
- Log dans la base de monitoring
