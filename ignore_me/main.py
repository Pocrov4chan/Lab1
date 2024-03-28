import pygame
import time

pygame.init()

screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load("mainclock.png")
minute_hand_image = pygame.image.load("rightarm.png")
second_hand_image = pygame.image.load("leftarm.png")

background_rect = background_image.get_rect(center=(screen_width // 2, screen_height // 2))
minute_hand_rect = minute_hand_image.get_rect(center=(screen_width // 2, screen_height // 2))
second_hand_rect = second_hand_image.get_rect(center=(screen_width // 2, screen_height // 2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current_time = time.localtime()
    seconds_angle = (current_time.tm_sec / 60) * 360
    minutes_angle = (current_time.tm_min / 60) * 360

    rotated_minute_hand = pygame.transform.rotate(minute_hand_image, -minutes_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand_image, -seconds_angle)

    screen.fill((0, 0, 0))

    screen.blit(background_image, background_rect)
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=minute_hand_rect.center))
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=second_hand_rect.center))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    

