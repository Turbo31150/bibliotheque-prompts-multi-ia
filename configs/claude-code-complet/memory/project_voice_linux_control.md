---
name: project_voice_linux_control
description: Système de pilotage vocal Linux complet - 898 commandes, 5 modules, routeur avec cache SQL, fallback IA, macros, apprentissage auto, pipeline v3.1 VAD
type: project
---

Pilotage vocal Linux complet, dernière mise à jour 2026-03-14.

**Architecture (898 commandes vocales, 100% tested) :**
- `src/voice_router.py` — routeur unifié, corrections SQL (124), analytics, fallback IA conversationnel
- `src/linux_desktop_control.py` — 505 commandes (apps, fichiers, volume, réseau, BT, services, IA, JARVIS cluster/dashboard, GPU, processus, sécurité, énergie, trading, Spotify, Docker, Git, workflows, productivité, macros, apprentissage vocal)
- `src/voice_window_manager.py` — 142 commandes (fenêtres, menus, workspaces, dialogues, mosaïque 2x2/1+2, swap, opacité)
- `src/voice_dictation.py` — 107 commandes (frappe, NATO, édition, insertion date/heure/signature/template, navigation paragraphe, sélection)
- `src/voice_screen_reader.py` — 89 commandes (titre, clipboard, OCR plein écran, IA vision, contraste, taille texte, couleur pixel)
- `src/voice_mouse_control.py` — 55 commandes (curseur, clics, scroll H/V, grille 3x3, coins, drag, shake, cercle, barre tâches/menu)

**Modules support :**
- `src/db_boot_validator.py` — validation 19 bases SQL au boot (~11ms), préchargement cache vocal
- `src/voice_learning.py` — analyse voice_analytics, auto-suggestion corrections, scheduler 6h
- `src/voice_macros.py` — enregistrement/replay de séquences de commandes, stockage SQL
- `src/voice_pipeline_v3.py` — v3.1: VAD silence, bip succès/erreur, mode continu, notification desktop, retry STT

**Intégrations :**
- `startup_wiring.py` Step 0 → DB validation, Step 2 → scheduler voice_learning
- Fallback IA via Ollama qwen3:1.7b
- 7 bases SQL sauvegardées le 2026-03-14

**Why:** Piloter tout Linux sans clavier ni souris.
**How to apply:** Nouvelles commandes → module approprié. Corrections STT → voice_corrections SQL. Macros → voice_macros SQL.
