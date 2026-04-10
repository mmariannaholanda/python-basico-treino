# aprendendo classes primeiro 

class Casa:
    def __init__(self, cor, quartos):
        self.cor = cor
        self.quartos = quartos

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')

casa1 = Casa('Azul', 4)
casa2 = Casa('Amarela', 6)

print('\nCasa 1:')
casa1.mostrar_cor()
print('\nCasa 2:')
casa2.mostrar_cor()


#aprendendo heranças

class Animais:
  def __init__(self, nome, cor, tipo, especie):
    self.nome = nome
    self.cor = cor
    self.tipo = tipo
    self.especie = especie
  def apresentar(self):
    print (f' {self.nome}\n {self.cor}\n {self.tipo} da espécie {self.especie}')

class Gato(Animais):
  def emitirSom(self):
    print(' Miau!\n')
class Cachorro(Animais):
  def emitirSom(self):
    print(' Au Auu!!\n')


a = Cachorro('Brownie','Chocolate','Cachorro','ShitZu')
a.apresentar()
a.emitirSom()

b = Gato('Flora','Preta','Gato','Siamês')
b.apresentar()
b.emitirSom()

# outro exemplo de treino

class Pessoa:
  def __init__ (self,nome,idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    print(f'{self.nome}, {self.idade} de idade')

class Funcionario(Pessoa):
  def __init__ (self,nome,idade,cargo):

    # na função super(). se puxa parametros de uma outra classe,
    # mesmo que tenha a herança, precisa puxar para ad outro parametro

    super().__init__(nome,idade)
    self.cargo = cargo

  def apresentar(self):
    print(f'{self.nome} tem {self.idade} de idade\nTrabalha no cargo {self.cargo}')


class Cliente(Pessoa):
  def __init__ (self,nome,idade,saldo):
    super().__init__(nome,idade)
    self.saldo = int(saldo)
  
  def comprar(self):
    compra = int(input(f'Qual o valor da compra que a {self.nome} quer fazer? '))
    if compra <= self.saldo:
      sobra = self.saldo - compra
      print(f'Compra aprovada, ainda resta {sobra} reais de saldo.')

    else:
      print('Saldo insuficiente.')

f1 = Funcionario('Marianna','19','Dev Júnior')
f1.apresentar()

c1 = Cliente('Raquel','42','420 ')
c1.apresentar()
c1.comprar()


# aprendendo herança múlltipla

# Classes Pai:
class Predador():
    def cacando(self):
        print('Este animal está caçando!')

class Presa():
    def fugindo(self):
        print('Este animal está sendo caçado!')

# Classes Filho
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass


coelho1 = Coelho()
tigre1 = Tigre()
golfinho1 = Golfinho()

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()

# promovendo para multinível


# Herança Multipla

# classe Avo

class Animal:
  def __init__(self,nome):
    self.nome = nome 


# Classes Pai:
class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} está caçando!')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está sendo caçado!')

# Classes Filho
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass


coelho1 = Coelho('Bark')
tigre1 = Tigre('Bow')
golfinho1 = Golfinho('Flora')

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()

#trabalhando mais com o super

# Sistema de Escola

class Escola():
  def __init__(self, nome, idade, status):
    self.nome = nome
    self.idade = idade
    self.status = status

  def Apresentar(self):
    print(f'Meu nome é {self.nome}')

  def verificar_status(self):
    print(f'Status: {"ATIVO" if self.status == 'ativo' or 'Ativo' else "INATIVO"}')


class Aluno(Escola):
  def __init__(self, nome, idade, status, ano):
    super().__init__(nome, idade, status)
    self.ano = ano

  def Apresentar(self):
    super().Apresentar()
    print(f'Eu sou um aluno da escola, meu nome é {self.nome}', tenho {self.idade} e sou do {self.ano} ano)


class Professor(Escola):
  def __init__(self, nome, idade, status, materia):
    super().__init__(nome, idade, status)
    self.materia = materia

  def Apresentar(self):
    super().Apresentar()
    print(f'Eu sou um professor da escola, meu nome é {self.nome}, tenho {self.idade} anos e sou professor(a)  da matéria de {self.materia}')

class Assistente(Escola):
  def __init__(self, nome, idade, status, bloco):
    super().__init__(nome, idade, status)
    self.bloco = bloco

  def Apresentar(self):
    super().Apresentar()
    print(f'Eu sou um(a) assistente da escola, meu nome é {self.nome}, tenho {self.idade} anos e trabalho no blo {self.bloco}')

a1 = Aluno(nome='Marcos', idade=12, status=True, ano=8)
p1 = Professor(nome='Roberto', idade=34, status=True, materia='Geometria')
as1 = Assistente(nome='Ana Maria', idade=29, status=False, bloco='Bloco C')

