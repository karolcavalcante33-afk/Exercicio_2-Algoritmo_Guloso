def calcular_troco(quantia, moedas):
    # Ordena as moedas em ordem decrescente para garantir que o algoritmo
    # pegue sempre a maior moeda possível primeiro (estratégia gulosa)
    moedas_ordenadas = sorted(moedas, reverse=True)
    
    resultado = {}
    total_moedas = 0
    
    for moeda in moedas_ordenadas:
        if quantia == 0:
            break
            
        # Quantas moedas desta face cabem na quantia atual?
        quantidade = quantia // moeda
        
        if quantidade > 0:
            resultado[moeda] = quantidade
            total_moedas += quantidade
            # Atualiza o restante da quantia
            quantia %= moeda
            
    return resultado, total_moedas

# Testando com o exemplo da aula:
quantia_exemplo = 18
moedas_disponiveis = [5, 2, 1]

detalhes, total = calcular_troco(quantia_exemplo, moedas_disponiveis)

print(f"Para a quantia de {quantia_exemplo} usando as moedas {moedas_disponiveis}:")
print(f"Número total de moedas utilizadas: {total}")
print("Distribuição das moedas:")
for moeda, qtd in detalhes.items():
    print(f"- {qtd} moeda(s) de R$ {moeda}")