import pygame

pygame.init()

pygame.mixer.init()

list_of_songs = ["song_1.mp3", "song_2.mp3", "song_3.mp3", "song_4.mp3"]

pygame.mixer.music.load("song_1.mp3")

pygame.mixer.music.play()

screen = pygame.display.set_mode()
font = pygame.font.SysFont("comicsansms", 20)
text = font.render("Here is a list of commands based on your input:", True, (0, 128, 0))
commamd_1 = font.render("1) n -- play the next song", True, (0, 128, 0))
command_2 = font.render("2) s -- pause the song", True, (0, 128, 0))
command_3 = font.render("3) c -- unpause the song", True, (0, 128, 0))
command_4 = font.render("4) p -- play the previosu somg", True, (0, 128, 0))
                   
                   

def play_next_song():
    global list_of_songs
    list_of_songs = list_of_songs[1:] + [list_of_songs[0]]
    pygame.mixer.music.load(list_of_songs[0])
    pygame.mixer.music.play()

def play_previous_song():
    global list_of_songs
    list_of_songs = [list_of_songs[-1]] + list_of_songs[0:-1]
    pygame.mixer.music.load(list_of_songs[0])
    pygame.mixer.music.play()

done = False

while not done:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            play_next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            play_previous_song()
    screen.fill((255, 255, 255))
    screen.blit(text, (200, 200))
    screen.blit(commamd_1, (200, 300))
    screen.blit(command_2, (200, 400))
    screen.blit(command_3, (200, 500))
    screen.blit(command_4, (200, 600))
    pygame.display.flip()

