import random

# Classe Carta
class Carta:
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Valete": 11, "Dama": 12, "Rei": 13, "Ás": 1
    }
    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __str__(self):
        return f"{self.valor} de {self.naipe}"
    
    def obter_valor(self):
        return Carta.valores[self.valor]

# Classe Baralho
class Baralho:
    naipes = ["Paus", "Ouros", "Copas", "Espadas"]
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]
    
    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in self.naipes for valor in self.valores]
    
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def distribuir(self, num_jogadores):
        # Divide as cartas igualmente entre os jogadores
        return [self.cartas[i::num_jogadores] for i in range(num_jogadores)]

# Classe Jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.montante = []
    
    def receber_cartas(self, cartas):
        self.montante.extend(cartas)
    
    def puxar_carta(self):
        return self.montante.pop(0) if self.montante else None
    
    def adicionar_ao_fim(self, cartas):
        self.montante.extend(cartas)
    
    def mostrar_montante(self):
        return len(self.montante)

# Função para o jogo de batalha entre dois jogadores
def jogar_batalha(jogador1, jogador2):
    rodada = 1
    while jogador1.montante and jogador2.montante:
        print(f"\n--- Rodada {rodada} ---")
        pilha_de_batalha = []
        
        # Jogadores puxam uma carta
        carta1 = jogador1.puxar_carta()
        carta2 = jogador2.puxar_carta()
        
        if carta1 and carta2:
            pilha_de_batalha.extend([carta1, carta2])
            print(f"{jogador1.nome} jogou: {carta1} (Valor: {carta1.obter_valor()})")
            print(f"{jogador2.nome} jogou: {carta2} (Valor: {carta2.obter_valor()})")
            
            # Compara valores das cartas
            if carta1.obter_valor() > carta2.obter_valor():
                jogador1.adicionar_ao_fim(pilha_de_batalha)
                print(f"{jogador1.nome} vence a rodada e adiciona {len(pilha_de_batalha)} cartas ao montante.")
            elif carta1.obter_valor() < carta2.obter_valor():
                jogador2.adicionar_ao_fim(pilha_de_batalha)
                print(f"{jogador2.nome} vence a rodada e adiciona {len(pilha_de_batalha)} cartas ao montante.")
            else:
                print("Empate! Continuando a batalha...")
                while True:
                    # Empate: ambos puxam uma nova carta para resolver o empate
                    carta_empate1 = jogador1.puxar_carta()
                    carta_empate2 = jogador2.puxar_carta()
                    
                    if carta_empate1 and carta_empate2:
                        pilha_de_batalha.extend([carta_empate1, carta_empate2])
                        print(f"{jogador1.nome} jogou: {carta_empate1} (Valor: {carta_empate1.obter_valor()})")
                        print(f"{jogador2.nome} jogou: {carta_empate2} (Valor: {carta_empate2.obter_valor()})")
                        
                        if carta_empate1.obter_valor() > carta_empate2.obter_valor():
                            jogador1.adicionar_ao_fim(pilha_de_batalha)
                            print(f"{jogador1.nome} vence o empate e adiciona {len(pilha_de_batalha)} cartas ao montante.")
                            break
                        elif carta_empate1.obter_valor() < carta_empate2.obter_valor():
                            jogador2.adicionar_ao_fim(pilha_de_batalha)
                            print(f"{jogador2.nome} vence o empate e
