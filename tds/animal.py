class Animais():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''
    sexo = ''

class Cachorro(Animais):
    tem_rabo = True
    especie = 'Canis lupus familiares'
    raca = "Shitzu"
    nome = "Sérgio"
    porte = "Pequeno"

    def latir():
        return 'AUAUAUAUAUAUAUAUAUAU'
    
    def comer():
        return "Chomp Chomp"
    
    def dormir():
        return 'ZZZZZZZZZZZZZZZZZZZ'
    
print(Cachorro.latir())
print(Cachorro.comer())
print(Cachorro.dormir())
print(Cachorro.tem_rabo)
print(Cachorro.especie)
print(Cachorro.raca)
print(Cachorro.nome)
print(Cachorro.porte)