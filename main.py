class Personagem():
    def __init__(self, nome, nível):
        self.nome = nome
        self.nível = nível
        self.vida = 2 * nível	
            
    def get_nível(self):
        return self.nível 
    
    def get_ataque(self):
        return self.nível * 1
    
    def set_vida(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
            
    def get_vida(self):
        return self.vida
    
    def get_nome(self):
        return self.nome
    
    def atacar(self, inimigo):
        inimigo.set_vida(self.get_ataque())
        print(f'\n {self.get_nome()} atacou {inimigo.get_nome()}, causou {self.get_ataque()} pontos de dano')
        print(f'\n {inimigo.get_nome()} está com {inimigo.get_vida()} PV')
        
class Inimigo(Personagem):
    def __init__(self, nome, nível):
        super().__init__(nome, nível)
        
class Herói(Personagem):
    def __init__(self, nome, nível, habilidade):
        super().__init__(nome, nível)
        self.habilidade = habilidade
        
    def ataque_especial(self, inimigo):
        inimigo.set_vida(self.get_ataque()*2)
        print(f'\n {self.get_nome()} atacou {inimigo.get_nome()} com {self.habilidade} e causou {self.get_ataque()*2} pontos de dano')
        print(f'\n {inimigo.get_nome()} está com {inimigo.get_vida()} PV')
        
class Jogo():
    def __init__(self):
        self.personagem1 = Herói('Herói', 12, 'Corte rápido')
        self.personagem2 = Inimigo('Orc', 20)
        
    def derrota(self):
        print('\n Após uma longa batalha você foi derrotado!')
        print(f'\n O {self.personagem2.get_nome()} te derrotou e restou {self.personagem2.vida} PV :(')
    
    def vitoria(self):
        print('\n Parabéns bravo guerreiro!')
        print(f'\n A batalha contra {self.personagem2.get_nome()} terminou em êxito!')
        print(f'\n Você conseguiu derrotar {self.personagem2.get_nome()} e restou {self.personagem1.vida} PV!')
        
    def iniciar_jogo(self):
        print("\n Bem-vindo ao Jogo de Personagens!")
        print(f'\n Você, {self.personagem1.get_nome()}, é nível {self.personagem1.get_nível()} e tem {self.personagem1.vida} PV')
        print(f'\n Seu oponente, {self.personagem2.get_nome()}, é  nível {self.personagem2.get_nível()} e tem {self.personagem2.vida} PV')
        self.cd = 0
        while True:
            num = input('\n Digite 1 para começar: ')
            if num == '1':
                break
        while self.personagem1.vida > 0 and self.personagem2.vida > 0:
            tipo = input("\n Digite 1 para ataque normal ou 2 para ataque especial: ")
            if tipo == '1':
                self.personagem1.atacar(self.personagem2)
                if self.cd > 0:
                    self.cd -= 1
            elif tipo == '2' and self.cd == 0:
                self.personagem1.ataque_especial(self.personagem2)
                self.cd = 1
            elif tipo == '2' and self.cd > 0:
                print(f'\n Você não pode usar essa habilidade - tempo de recarga: {self.cd} !')
                while tipo == '2':
                    tipo = input("\n Escolha outro ataque: 1 - ataque normal ")
                self.personagem1.atacar(self.personagem2)
                self.cd -= 1
                
            if self.personagem2.vida <= 0:
                break
            self.personagem2.atacar(self.personagem1)
            if self.personagem1.vida <= 0:
                break
        
        if self.personagem1.vida > 0:
           self.vitoria()
        else:
            self.derrota()
            
            
            
jogo = Jogo()
jogo.iniciar_jogo()
            
        