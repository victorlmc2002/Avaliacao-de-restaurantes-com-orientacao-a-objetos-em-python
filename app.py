from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.recebe_avaliacao('Eu', 7)
restaurante_praca.recebe_avaliacao('Ela', 8)
restaurante_mexicano.recebe_avaliacao('Eu', 9)
restaurante_mexicano.alternar_status()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
