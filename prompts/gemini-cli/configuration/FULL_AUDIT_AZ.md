# ⚡ CONFIGURATION EXHAUSTIVE : GEMINI CLI (A à Z)

Ce document répertorie chaque paramètre vital de l'instance Gemini CLI optimisée pour le Cluster JARVIS.

## ⚙️ PARAMÈTRES RÉSEAU & FLUX
*   **Buffer Size** : 1M+ (Désactivation du rendu incrémental pour flux massifs).
*   **Protocole d'Import** : Namespace virtuel `src` (core + modules).
*   **Timeout Session** : 3600s (Exécutions SRE longues durées).

## 🛡️ PARAMÈTRES DE SÉCURITÉ & YOLO
*   **Mode YOLO** : Activé par défaut (Auto-approbation ROOT).
*   **Permissions** : Sandbox désactivée (Accès physique total aux 5 GPUs).
*   **Persistance** : Checkpointing agressif à chaque étape validée.

## 🧠 PARAMÈTRES COGNITIFS
*   **Fenêtre de Contexte** : 1 048 576 tokens (Ingestion totale du repo 16k fichiers).
*   **Retry Policy** : x5 avec exponentiel backoff en cas d'erreur API.
