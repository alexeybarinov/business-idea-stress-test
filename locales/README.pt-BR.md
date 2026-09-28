<div align="center">

<img src="../assets/icon.png" alt="Logotipo do Business Idea Stress Test" width="110">

# Business Idea Stress Test

**Coloque sua ideia de negócio à prova antes de investir muito tempo e dinheiro**

Uma habilidade de IA de código aberto para fazer uma **avaliação crítica, pontual e baseada em evidências** de novas ideias de negócio

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[Instalação](../docs/installation.md) · [Primeiros passos](../docs/quickstart.md) · [Versão mais recente](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **Idioma:** esta página está traduzida para português do Brasil. O `SKILL.md` principal está em inglês, mas a habilidade deve responder no idioma do usuário. A documentação técnica detalhada sobre instalação está em inglês

## Para que serve?

Uma ideia pode parecer ótima antes de alguém testar se os clientes realmente pagariam, quais alternativas já utilizam e quanto custa adquirir e atender cada cliente. Este skill não foi feito para concordar automaticamente ou escrever um plano otimista: ele faz perguntas difíceis, busca evidências quando o assistente tem acesso a ferramentas e constrói os argumentos contrários mais relevantes

O objetivo é identificar **o que já foi comprovado, o que ainda é hipótese e qual experimento barato deve vir antes de um investimento maior**

## As seis etapas

1. **Entrevista com o fundador:** perguntas sucessivas sobre problema, cliente pagante, região, orçamento, recursos e limitações
2. **Validação inicial:** hipótese central, alternativas realmente disponíveis e possíveis impedimentos críticos
3. **Pesquisa externa:** demanda, público e concorrentes diretos e indiretos, com fontes e datas quando houver ferramentas adequadas
4. **Análise financeira:** receitas, custos, economia unitária, capital de giro e cenários baseados em premissas explícitas
5. **Revisão adversarial:** objeções dos pontos de vista do comprador, da concorrência, das finanças e das operações
6. **Conclusão condicional:** lacunas de evidência e teste de baixo custo com teto de gastos e critérios de sucesso e interrupção

O skill não substitui entrevistas reais, profissionais especializados ou um painel de modelos independentes. Dados sem confirmação precisam ser identificados como desconhecidos

## Como instalar

**ChatGPT:** baixe o [ZIP oficial da versão mais recente](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) e, caso sua conta tenha acesso a Skills personalizados, abra **Plugins → Skills → Create → Upload from your computer**. Use o ZIP anexado à versão publicada, não o arquivo de código-fonte gerado automaticamente pelo GitHub. A disponibilidade depende do plano e do espaço de trabalho

**Codex:**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

**Claude Code:**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

**Gemini CLI:**

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
```

Para Cursor, Copilot, OpenCode, Claude.ai, instalação manual e atualizações, consulte o [guia completo](../docs/installation.md). `-g` instala para todos os projetos do usuário. Node.js só é necessário para instalar via `npx`, não para executar o skill

## Como começar

Abra uma conversa nova para cada ideia independente. Selecione o skill instalado, quando houver essa opção, e envie:

```text
Use Business Idea Stress Test. Minha ideia de negócio é: [descrição].
Comece me entrevistando, com uma pergunta importante de cada vez.
Questione minhas premissas e destaque a falta de evidências,
sem concordar comigo automaticamente
```

Você pode responder “não sei”. Depois, envie links de concorrentes, notas de entrevistas reais ou cotações de custos que já possui. No final, peça as fontes das conclusões decisivas, cálculos transparentes e um experimento mensurável

**Privacidade:** não compartilhe senhas, listas com dados pessoais de clientes ou informações sigilosas de terceiros sem autorização. Decisões financeiras e jurídicas importantes podem exigir análise profissional

## Versões e agradecimentos

[Histórico de alterações](../CHANGELOG.md) · [Versões](https://github.com/alexeybarinov/business-idea-stress-test/releases). Para atualizar uma instalação global com `npx`: `npx skills update business-idea-stress-test -g`. A instalação manual pode exigir o envio de um novo ZIP

Agradecemos a [Matt Pocock](https://github.com/mattpocock/skills), [BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os), [xcrrr](https://github.com/xcrrr/claude-skills), [Corey Haines](https://github.com/coreyhaines31/marketingskills), [sickn33](https://github.com/sickn33/agentic-awesome-skills) e [jukeyman](https://github.com/jukeyman/jukeyman-skills) pelos projetos que inspiraram este trabalho. Não há afiliação ou endosso por parte dos autores citados. [Créditos completos](../README.md#-standing-on-the-shoulders-of-the-community)

Licença dos arquivos originais: [MIT](../LICENSE)
