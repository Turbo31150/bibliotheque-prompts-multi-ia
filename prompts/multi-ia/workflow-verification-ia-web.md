# Multi-IA — Workflow Verification IA Web

> Pattern async : coller dans IA web → travailler ailleurs → revenir lire apres 1 min.
> Regle : JAMAIS publier sans verification IA web prealable.

---

## Le Pattern en 4 Etapes

### Etape 1 — Coller le contenu dans l'IA web
```bash
# Via CLI dispatch
jai perplexity "Verifie ce pitch freelance : [CONTENU]. Note /10, ameliore."
jai aistudio "Review ces 5 offres : [OFFRES]. Note credibilite prix, ameliore visuel."
```

### Etape 2 — Memoriser ou on a colle
```
# Tab Perplexity : verification pitch
# Tab AI Studio : review offres
```

### Etape 3 — Travailler sur autre chose (~60s)
```bash
# Pendant ce temps, faire du code, du monitoring, etc.
jai m1 "Analyse les logs recents de JARVIS"
```

### Etape 4 — Revenir lire les reponses
```bash
# Via CDP, lire le contenu des tabs
curl -s http://127.0.0.1:9222/json | python3 -c "
import sys,json
for t in json.load(sys.stdin):
    if 'perplexity' in t.get('url','').lower():
        print(f'Perplexity: {t[\"title\"][:60]}')
"
```

## Prompts de verification par type

### Pitch / Profil freelance
```
Verifie ce pitch pour [PLATEFORME]. Note la credibilite /10, ameliore la structure visuelle, corrige le wording. Propose une version amelioree.
```

### Offre / Proposition commerciale
```
Verifie cette offre freelance IA. Note credibilite du prix /10, force de l'argument, structure visuelle. Ameliore le wording, ajoute des elements visuels pour [PLATEFORME].
```

### Post LinkedIn
```
Verifie ce post LinkedIn. Est-il engageant ? Structure visuelle ok ? Hashtags pertinents ? Propose une version amelioree avec meilleur hook.
```

### Code / Architecture
```
Review cette architecture technique. Points forts, faiblesses, suggestions d'amelioration. Note globale /10.
```

## Quand utiliser ce workflow
- Avant TOUTE publication (Codeur, LinkedIn, GitHub)
- Avant toute modification de profil
- Avant tout envoi de proposition client
- Pour valider des decisions techniques importantes
