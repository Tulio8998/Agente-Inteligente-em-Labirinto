# Relatório de Uso de IA

# Semana 1

## 1. Ferramentas utilizadas

* **Google Gemini**: Utilizado como assistente principal para design de cenários de teste (labirintos), modelagem formal (PEAS), geração de código para visualização de dados (gráficos) e discussão teórica sobre o comportamento dos algoritmos.

## 2. Principais prompts utilizados

* *"Nesse site, ascii-maze-generator, tem esses tipos de shape, maze algorithm e start/exit placement, me ajude a montar uns por esse site para testar os algoritmos."*
* *"Foram esses dados que obitve deles [...] A tabela experimental mínima deve seguir o modelo. O relatório deve responder [questões de análise]."*
* *"Fiz essa correcao e ele continuam dando o mesmo resultado, o arquivo nao alterou mesmo eu copiando e colando oq vc fez, qual foi o erro e onde devo ajustar?"*
* *"Qual tipo de grafico é melhor para meu caso?"*

## 3. Trechos de código sugeridos por IA

A IA foi responsável por sugerir a implementação das funções de visualização gráfica utilizando a biblioteca `matplotlib`. Os principais trechos incorporados ao projeto original foram:

* A função `plot_barras_metricas(resultado)` para plotar as métricas individuais (Passos, Expandidos, Fronteira Máx) de uma única execução.
* A função `plot_linhas_comparativo(lista_resultados)` para plotar o gráfico de divergência entre "Esforço Computacional" (Nós Expandidos) e "Qualidade da Solução" (Passos) na Opção 8 (bateria de testes).

## 4. Sugestões rejeitadas

* A IA sugeriu inicialmente usar gráficos de linha para todas as execuções. A sugestão foi parcialmente rejeitada pois concluiu-se que gráficos de barras são melhores para métricas isoladas categóricas, enquanto os gráficos de linha ficaram restritos apenas à comparação de tendência entre múltiplos algoritmos (Opção 8).

## 5. Erros cometidos pela IA

* **Erro de topologia nos labirintos:** Ao sugerir os mapas `mansion_grid` e `u_trap`, a IA gerou matrizes onde o objetivo (`B`) estava isolado por paredes ou estruturado com falhas de alinhamento (Word Wrap), fazendo com que todos os algoritmos falhassem (retornassem "Não" para Sucesso).
* **Erro de tipagem no código:** A IA sugeriu chamar a função `plot_linhas_comparativo(resultado)` dentro da execução individual (Opções 1 a 7). Como a função esperava uma lista de resultados e recebeu apenas um objeto, o código falhava e não plotava os gráficos.
* **Omissão de importação:** A IA forneceu o código para gerar gráficos assumindo que o ambiente já possuía a biblioteca instalada, resultando no erro `ModuleNotFoundError: No module named 'matplotlib'` ao rodar localmente.

## 6. Como o grupo validou a solução

* **Validação empírica dos labirintos:** Os mapas gerados foram testados no terminal. Ao notar que o agente não achava a saída, analisamos o arquivo `.txt` e identificamos os caracteres desalinhados.
* **Validação teórica das métricas:** Cruzamos os dados das tabelas geradas pelo código com a teoria de Inteligência Artificial. Validamos, por exemplo, que a Busca Gulosa estava realmente expandindo menos nós, que a BFS encontrava caminhos ótimos e que a DFS gerava caminhos excessivamente longos (subótimos) nos mapas abertos (`open_battlefield`).
* **Depuração visual:** Executamos o código no Google Colab e localmente para garantir que as funções do `matplotlib` extraíam exatamente os valores dos atributos da classe `ResultadoBusca`.

## 7. Modificações feitas pelo grupo

* **Correção manual das matrizes:** Refizemos a estrutura dos labirintos de teste (`u_trap_21_9.txt` e `mansion_grid_21_11.txt`), realinhando os caracteres `#` e garantindo um formato perfeitamente retangular no Bloco de Notas sem quebra automática de linha.
* **Ajuste no fluxo do Menu (Célula 4):** Modificamos a estrutura condicional `if/else` para garantir que `plot_barras_metricas` fosse chamado apenas para testes individuais e `plot_linhas_comparativo` fosse chamado apenas para a lista de resultados da Opção 8.
* **Instalação de dependências:** Tivemos que instalar manualmente o pacote `matplotlib` (`pip install matplotlib`) no ambiente virtual local para resolver o erro de compilação.

