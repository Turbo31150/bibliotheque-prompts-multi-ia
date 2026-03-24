# Audit Sécurité Docker + GPU (5 Points Critiques)

> 🔵 Bleu — Sécurité, Docker, GPU  
> Source: Perplexity AI (mars 2026)

```text
5 points critiques pour auditer un système IA self-hosted Docker + 6 GPUs:

1. SCAN IMAGES DOCKER: Utiliser Trivy/Snyk sur toutes les images. Les images IA (PyTorch, TensorFlow) contiennent souvent des centaines de CVE. Images minimales (Alpine) préférées.

2. ISOLATION GPU: Limiter l'accès GPU par container (--gpus device=0). Pas de --privileged. Vérifier que les containers ne peuvent pas accéder aux GPUs non autorisés.

3. SECRETS MANAGEMENT: Jamais de clés API dans les images ou docker-compose.yml. Utiliser Docker secrets ou vault. Rotation régulière des tokens.

4. NETWORK SEGMENTATION: Réseau interne pour communication inter-containers. Pas d'exposition ports inutiles. Firewall entre machines du cluster.

5. RUNTIME MONITORING: Surveiller les syscalls suspects (seccomp). Logger tous les accès GPU. Alerter si utilisation anormale (crypto-mining, exfiltration données).

OUTILS: Trivy, Falco, nvidia-smi monitoring, Docker Bench Security
```
