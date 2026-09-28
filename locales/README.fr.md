<div align="center">

<img src="../assets/icon.png" alt="Logo de Business Idea Stress Test" width="110">

# Business Idea Stress Test

**Mettez votre idée d'entreprise à l'épreuve avant d'investir beaucoup de temps et d'argent**

Un Agent Skill open source conçu pour réaliser une **évaluation critique ponctuelle et fondée sur des éléments vérifiables**

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[Installation](../docs/installation.md) · [Démarrage rapide](../docs/quickstart.md) · [Dernière version](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **Langue :** cette page est traduite en français. Les instructions centrales de `SKILL.md` sont en anglais, mais le skill doit répondre dans la langue de l'utilisateur. Le guide technique complet d'installation est disponible en anglais

## Pourquoi l'utiliser ?

Une idée peut sembler excellente tant que personne n'a vérifié la volonté de payer, les solutions déjà utilisées par les clients, les coûts d'acquisition ou les risques opérationnels. Ce skill ne rédige pas automatiquement un business plan optimiste : il pose des questions difficiles, cherche des informations externes lorsqu'il dispose d'outils de recherche et examine les meilleurs arguments **contre** votre projet

L'objectif est d'identifier **ce qui est étayé, ce qui reste hypothétique et quel test concret mener à moindre coût** avant un investissement important

## Les six étapes

1. **Entretien avec le porteur de projet :** clarification progressive du problème, des clients payeurs, du territoire, du budget et des contraintes, généralement une question importante à la fois
2. **Validation initiale :** identification de l'hypothèse centrale, des solutions de remplacement et des obstacles potentiellement décisifs
3. **Recherche externe :** analyse de la demande, des clients et de la concurrence directe et indirecte, avec des sources et dates lorsque les outils le permettent
4. **Analyse financière :** revenus, coûts, économie unitaire, besoins de trésorerie et scénarios explicitement conditionnels
5. **Examen contradictoire :** objections des points de vue des clients, des concurrents, des finances et des opérations
6. **Conclusion conditionnelle :** informations manquantes et expérimentation limitée avec budget, critères de réussite et conditions d'arrêt

Le skill ne réalise pas d'entretiens réels sans outils et autorisation, et ne représente pas un comité d'experts indépendants. Les données non vérifiables doivent rester clairement identifiées

## Installer le skill

**ChatGPT :** téléchargez le [ZIP officiel de la dernière version](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest). Si votre compte permet l'ajout de skills, ouvrez **Plugins → Skills → Create → Upload from your computer**. Choisissez le ZIP de la version publiée, pas l'archive source générée automatiquement par GitHub. La disponibilité dépend du compte et de l'espace de travail

**Codex :**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

**Claude Code :**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

**Gemini CLI :**

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
```

Pour Cursor, Copilot, OpenCode, Claude.ai, l'installation manuelle et les mises à jour, consultez le [guide complet](../docs/installation.md). `-g` rend le skill disponible pour tous les projets de votre compte local. Node.js est nécessaire uniquement si vous choisissez l'installation avec `npx`, pas pour exécuter le skill

## Premier essai

Créez une nouvelle conversation pour chaque idée et demandez explicitement :

```text
Utilise Business Idea Stress Test. Voici mon idée : [description].
Commence par m'interroger, une question essentielle à la fois.
Remets en question mes hypothèses et signale les données manquantes
au lieu de valider automatiquement mon projet
```

« Je ne sais pas » est une réponse acceptable. Vous pouvez fournir ensuite des liens vers des concurrents, des entretiens clients existants ou des devis. Demandez à voir les sources, les calculs explicites et un protocole de test concret dans le rapport final

**Confidentialité :** ne communiquez pas de mots de passe ni de données clients confidentielles sans autorisation. Des conseils juridiques ou financiers professionnels peuvent être nécessaires selon les enjeux

## Versions et remerciements

[Journal des versions](../CHANGELOG.md) · [Téléchargements](https://github.com/alexeybarinov/business-idea-stress-test/releases). Mise à jour d'une installation globale `npx` : `npx skills update business-idea-stress-test -g`. Une installation effectuée par ZIP peut nécessiter un nouvel envoi

Merci à [Matt Pocock](https://github.com/mattpocock/skills), [BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os), [xcrrr](https://github.com/xcrrr/claude-skills), [Corey Haines](https://github.com/coreyhaines31/marketingskills), [sickn33](https://github.com/sickn33/agentic-awesome-skills) et [jukeyman](https://github.com/jukeyman/jukeyman-skills) pour leurs travaux inspirants. Ce projet est indépendant et n'est ni affilié à ces auteurs ni approuvé par eux. [Remerciements complets](../README.md#-standing-on-the-shoulders-of-the-community)

Licence des fichiers originaux de ce dépôt : [MIT](../LICENSE)
