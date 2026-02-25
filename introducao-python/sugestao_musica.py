def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'Neutra'
    else: 'não recomendada'

resultado = classificar_musica('Pop', 'Rock')
print(resultado)