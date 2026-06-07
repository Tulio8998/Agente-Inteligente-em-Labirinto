import json

code = """
    def calcular_matriz_distancias(self) -> Dict[Tuple[Estado, Estado], float]:
        \"\"\"
        Calcula o custo real do menor caminho entre todos os pontos de interesse 
        (Início, Pontos de Coleta e Objetivo) usando o algoritmo A* já implementado.
        \"\"\"
        pontos = [self.inicio] + self.pontos_coleta + [self.objetivo]
        matriz_distancias = {}
        
        # Salva o estado original para restaurar depois
        inicio_original = self.inicio
        objetivo_original = self.objetivo
        
        for p1 in pontos:
            for p2 in pontos:
                if p1 == p2:
                    matriz_distancias[(p1, p2)] = 0.0
                    continue
                if (p1, p2) in matriz_distancias:
                    continue
                
                # Altera temporariamente o início e o objetivo para usar o A* existente
                self.inicio = p1
                self.objetivo = p2
                
                res = self.busca_astar()
                if res.encontrado:
                    matriz_distancias[(p1, p2)] = res.custo_caminho
                    matriz_distancias[(p2, p1)] = res.custo_caminho
                else:
                    matriz_distancias[(p1, p2)] = math.inf
                    matriz_distancias[(p2, p1)] = math.inf
                    
        # Restaura o estado original do labirinto
        self.inicio = inicio_original
        self.objetivo = objetivo_original
        return matriz_distancias

    def calcular_custo_total_rota(self, rota: List[Estado], matriz_distancias: dict) -> float:
        \"\"\"
        Calcula o custo total C(s) de uma rota de coleta: A -> C_pi(1) -> ... -> C_pi(k) -> B
        \"\"\"
        if not rota:
            return matriz_distancias.get((self.inicio, self.objetivo), math.inf)
            
        custo = matriz_distancias.get((self.inicio, rota[0]), math.inf)
        for i in range(len(rota) - 1):
            custo += matriz_distancias.get((rota[i], rota[i+1]), math.inf)
        custo += matriz_distancias.get((rota[-1], self.objetivo), math.inf)
        return custo

    def obter_vizinhos_busca_local(self, rota_atual: List[Estado], tipo_vizinhanca: str = 'swap') -> List[List[Estado]]:
        \"\"\"
        Gera vizinhos baseados na estratégia escolhida (Justificativa obrigatória no relatório).
        'swap': Troca dois pontos de posição.
        'inverse': Inverte um trecho inteiro da rota.
        \"\"\"
        vizinhos = []
        n = len(rota_atual)
        
        if tipo_vizinhanca == 'swap':
            for i in range(n):
                for j in range(i + 1, n):
                    nova_rota = list(rota_atual)
                    nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
                    vizinhos.append(nova_rota)
                    
        elif tipo_vizinhanca == 'inverse':
            for i in range(n):
                for j in range(i + 2, n + 1):
                    nova_rota = list(rota_atual)
                    nova_rota[i:j] = list(reversed(nova_rota[i:j]))
                    vizinhos.append(nova_rota)
                    
        return vizinhos

    def hill_climbing(self, tipo_vizinhanca: str = 'swap') -> Tuple[List[Estado], float, List[float], int]:
        \"\"\"
        Hill-Climbing para otimização da rota dos pontos de coleta.
        Retorna: melhor rota, melhor custo, histórico de evolução e total de iterações.
        \"\"\"
        import random
        matriz_distancias = self.calcular_matriz_distancias()
        
        if not self.pontos_coleta:
            return [], matriz_distancias.get((self.inicio, self.objetivo), 0.0), [0.0], 0

        # Estado inicial aleatório
        estado_atual = list(self.pontos_coleta)
        random.shuffle(estado_atual)
        custo_atual = self.calcular_custo_total_rota(estado_atual, matriz_distancias)
        
        historico_custo = [custo_atual]
        iteracoes = 0
        
        while True:
            iteracoes += 1
            vizinhos = self.obter_vizinhos_busca_local(estado_atual, tipo_vizinhanca)
            melhor_vizinho = None
            melhor_custo_vizinho = custo_atual
            
            for vizinho in vizinhos:
                custo_viz = self.calcular_custo_total_rota(vizinho, matriz_distancias)
                if sig_viz := custo_viz < melhor_custo_vizinho:
                    melhor_custo_vizinho = custo_viz
                    melhor_vizinho = vizinho
            
            # Se nenhum vizinho melhorou, atingiu mínimo local
            if melhor_custo_vizinho >= custo_atual:
                break
                
            estado_atual = melhor_vizinho
            custo_atual = melhor_custo_vizinho
            historico_custo.append(custo_atual)
            
        return estado_atual, custo_atual, historico_custo, iteracoes

    def simulated_annealing(self, temp_inicial: float = 1000.0, taxa_resfriamento: float = 0.95, 
                            max_iter: int = 1000, tipo_vizinhanca: str = 'swap') -> Tuple[List[Estado], float, List[float], int]:
        \"\"\"
        Simulated Annealing para evitar mínimos locais na rota de coleta.
        Retorna: melhor rota, melhor custo, histórico de convergência e total de iterações executadas.
        \"\"\"
        import random
        matriz_distancias = self.calcular_matriz_distancias()
        
        if not self.pontos_coleta:
            return [], matriz_distancias.get((self.inicio, self.objetivo), 0.0), [0.0], 0

        estado_atual = list(self.pontos_coleta)
        random.shuffle(estado_atual)
        custo_atual = self.calcular_custo_total_rota(estado_atual, matriz_distancias)
        
        melhor_estado = estado_atual
        melhor_custo = custo_atual
        
        T = temp_inicial
        historico_custo = [custo_atual]
        iteracoes = 0
        
        for iteracao in range(max_iter):
            iteracoes += 1
            if T < 1e-4:
                break
                
            vizinhos = self.obter_vizinhos_busca_local(estado_atual, tipo_vizinhanca)
            if not vizinhos:
                break
                
            vizinho_sorteado = random.choice(vizinhos)
            custo_vizinho = self.calcular_custo_total_rota(vizinho_sorteado, matriz_distancias)
            
            delta_c = custo_vizinho - custo_atual
            
            # Critério de aceitação de Boltzmann
            if delta_c < 0 or random.random() < math.exp(-delta_c / T):
                estado_atual = vizinho_sorteado
                custo_atual = custo_vizinho
                
                if custo_atual < melhor_custo:
                    melhor_custo = custo_atual
                    melhor_estado = Point = vizinho_sorteado
            
            historico_custo.append(melhor_custo)
            T *= taxa_resfriamento
            
        return melhor_estado, melhor_custo, historico_custo, iteracoes
"""

lines_to_insert = []
for line in code.split('\n'):
    lines_to_insert.append(line + '\n')
if lines_to_insert[0].strip() == '':
    lines_to_insert = lines_to_insert[1:]
if lines_to_insert[-1].strip() == '':
    lines_to_insert = lines_to_insert[:-1]

with open('labirinto_buscas_2026.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if any('class LabirintoBusca' in s for s in source) and any('def plot_single_search_metrics_batch' in s for s in source):
            insert_idx = -1
            for i, line in enumerate(source):
                if line.startswith('def plot_single_search_metrics_batch'):
                    insert_idx = i
                    break
            
            if insert_idx != -1:
                cell['source'] = source[:insert_idx] + lines_to_insert + source[insert_idx:]
                break

with open('labirinto_buscas_2026.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
