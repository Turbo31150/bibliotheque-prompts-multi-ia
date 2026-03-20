# OpenClaw - Developpement

## Vue d'ensemble

Creation d'agents et de skills personnalises pour OpenClaw. Les agents orchestrent les taches IA, les skills leur donnent des capacites concretes.

## Structure d'un agent

Un agent OpenClaw est defini par :

- **Nom** : identifiant unique
- **Modele** : LLM utilise (ollama, lmstudio, jarvis-proxy)
- **System prompt** : instructions de comportement
- **Skills** : liste des fonctions disponibles
- **Outils MCP** : serveurs MCP accessibles

### Creation via API

```bash
curl -X POST http://localhost:28789/api/agents \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "code-reviewer",
    "model": "claude-sonnet",
    "system_prompt": "Tu es un expert en revue de code...",
    "skills": ["git_diff", "code_analysis"],
    "mcp_servers": ["filesystem-mcp"]
  }'
```

## Structure d'une skill TypeScript

```typescript
// skills/example_skill.ts
import { Skill, SkillContext, SkillResult } from "@openclaw/sdk";

export default class ExampleSkill implements Skill {
  name = "example_skill";
  description = "Description de la skill";

  // Parametres acceptes
  parameters = {
    input: { type: "string", required: true, description: "Entree principale" },
    verbose: { type: "boolean", required: false, default: false }
  };

  async execute(ctx: SkillContext): Promise<SkillResult> {
    const { input, verbose } = ctx.params;

    // Logique metier
    const result = await this.process(input);

    if (verbose) {
      ctx.log(`Resultat detaille: ${JSON.stringify(result)}`);
    }

    return { success: true, data: result };
  }

  private async process(input: string): Promise<any> {
    // Implementation
    return { processed: input };
  }
}
```

## Enregistrement d'une skill

```bash
# Copier la skill dans le repertoire
cp my_skill.ts /path/to/openclaw/skills/

# Recharger les skills
curl -X POST http://localhost:28789/api/skills/reload \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"
```

## Bonnes pratiques

- **Un agent = une responsabilite** : eviter les agents fourre-tout
- **Skills atomiques** : chaque skill fait une seule chose bien
- **Gestion d'erreurs** : toujours retourner un `SkillResult` meme en cas d'echec
- **Logs** : utiliser `ctx.log()` pour le debug, pas `console.log`
- **Tests** : ecrire des tests unitaires pour chaque skill avant deploiement

## Cycle de developpement

1. Definir le besoin (quel agent, quelles skills)
2. Creer la skill TypeScript
3. Tester en local
4. Deployer dans OpenClaw (`skills/`)
5. Creer ou mettre a jour l'agent
6. Valider le comportement end-to-end
