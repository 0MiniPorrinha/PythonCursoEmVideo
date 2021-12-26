from pygame import mixer

#inicia o mixer
mixer.init()

#carega a musica
mixer.music.load('uepa.mp3')

#controla o volume
mixer.music.set_volume(0.7) 

#começa a tocar a musica
mixer.music.play()
