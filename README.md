# 🌱 Chunk Generator - Simulação Procedural em Python

Este projeto é uma **simulação experimental de geração procedural de ambiente**, escrita em **Python**.
O sistema cria uma grade de *chunks* (blocos) que representam regiões do mapa, e cada *chunk* recebe valores aleatórios de folhas, alterando sua cor conforme a densidade da vegetação.

A ideia é testar a **lógica por trás da geração de mundos em jogos**, antes de aplicá-la em um projeto maior.

---

## 🧠 Conceito

O programa utiliza **aleatoriedade controlada** para criar pequenas variações visuais e de comportamento em cada *chunk*.
Cada bloco tem informações como:

* `bio`: tipo de bioma (padrão por enquanto)
* `folhasLim`: limite de folhas (quantidade máxima gerada aleatoriamente)
* `range`: coordenadas que definem a área da chunk

A cor de cada *chunk* muda conforme a quantidade de folhas, simulando **densidade de vegetação** — um passo inicial para a criação de biomas procedurais.

---

## ⚙️ Estrutura do Projeto

```
project/
├── main.py             # Arquivo principal (renderização e lógica visual)
├── Translate.py        # Conversor de nomes de chunks para coordenadas
├── ChunkConfig.py      # Geração inicial dos dados das chunks
└── README.md           # Este arquivo
```

---

## 🧩 Funcionamento

1. O arquivo `ChunkConfig.py` cria uma matriz de *chunks* de 16x12, cada uma com:

   * Nome gerado como `x50y50`, `x100y150`, etc.
   * Limite aleatório de folhas (`folhasLim`)
   * Faixa de coordenadas (`range`) para renderização

2. No `main.py`, as *chunks* são desenhadas na tela e coloridas de acordo com o número de folhas.

3. A função `conversorKeyName()` em `Translate.py` interpreta o nome das *chunks* e retorna suas coordenadas (ex.: `"x050y150" → [50, 150]"`).

---

## 🧱 Níveis de Proceduralidade (Planejados)

| Nível                             | Descrição                                                                |
| --------------------------------- | ------------------------------------------------------------------------ |
| **1 - Aleatoriedade simples**     | Cada *chunk* recebe valores totalmente aleatórios (já implementado).     |
| **2 - Correlação local**          | As *chunks* vizinhas passam a influenciar umas às outras (via `anchor`). |
| **3 - Biomas condicionais**       | Regras determinam tipos de biomas com base nos valores locais.           |
| **4 - Geração contextual global** | Uso de *seed* e ruído Perlin/Simplex para criar mundos reproduzíveis.    |

---

## 🧪 Objetivo do Projeto

O propósito principal é **aprender e experimentar os fundamentos da geração procedural** que aparecem em jogos e simulações — como *Minecraft*, *Terraria*, e *No Man’s Sky*.
Com o tempo, o projeto servirá como base para a implementação de **um sistema mais complexo de geração de mundos**.

---

## 💻 Requisitos

* Python 3.10 ou superior
* [Pygame](https://www.pygame.org/docs/)

Instalação:

```bash
pip install pygame
```

---

## 🚀 Execução

Execute o programa principal:

```bash
python main.py
```

A simulação abrirá uma janela mostrando a grade de *chunks*, com cores variando conforme a densidade de folhas.

---

## 🧩 Próximos Passos

* Adicionar sistema de **biomas dinâmicos**.
* Implementar **interação entre chunks vizinhas (anchor)**.
* Criar **semente global (seed)** para geração reproduzível.
* Otimizar a renderização para mundos maiores.

---

## 🧑‍💻 Autor

**Ricardo Henrique**
Explorando lógica de jogos e geração procedural 🌍
📜 Projeto experimental sem fins lucrativos.

---
