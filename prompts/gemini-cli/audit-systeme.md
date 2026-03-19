# Gemini CLI — Audit Systeme

> Prompts pour realiser des audits systeme complets avec Gemini CLI.

---

## Prompt d'audit complet

```
@gemini Realise un audit systeme complet de cette machine Linux.

Execute et analyse les commandes suivantes :
1. uname -a (kernel et architecture)
2. lscpu (CPU details)
3. free -h (RAM)
4. df -h (disque)
5. nvidia-smi (GPU si disponible)
6. docker ps (containers actifs)
7. systemctl list-units --state=running (services actifs)
8. ss -tlnp (ports ouverts)
9. top -bn1 | head -20 (charge systeme)

Pour chaque categorie, donne :
- Status : OK / WARNING / CRITICAL
- Valeur actuelle vs seuil recommande
- Action corrective si necessaire

Format tableau recapitulatif en fin d'analyse.
```

### Ce que ca fait
Audit exhaustif en une seule commande. Gemini execute les commandes et synthetise les resultats.

### Effet sur le modele
- Le format "execute + analyse" active le mode agent de Gemini
- La classification OK/WARNING/CRITICAL force une evaluation quantitative
- Le tableau final permet une vue d'ensemble rapide

### Exemple de sortie attendue

```
| Composant | Status | Valeur | Seuil | Action |
|-----------|--------|--------|-------|--------|
| CPU | OK | 23% | < 80% | — |
| RAM | WARNING | 78% | < 75% | Fermer processes non-essentiels |
| Disk / | OK | 45% | < 85% | — |
| GPU 0 | OK | 62C | < 75C | — |
| GPU 1 | WARNING | 73C | < 75C | Surveiller |
```

---

## Prompt d'audit securite

```
@gemini Realise un audit securite de cette machine :

1. Utilisateurs avec acces sudo
2. Cles SSH autorisees
3. Ports ouverts accessibles depuis l'exterieur
4. Services avec privileges root
5. Fichiers avec permissions 777
6. Variables d'environnement contenant des tokens/secrets
7. Containers Docker avec --privileged
8. Mise a jour securite en attente

Classe chaque point : SAFE / RISK / CRITICAL
Propose un fix pour chaque RISK et CRITICAL.
```

---

## Prerequis
- Gemini CLI avec acces terminal
- Droits sudo pour certaines commandes d'audit
- nvidia-smi pour l'audit GPU
