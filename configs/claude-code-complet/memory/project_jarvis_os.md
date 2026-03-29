---
name: project_jarvis_os
description: JARVIS OS — Ubuntu 24.04 entièrement modifié, 1007 commandes vocales, 16 services, extension GNOME, routines, profils, dashboard web
type: project
---

JARVIS OS — Ubuntu 24.04 transformé. Dernière mise à jour 2026-03-14.

**1007 commandes vocales (5 modules) :**
- Desktop: 614 (apps, JARVIS, GPU, trading, Spotify, Docker, Git, macros, routines, profils, navigateur avancé, multimédia PipeWire, widgets, dashboard, OCR, search IA)
- Fenêtres: 142 (mosaïque 2x2/1+2, swap, opacité, multi-écran)
- Dictée: 107 (dates, templates, navigation paragraphe, sélection)
- Écran: 89 (OCR plein écran, contraste, taille texte, couleur pixel)
- Souris: 55 (scroll H/V, shake, cercle, positions nommées)

**9 couches d'intégration OS :**
1. Boot: Plymouth theme jarvis, GRUB "JARVIS OS"
2. Login: MOTD dynamique, GDM banner, /etc/issue
3. Desktop: Wallpaper HUD dynamique (5min), mode sombre, dock
4. Terminal: Prompt git+venv, 33 aliases j*, CLI `/usr/local/bin/jarvis`
5. Nautilus: 7 scripts clic-droit (IA, transcription, conversion)
6. systemd: jarvis-full.target, 16 services actifs
7. Sons: 6 WAV thème JARVIS
8. Raccourcis: Super+J/D/T/G/W
9. Extension GNOME Shell: jarvis-indicator@turbo (panel GPU/services)

**Fonctionnalités avancées :**
- 6 profils (normal, travail, dev, gaming, veille, présentation)
- 6 routines (matin, soir, bureau, départ, gaming, reset)
- Macros vocales (enregistrer/rejouer séquences)
- Fallback IA conversationnel (Ollama qwen3:1.7b)
- Apprentissage vocal auto (scheduler 6h)
- Dashboard web interactif (port 8088)
- Notification daemon (GPU >75°C, services failed, disk >90%)
- 8 lanceurs dans le menu Applications GNOME
- Wallpaper dynamique (données GPU/cluster temps réel)
- Navigateur avancé (historique, privé, devtools, onglets par numéro)
- Multimédia PipeWire (switch casque/enceintes/HDMI, enregistrement)

**16 services actifs :**
voice, whisper, mcp, brain, trading-sentinel, dashboard-web, dashboard-resilient, gpu-monitor, gpu-fan, gpu-watcher, resource-manager, lmstudio-debugger, turbo-ws, ws, wallpaper, notif-daemon
