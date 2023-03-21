![logo do projeto](assets/logo.png){ width="300" .center }
# Notas musicais

## Como usar?
Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run escalas
```
Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘

```
## Alteração da tônica da escala

O primeiro parâmentro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala 'F#':

```bash
poetry run escalas
```
Resultado em: 
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```
## Alteração na tonalidade da escala
Você pode alterar a tonalidade da escala também! Esse é o segundo parâmentro da linha de comando. Por exemplo, a escala 'D#' maior:
```bash
poetry run escalas D# maior 
```
Resultado em:
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘

```
## Mais infromações sobre o CLI

Para descobrir outras opções, você pode usar a flag '--help'

```bash
poetry run escalas --help

```

Resultado em:
```bash
Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                                        
                                                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tõnica da escala [default: c]                                       │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified   │
│                                                              shell.                                 │
│                                                              [default: None]                        │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified      │
│                                                              shell, to copy it or customize the     │
│                                                              installation.                          │
│                                                              [default: None]                        │
│ --help                                                       Show this message and exit.            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
