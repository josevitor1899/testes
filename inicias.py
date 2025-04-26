class MinhaClasse:
    def __init__(self, info): #método construtor, primeiro método a ser executado
        self.atributo1 = "meu atributo"
        self.atributo2 = [1, 2, 3]
        self.novoatributo = info
        
        
    def metodo_1(self):
        print("minha acao1")
    
    def metodo2(self, numero):
        print(self.atributo2[1] + numero)
    
    def metodo3(self):
        print(self.novoatributo)

#"minha_classse" é o um objeto

#A partir de uma classe("MinhaClasse") instanciamos um objeto

minha_classe = MinhaClasse("aqui está o valor do novo atributo")
minha_classe.metodo2(2)
minha_classe.metodo3()