p1.Apresentar()
p1.verificar_status()

as1.Apresentar()
as1.verificar_status()







#DESAFIO BIBLIOTECA ------------------------------------------------------------- 

class Livros:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero.lower()


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.romances = []
        self.fantasia = []
        self.ficcao = []
        self.suspense = []
        self.terror = []
        self.acao = []

    def add_livro(self, livro):
        self.livros.append(livro)

        if livro.genero == 'fantasia':
            self.fantasia.append(livro)

        elif livro.genero == 'romance':
            self.romances.append(livro)

        elif livro.genero == 'ficcao':
            self.ficcao.append(livro)

        elif livro.genero == 'suspense':
            self.suspense.append(livro)

        elif livro.genero == 'terror':
            self.terror.append(livro)

        elif livro.genero == 'acao':
            self.acao.append(livro)





    def listar_livros(self):
        for livro in self.livros:
            print(f'{livro.nome} - Gênero: {livro.genero}')



    def generos(self):
        pesquisar = True

        while pesquisar:
            print('\nQuer algum gênero específico?')
            preferencia = input('').lower()
            print()
            if preferencia == 'romance':
                print('Livros de romance:')
                for livro in self.romances:
                    print(f'Nome: {livro.nome}')

            elif preferencia == 'fantasia':
                print('Livros de fantasia:')
                for livro in self.fantasia:
                    print(f'Nome: {livro.nome}')

            elif preferencia == 'ficcao':
                print('Livros de ficção:')
                for livro in self.ficcao:
                    print(f'Nome: {livro.nome}')

            elif preferencia == 'suspense':
                print('Livros de suspense:')
                for livro in self.suspense:
                    print(f'Nome: {livro.nome}')

            elif preferencia == 'terror':
                print('Livros de terror:')
                for livro in self.terror:
                    print(f'Nome: {livro.nome}')

            elif preferencia == 'acao':
                print('Livros de ação:')
                for livro in self.acao:
                    print(f'Nome: {livro.nome}')
            elif preferencia == 'não' or preferencia == 'n':
                pesquisar = False

            else:
                print('Esse gênero não está disponível na nossa biblioteca.')


            continuar_pesquisando = input('\n\nPesquisar outro gênero? (s/n) ').lower()
            if continuar_pesquisando != 's':
                pesquisar = False


# -----------------------------------------------
livro1 = Livros('A Rainha', 'suspense')
livro2 = Livros('A Estrela Encantada', 'ficcao')
livro3 = Livros('Solidão com Vista para o Mar', 'romance')
livro4 = Livros('Hang With', 'acao')
livro5 = Livros('Íris', 'terror')
livro6 = Livros('Rosto na Ponta do Queixo', 'romance')
livro7 = Livros('Versos Precisos', 'fantasia')
livro8 = Livros('Lágrimas Negras', 'terror')
livro9 = Livros('Entre Flores e Estrelas', 'romance')
livro10 = Livros('Cobertor', 'ficcao')
livro11 = Livros('Chuva de Prata', 'fantasia')
livro12 = Livros('A Força Estranha', 'suspense')
livro13 = Livros('Hero Lonely', 'acao')

biblioteca = Biblioteca()
biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)
biblioteca.add_livro(livro3)
biblioteca.add_livro(livro4)
biblioteca.add_livro(livro5)
biblioteca.add_livro(livro6)
biblioteca.add_livro(livro7)
biblioteca.add_livro(livro8)
biblioteca.add_livro(livro9)
biblioteca.add_livro(livro10)
biblioteca.add_livro(livro11)
biblioteca.add_livro(livro12)
biblioteca.add_livro(livro13)

# testar
biblioteca.listar_livros()
biblioteca.generos()














