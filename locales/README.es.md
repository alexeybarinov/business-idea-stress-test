<div align="center">

<img src="../assets/icon.png" alt="Logotipo de Business Idea Stress Test" width="110">

# Business Idea Stress Test

**Somete tu idea de negocio a una prueba exigente antes de invertir dinero y tiempo**

Una habilidad abierta para asistentes de IA que permite realizar un **análisis crítico y puntual** de una idea empresarial

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[Instalación](../docs/installation.md) · [Primeros pasos](../docs/quickstart.md) · [Última versión](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **Idiomas:** esta página está traducida al español. El archivo principal `SKILL.md` está redactado en inglés, pero la habilidad debe responder en el idioma del usuario. La documentación técnica completa de instalación está en inglés

## ¿Para qué sirve?

Muchas ideas parecen prometedoras antes de verificar si los clientes realmente pagarán, qué alternativas usan hoy, cuánto cuesta adquirirlos y cuáles son los obstáculos para operar. Esta habilidad **no** produce automáticamente un plan optimista: cuestiona las hipótesis, examina pruebas externas cuando dispone de herramientas y plantea la mejor objeción posible a la idea

Su finalidad es determinar **qué se sabe, qué falta demostrar y cuál sería la prueba real menos costosa** antes de comprometer una inversión significativa

## Los seis pasos

1. **Entrevista al fundador:** preguntas consecutivas sobre el problema, el cliente que paga, la zona geográfica, el presupuesto y las limitaciones
2. **Validación inicial:** hipótesis críticas, sustitutos reales y posibles obstáculos decisivos
3. **Investigación externa:** demanda, público objetivo y competencia directa e indirecta, con fuentes y fechas cuando sea posible
4. **Análisis financiero:** ingresos, costes, economía unitaria, liquidez y escenarios ilustrativos con supuestos explícitos
5. **Revisión crítica:** argumentos contrarios desde las perspectivas del comprador, la competencia, las finanzas y las operaciones
6. **Conclusión condicional:** cuestiones pendientes, experimento económico, presupuesto máximo y criterios para continuar o parar

No se hacen entrevistas auténticas ni se consultan varias IA independientes por el mero hecho de activar esta habilidad. Los datos que no se puedan verificar deben quedar identificados como tales

## Instalación

**ChatGPT:** descarga el [ZIP oficial de la última versión](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) y, si tu cuenta permite instalar habilidades, entra en **Plugins → Skills → Create → Upload from your computer**. Descarga el archivo adjunto a la versión, no el ZIP del código fuente generado por GitHub. La disponibilidad depende de la cuenta y del espacio de trabajo

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

Para Cursor, Copilot, OpenCode, Claude.ai, instalación manual y actualizaciones, consulta la [guía completa](../docs/installation.md). La opción `-g` instala la habilidad para todos tus proyectos. Node.js solo es necesario si utilizas `npx` para instalarla; no para ejecutar las instrucciones

## Primer uso

Abre una conversación nueva para cada idea y envía:

```text
Usa Business Idea Stress Test. Mi idea de negocio es: [descripción].
Empieza entrevistándome con una sola pregunta importante cada vez.
Quiero que cuestiones mis hipótesis y señales las pruebas que faltan,
no que apoyes la idea de manera automática
```

Puedes responder «no lo sé» y aportar documentos o enlaces de competidores más adelante. Al final, solicita las fuentes de las afirmaciones principales, los costes expresados con sus fórmulas y un plan de experimentación con criterios de éxito y abandono

**Privacidad:** no compartas contraseñas, datos personales de clientes ni información confidencial de terceros sin autorización. Para decisiones jurídicas o financieras importantes puede ser necesario consultar a un profesional

## Versiones y agradecimientos

[Historial de cambios](../CHANGELOG.md) · [Versiones](https://github.com/alexeybarinov/business-idea-stress-test/releases). Para actualizar una instalación global hecha con `npx`: `npx skills update business-idea-stress-test -g`. Las cargas manuales pueden requerir subir un ZIP nuevo

Gracias a [Matt Pocock](https://github.com/mattpocock/skills), [BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os), [xcrrr](https://github.com/xcrrr/claude-skills), [Corey Haines](https://github.com/coreyhaines31/marketingskills), [sickn33](https://github.com/sickn33/agentic-awesome-skills) y [jukeyman](https://github.com/jukeyman/jukeyman-skills) por las metodologías que inspiraron este proyecto independiente. No existe afiliación ni respaldo de dichos autores. [Agradecimientos completos](../README.md#-standing-on-the-shoulders-of-the-community)

Licencia de los archivos originales del proyecto: [MIT](../LICENSE)
