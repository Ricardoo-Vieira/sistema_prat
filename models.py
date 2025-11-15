class Tarefa:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_atual = 1

    def adicionar_tarefa(self, titulo):
        tarefa = Tarefa(self.id_atual, titulo)
        self.tarefas.append(tarefa)
        self.id_atual += 1

    def listar_tarefas(self):
        return self.tarefas