class Livros:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero.lower()
        #criar listas para automatizacao:
        self.nomes = []
        self.generos = []
        #-----------------
        self.nomes.append(self.nome)
        self.generos.append(self.generos)

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.romances = []
        self.fantasia = []
        self.ficcao = []
        self.suspense = []
        self.terror = []
        self.acao = []

    def add_livro(self, livro):
        self.livros.append(livro)

        if livro.genero == 'fantasia':
            self.fantasia.append(livro)

        elif livro.genero == 'romance':
            self.romances.append(livro)

        elif livro.genero == 'ficcao':
            self.ficcao.append(livro)

        elif livro.genero == 'suspense':
            self.suspense.append(livro)

        elif livro.genero == 'terror':
            self.terror.append(livro)

        elif livro.genero == 'acao':
            self.acao.append(livro)

    def adicionarL(self):
        ln = input('Qual o nome do livro que você quer adicionar? ')
        lg = input('Qual o gênero do livro que você quer adicionar? ')

        livro = Livros(ln, lg)
        self.add_livro(livro)

        print('Livro adicionado com sucesso!')

    def listar_livros(self):
        print('Todos os nossos livros:')
        for livro in self.livros:
            print(f'{livro.nome} - Gênero: {livro.genero}')
            pesquisar = True
            while pesquisar:
                print('\nQuer filtrar algum gênero específico (s/n)? ')
                pesquisarGenero = input('').lower()
                print()
                if pesquisarGenero == 's':
                    preferencia = input('Digite o gênero desejado: \n 1 - Romance\n 2 - Fantasia\n 3 - Ficção\n 4 - Suspense\n 5 - Terror\n 6 - Ação\n 7 - Outro\n -> ')
                    if preferencia == '1':
                        print(f'\nLivros de romance:')
                        for livro in self.romances:
                            print(f'- {livro.nome}')

                    elif preferencia == '2':
                        print(f'\nLivros de fantasia:')
                        for livro in self.fantasia:
                            print(f'- {livro.nome}')

                    elif preferencia == '3':
                        print(f'\nLivros de ficção:')
                        for livro in self.ficcao:
                            print(f'- {livro.nome}')

                    elif preferencia == '4':
                        print(f'\nLivros de suspense:')
                        for livro in self.suspense:
                            print(f'- {livro.nome}')

                    elif preferencia == '5':
                        print(f'\nLivros de terror:')
                        for livro in self.terror:
                            print(f'- {livro.nome}')

                    elif preferencia == '6':
                        print(f'\nLivros de ação:')
                        for livro in self.acao:
                            print(f'- {livro.nome}')

                    elif preferencia == '7':
                        print(f'\nSó temos os gêneros de 1-6 na nossa biblioteca.')

                    else:
                        print(f'\nDigite um número válido.')

                    continuar_pesquisando = input('\n\nPesquisar outro gênero (s/n) ? ').lower()
                    if continuar_pesquisando == 'n':
                        pesquisar = False
                        break
                    else:
                        pesquisar = True
                    
                
                
                elif pesquisarGenero == 'n':
                    pesquisar = False
                    print('Você finalizou a consulta.')
                    break
                else:
                    print('Digite uma resposta válida!')
            if continuar_pesquisando == 'n' or pesquisarGenero == 'n':
                break                 


# ------------- CONFIGURAÇÕES PRE-ESTABELECIDAS-------------
livro1 = Livros('A Rainha', 'suspense')
livro2 = Livros('A Estrela Encantada', 'ficcao')
livro3 = Livros('Solidão com Vista para o Mar', 'romance')
livro4 = Livros('Hang With', 'acao')
livro5 = Livros('Íris', 'terror')
livro6 = Livros('Rosto na Ponta do Queixo', 'romance')
livro7 = Livros('Versos Precisos', 'fantasia')
livro8 = Livros('Lágrimas Negras', 'terror')
livro9 = Livros('Entre Flores e Estrelas', 'romance')
livro10 = Livros('Cobertor', 'ficcao')
livro11 = Livros('Chuva de Prata', 'fantasia')
livro12 = Livros('A Força Estranha', 'suspense')
livro13 = Livros('Hero Lonely', 'acao')

biblioteca = Biblioteca()
biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)
biblioteca.add_livro(livro3)
biblioteca.add_livro(livro4)
biblioteca.add_livro(livro5)
biblioteca.add_livro(livro6)
biblioteca.add_livro(livro7)
biblioteca.add_livro(livro8)
biblioteca.add_livro(livro9)
biblioteca.add_livro(livro10)
biblioteca.add_livro(livro11)
biblioteca.add_livro(livro12)
biblioteca.add_livro(livro13)
#----------------------------------------------------------

def usuario():
    print('Somos sua biblioteca preferida!! Digite:\n 1 - Pesquisar\n 2 - Adicionar')

    try:
        decisao = int(input('-> '))
    except ValueError:
        print('Digite apenas números (1 ou 2)!')
        return

    if decisao == 1:
        biblioteca.listar_livros()
    elif decisao == 2:
        biblioteca.adicionarL()
    else:
        print('Opção inválida')
    
    while True:
        print('Continue pesquisando... Digite:\n 1 - Pesquisar\n 2 - Adicionar')

        try:
            decisao = int(input('-> '))
        except ValueError:
            print('Digite apenas números (1 ou 2)!')
            return

        if decisao == 1:
            biblioteca.listar_livros()
        elif decisao == 2:
            biblioteca.adicionarL()
        else:
            print('Opção inválida')
        


# testar
usuario()
