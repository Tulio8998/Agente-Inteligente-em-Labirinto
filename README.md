# Agente-Inteligente-em-Labirinto

Este Trabalho Prático tem como objetivo desenvolver um agente inteligente capaz de atuar em um labirinto discreto, representado por uma matriz. O mesmo domínio será utilizado para estudar três formas diferentes de resolução de problemas em Inteligência Artificial: **Busca Clássica**, **Busca Local** e **Busca Online**.

---

## 🎯 Etapas do Projeto

O projeto foi dividido em três grandes módulos de complexidade crescente:

### 1. Busca Clássica (Modo Offline)

O agente conhece todo o labirinto (matriz completa) e precisa encontrar o caminho do ponto inicial (`A`) até o objetivo (`B`).

**Algoritmos Implementados:**
- Busca em Largura (BFS)
- Busca em Profundidade (DFS)
- Busca de Custo Uniforme (UCS)
- Busca Gulosa (Greedy)
- A* (A-Estrela)
- Weighted A*
- IDA*

**Heurística:**
- Distância de Manhattan

### 2. Busca Local (Otimização Combinatória)

O labirinto possui múltiplos pontos de coleta obrigatórios (`C`). O problema transforma-se em uma variação do Problema do Caixeiro Viajante (TSP), onde o agente deve descobrir a melhor ordem de visitação para minimizar o custo total.

**Algoritmos Implementados:**
- Hill-Climbing
- Simulated Annealing

**Vizinhança:**
- *Swap* (troca de posições na ordem de visitação)

### 3. Busca Online (Névoa de Guerra)

O agente não conhece o labirinto. Ele possui apenas um "Mapa Interno" vazio e um raio de visão (sensor). Ele deve interagir com um Simulador Real passo a passo.

**Estratégia:**
- Replanning com A* (Replanejamento Contínuo)

**Comportamento:**
- O agente assume que o desconhecido é um caminho livre (*Free-Space Assumption*), planeja a rota, dá um passo e recalcula tudo caso o sensor detecte uma parede inesperada.

---

## 🚀 Como Executar

O projeto foi desenvolvido em Python e estruturado em um *Jupyter Notebook* para facilitar a visualização dos mapas e gráficos.

### Pré-requisitos

- Python 3.x
- Biblioteca `matplotlib`

### Passos para uso (Google Colab ou Jupyter Local)

1. Clone este repositório:

```bash
git clone https://github.com/Tulio8998/Agente-Inteligente-em-Labirinto.git
```

2. Abra o arquivo principal do notebook (`.ipynb`).

3. Execute a **Célula 1** e faça o upload de um dos arquivos `.txt` localizados na pasta `labirintos/`.

4. Execute as células de definição de classes.

5. Vá até a **Célula de Menu** (*Escolher e executar um algoritmo*). O terminal interativo pedirá que você digite um número de **1 a 10** para rodar a simulação desejada:

   - **[1 a 7]**: Buscas Clássicas
   - **[8]**: Executa todos os algoritmos clássicos e gera a tabela comparativa
   - **[9 e 10]**: Buscas Locais (necessário um mapa contendo pontos `C`)

6. Para testar a **Busca Online**, execute a última célula do notebook, que ativará o Simulador Real e a animação do agente descobrindo o mapa.

---

## 📂 Estrutura do Repositório

- `/labirintos`
  - Pasta contendo os mapas de teste nos formatos exigidos (ex.: `42x23`, `101x101`, `Open Battlefield`, etc.)

- `labirinto_buscas_2026.ipynb`
  - Código-fonte completo com a implementação das três partes do projeto.

- `resultados_experimentos.csv`
  - Tabela contendo os dados e métricas extraídos dos experimentos (tempo, nós expandidos, passos, entre outros).

- `uso_ia.md`
  - Arquivo de auditoria detalhando as interações e o suporte de IAs generativas durante o desenvolvimento.

- `Relatorio_Tecnico.pdf`
  - Artigo técnico documentando a modelagem PEAS, formulações matemáticas, equações e análises críticas dos resultados.

---

## 👨‍💻 Autores

Projeto desenvolvido por estudantes da Universidade Federal de Ouro Preto (UFOP) – Campus João Monlevade:

- Emerson Caetano Ataide
- Íthan de Paula Amaral
- Túlio Vilela Lopes