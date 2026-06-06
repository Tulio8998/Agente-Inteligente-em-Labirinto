Aqui está a estrutura do seu arquivo **uso_ia.md** baseada estritamente no que desenvolvemos e resolvemos durante a modelagem, execução do código, montagem dos labirintos e criação dos gráficos (Semana 1).

Pode copiar e salvar como seu arquivo `.md`:

---

# Relatório de Uso de IA - Semana 1

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