# Semana 2

## 1. Ferramentas utilizadas

* **Google Gemini**: Utilizado como parceiro de revisão técnica, laboratório de conceitos matemáticos, refinamento da lógica de otimização combinatória (Caixeiro Viajante) e suporte para a formatação da análise crítica de desempenho dos algoritmos.

## 2. Principais prompts utilizados

* *"Analise estes resultados do Hill-Climbing e do Simulated Annealing no mapa 101x101. Por que o Hill-Climbing falhou tanto em achar a melhor rota?"*
* *"Como posso justificar matematicamente no relatório a escolha da vizinhança 'swap' (troca) em vez de gerar permutações totalmente novas a cada iteração?"*
* *"O Simulated Annealing está demorando muito. Como ajusto a temperatura inicial e a taxa de resfriamento para equilibrar o tempo sem perder a chance de escapar de mínimos locais?"*
* *"Ajude-me a formatar as limitações observadas na Busca Local para a sintaxe do LaTeX."*

## 3. Trechos de código sugeridos por IA

A IA foi utilizada principalmente para refinar a lógica matemática de geração de vizinhos e a fórmula de probabilidade. Os principais trechos incorporados/ajustados foram:

* A otimização da função `obter_vizinhos_busca_local`, garantindo que a mutação dos estados (*swap*) fosse feita apenas invertendo dois índices da lista, mantendo o custo de processamento mínimo.
* A implementação da fórmula de probabilidade exponencial de Boltzmann no *Simulated Annealing* (`math.exp(-delta_c / T)`), cruzando-a corretamente com a função `random.random()` para permitir a aceitação de pioras estruturadas.
* O script de "Teste de Estresse e Análise Estatística" (executar os algoritmos 30 vezes e tirar as médias) para comprovar a eficácia das meta-heurísticas de forma científica.

## 4. Sugestões rejeitadas

* A IA sugeriu calcular o caminho real ($A^*$) entre os pontos de coleta *a cada iteração* da Busca Local para garantir precisão absoluta. A sugestão foi **rejeitada** pois isso aumentaria o tempo de processamento exponencialmente. Em vez disso, o grupo optou por pré-calcular uma `matriz_distancias` estática antes de iniciar o loop de otimização, consultando apenas o valor pré-processado (Dicionário $O(1)$) durante as mutações.

## 5. Erros cometidos pela IA

* **Erro de resfriamento (Loop Infinito):** Inicialmente, a IA sugeriu um laço `while T > 0` para a temperatura do *Simulated Annealing*. Como o decaimento era feito por multiplicação (`T *= 0.95`), a variável `T` sofria de limite de precisão de ponto flutuante (*floating-point underflow*) e nunca chegava matematicamente a zero, causando um loop infinito no Jupyter Notebook.
* **Erro de avaliação de vizinhança no SA:** A IA propôs gerar todos os vizinhos possíveis a cada iteração do *Simulated Annealing* (como o Hill-Climbing faz). Isso violava o princípio do algoritmo, que deve avaliar apenas **um** vizinho aleatório por vez para decidir se o aceita ou não.

## 6. Como o grupo validou a solução

* **Validação teórica (Caixeiro Viajante):** Apoiados na teoria de IA, entendemos que o problema de coleta possui complexidade fatorial ($N!$). Validamos a implementação verificando se a rota sugerida no final possuía os pontos mais próximos interligados, evitando cruzamentos no mapa.
* **Depuração da Taxa de Sucesso:** Rodamos baterias de testes (30 execuções). Constatámos matematicamente que o *Hill-Climbing* ficava preso na rota sorteada inicialmente (taxa de sucesso variável), enquanto o *Simulated Annealing*, após o ajuste fino da temperatura, conseguia uma taxa de sucesso muito maior de encontrar o ótimo global.
* **Validação Visual:** Analisamos os gráficos de convergência plotados, atestando visualmente que o *Hill-Climbing* estabilizava cedo (linha reta horizontal logo após a queda), enquanto o *Simulated Annealing* mostrava pequenas "subidas" (aceitação de piora) antes de descer até o vale absoluto.

## 7. Modificações feitas pelo grupo

