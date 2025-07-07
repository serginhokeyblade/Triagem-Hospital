# Nodo que representa cada estado
class NodoEstado:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# Lista encadeada para cada posição da tabela hash
class ListaEncadeada:
    def __init__(self):
        self.head = None

    # Inserção sempre no início
    def inserir_inicio(self, sigla, nomeEstado):
        novo = NodoEstado(sigla, nomeEstado)
        novo.proximo = self.head
        self.head = novo

    def imprimir_lista(self):
        atual = self.head
        while atual:
            print(f"  - {atual.sigla} ({atual.nomeEstado})")
            atual = atual.proximo

# Tabela Hash com 10 posições
class TabelaHash:
    def __init__(self):
        self.tabela = [None for _ in range(10)]

    # Função hash
    def funcao_hash(self, sigla):
        if sigla.upper() == "DF":
            return 7
        else:
            ascii1 = ord(sigla[0].upper())
            ascii2 = ord(sigla[1].upper())
            return (ascii1 + ascii2) % 10

    # Inserção de estado
    def inserir(self, sigla, nomeEstado):
        posicao = self.funcao_hash(sigla)
        if self.tabela[posicao] is None:
            self.tabela[posicao] = ListaEncadeada()
        self.tabela[posicao].inserir_inicio(sigla, nomeEstado)

    # Impressão da tabela hash
    def imprimir_tabela(self):
        print("\n--- TABELA HASH ---")
        for i in range(10):
            print(f"Posição {i}:")
            if self.tabela[i] is None or self.tabela[i].head is None:
                print("  (vazio)")
            else:
                self.tabela[i].imprimir_lista()

# Lista dos 26 estados e DF
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"),
    ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"),
    ("SC", "Santa Catarina"), ("SP", "São Paulo"), ("SE", "Sergipe"),
    ("TO", "Tocantins"), ("DF", "Distrito Federal")
]

# Estado fictício com seu nome e sigla
estado_ficticio = ("MS", "MÁRIO SÉRGIO CELESTINO DA SILVA")

# Execução e testes
hash_table = TabelaHash()

# Exigência de saída 1: Tabela hash vazia
print("Saída 1: Tabela hash antes das inserções")
hash_table.imprimir_tabela()

# Exigência de saída 2: Inserção dos 27 estados
for sigla, nome in estados:
    hash_table.inserir(sigla, nome)

print("\nSaída 2: Tabela hash após inserção dos 26 estados + DF")
hash_table.imprimir_tabela()

# Exigência de saída 3: Inserção do estado fictício
hash_table.inserir(*estado_ficticio)

print("\nSaída 3: Tabela hash após inserção do estado fictício (MS - MÁRIO SÉRGIO CELESTINO DA SILVA)")
hash_table.imprimir_tabela()
