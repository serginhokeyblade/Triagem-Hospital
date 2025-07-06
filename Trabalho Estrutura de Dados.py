class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        while True:
            cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
            if cor in ["A", "V"]:
                break
            print("Cor inválida. Digite apenas A ou V.")

        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
        else:
            numero = self.contador_amarelo
            self.contador_amarelo += 1

        novo_nodo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo_nodo
        elif cor == "V":
            self.inserirSemPrioridade(novo_nodo)
        else:
            self.inserirComPrioridade(novo_nodo)

        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

    def imprimirListaEspera(self):
        if self.head is None:
            print("A fila está vazia.")
        else:
            atual = self.head
            print("\n--- Lista de Espera ---")
            while atual is not None:
                print(f"Cartão {atual.cor}{atual.numero}")
                atual = atual.proximo
            print("------------------------\n")

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila para atendimento.")
        else:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão {paciente.cor}{paciente.numero} para atendimento.")


# Função principal com menu
def menu():
    fila = ListaEncadeada()

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            fila.inserir()
        elif opcao == "2":
            fila.imprimirListaEspera()
        elif opcao == "3":
            fila.atenderPaciente()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