* **Correção da Temperatura no SA:** Substituímos o laço infinito sugerido pela IA por uma condição de parada segura: adicionamos um limite de iterações (`max_iter`) e uma condição de resfriamento mínimo funcional (`if T < 1e-4: break`).
* **Adaptação para Testes em Lote:** O grupo implementou "cápsulas falsas" (`ResultadoMétricasMédia`) para disfarçar os dados da Busca Local no formato da classe `ResultadoBusca` da Semana 1, permitindo reaproveitar as funções de plotagem gráfica sem precisar reescrever o código do *Matplotlib*.
* **Ajuste Fino de Hiperparâmetros:** Testámos manualmente e fixámos a temperatura inicial e a taxa de resfriamento ($T=1000$, $\alpha=0.95$) para garantir um equilíbrio ótimo entre processamento e qualidade da solução nos labirintos escolhidos.

# Semana 3 

## 1. Ferramentas utilizadas

* **Google Gemini**: Utilizado para implementação da arquitetura da Busca Online (Agente vs Simulador Real), criação das métricas de busca online (Células Reveladas, Replanejamentos), mesclagem avançada de código de Jupyter Notebook via script para resolução de conflitos de Git, e elucidação de dúvidas conceituais sobre estruturas de dados em grafos.

## 2. Principais prompts utilizados

* *"Preciso implementar a Parte IV, a Busca Online. O agente não tem o mapa e precisa explorar. Como separar isso em um Simulador e o conhecimento parcial do Agente?"*
* *"Me sugira uma estratégia de Replanning A*. O agente tenta achar a saída assumindo que o desconhecido está livre e se replaneja quando bater numa parede."*
* *"Como posso gerar gráficos comparando o número de passos reais da busca online com o custo ótimo se o agente conhecesse o mapa todo?"*
* *"Por que tem um a mais do que o total de movimentos e de custo real?"*

## 3. Trechos de código sugeridos por IA

* **Lógica da Busca Online:** Arquitetura base (classes `MapaInterno`, `SimuladorReal`, `AgenteOnline`) e estratégia de `AgenteReplanningAStar`, ajudando a separar a visão restrita do agente do mapa global.
* **Gráficos da Busca Online:** Funções `plot_online_metrics` e `plot_online_metrics_lines` em `matplotlib` para visualização comparativa de Passos Reais vs Custo Ótimo Offline.

## 4. Erros cometidos pela IA e Sugestões Rejeitadas

* **Falta de clareza nas métricas do vetor de caminho:** O código inicial da IA tratava o tamanho do vetor de posições gerado pela Busca Online sem a devida explicação da sua divergência para o custo de deslocamento. **Melhoria sugerida:** Apontei o erro lógico questionando "Por que tem um a mais do que o total de movimentos?", forçando a IA a refinar o output e a fundamentação teórica separando nós (len) de arestas (custo).
* **Poluição do repositório com scripts de teste:** A IA gerou os arquivos `.py` extras (`test_plot.py` e `notebook_code.py`) além de imagens soltas (`test_plot.png`) durante a depuração que sujariam a branch principal do projeto. **Solução Rejeitada:** Rejeitei a ideia de manter esses arquivos auxiliares, instruindo a IA para deletá-los e não subi-los para o remoto.

## 5. Como o grupo validou a solução

* **Teste do Comportamento do Agente Online:** Executamos o labirinto no Jupyter Notebook e acompanhamos os *logs* iterativos para validar que o agente estava realmente parando ao encontrar paredes recém-descobertas (névoa de guerra) e que o gatilho de replanejamento rotas (novo A*) estava sendo acionado perfeitamente.
* **Validação Teórica do Custo em Grafos:** Ao notarmos uma divergência no vetor de caminhos gerado pela Busca Online, questionamos a IA e validamos conceitualmente que o tamanho da lista sempre refletirá o número de *nós* (Custo + 1, pois inclui a raiz), enquanto a métrica reportada na tela é o número de *arestas* (custo real das transições físicas).
* **Verificação Visual da Razão Competitiva:** Conferimos os gráficos gerados (`plot_online_metrics`) validando se as discrepâncias de passos (Online vs Offline) e o número de replanejamentos reportados nas métricas faziam sentido com o excesso de becos sem saída dos labirintos testados.