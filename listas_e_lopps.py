tarefas = []
continuar = 's'

tarefas.append('Estudar Python com IA')
tarefas.append('Ler um artigo sobre IA')
tarefas.append('Responder emails')

while continuar == 's':
    add = input('Qual tarefa você quer adicionar? ')
    tarefas.append(add)
    print('Minhas tarefas de hoje: ')
    
    for tarefa in tarefas:
        print(f'Tarefa: {tarefa}')
    continuar = input('Ainda quer adicionar algo (s/n) ? ')

print('Você acabou as modificações da lista.')
print('Lista final:')
for tarefa in tarefas:
    print(f'Tarefa: {tarefa}')v
