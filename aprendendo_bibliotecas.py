#dicionarios


usuarios = {
    'nome': 'André',
    'idade': '47',
    'Departamento': 'TI '
}

usuarios['idade'] = 35
usuarios['nome'] = input('Qual seu nome? ')
print(usuarios)
print(usuarios['idade'])


aluno = {
    'nome': input('Nome do Aluno: '),
    'idade': input('Idade do Aluno: '),
    'nota': input('Nota do Aluno: '),
}

print(f"{aluno['nome']} tem {aluno['idade']} anos de idade e tirou uma nota de {aluno['nota']}!")
