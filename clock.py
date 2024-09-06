try:
    import pygame
    from pygame.locals import *
    import time
    import math

    pygame.init()

    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Clock')

    # variable
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    DARKERBLUE = (22, 29, 111)
    DARKBLUE = (11, 47, 159)
    LIGHTBLUE = (152, 222, 217)
    LIGHTERBLUE = (199, 255, 216)
    SUPERDARKBLUE = (30, 42, 94)
    LIGHTSKIN = (225, 215, 183)
    running = True
    total_secs = 0
    start = False
    total = 0

    # tạo font chữ
    font = pygame.font.SysFont('sans', 50)
    text_1 = font.render('+', True, SUPERDARKBLUE)
    text_2 = font.render('-', True, SUPERDARKBLUE)
    text_3 = font.render('Start', True, SUPERDARKBLUE)
    text_4 = font.render('Reset', True, SUPERDARKBLUE)


    # gọi biến thời gian
    clock = pygame.time.Clock()

    # biến âm thanh
    sound = pygame.mixer.Sound('bingchiling.mp3')

    # game running
    while running:
        # fps 60
        clock.tick(60)
        screen.fill(SUPERDARKBLUE)

        # lấy vị trí chuột
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print(mouse_x, mouse_y)

        # plus button & start
        pygame.draw.rect(screen, LIGHTSKIN, (100, 50, 50, 50))
        pygame.draw.rect(screen, LIGHTSKIN, (200, 50, 50, 50))
        pygame.draw.rect(screen, LIGHTSKIN, (300, 50, 150, 50))

        # subtract button & reset
        pygame.draw.rect(screen, LIGHTSKIN, (100, 200, 50, 50))
        pygame.draw.rect(screen, LIGHTSKIN, (200, 200, 50, 50))
        pygame.draw.rect(screen, LIGHTSKIN, (300, 200, 150, 50))

        # status bar
        pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
        pygame.draw.rect(screen, LIGHTBLUE, (60, 530, 380, 30))
        




        # viết chữ lên màn hình
        screen.blit(text_1, (110, 45))
        screen.blit(text_1, (210, 45))
        screen.blit(text_3, (310, 45))
        screen.blit(text_2, (110, 195))
        screen.blit(text_2, (210, 195))
        screen.blit(text_4, (310, 195))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.pause()
                    # 3 nút hàng đầu tiên
                    if (100 < mouse_x < 150) and (50 < mouse_y < 100):
                        total_secs += 60
                        total = total_secs
                    if (200 < mouse_x < 250) and (50 < mouse_y < 100):
                        total_secs += 1
                        total = total_secs
                    if (300 < mouse_x < 450) and (50 < mouse_y < 100):
                        if total_secs != 0:
                            start = True
                            total = total_secs
                    # 3 nút hàng tiếp theo
                    if (100 < mouse_x < 150) and (200 < mouse_y < 250):
                        total_secs -= 60
                        total = total_secs
                    if (200 < mouse_x < 250) and (200 < mouse_y < 250):
                        total_secs -= 1
                        total = total_secs
                    if (300 < mouse_x < 450) and (200 < mouse_y < 250):
                        total_secs = 0
                        total = total_secs
                        start = False

        # giảm thời gian nếu Start là true
        if start:
            total_secs -= 1
            if total_secs == 0:
                start = False
                pygame.mixer.Sound.play(sound)
            time.sleep(0.05)

        # không làm xuất hiện số âm
        if total_secs < 0:
            total_secs = 0

        # Hiển thị thời gian lên màn hình
        mins = int(total_secs / 60)
        secs = total_secs - mins*60
        time_now = str(mins) + "   :   " + str(secs)
        text_time = font.render(time_now, True, LIGHTERBLUE)
        screen.blit(text_time, (110, 120))

        # vẽ loading bar
        if total != 0:
            pygame.draw.rect(screen, DARKBLUE, (60, 530, total_secs * 380 / total, 30))


        # circle
        x_center = 250
        y_center = 400 
        pygame.draw.circle(screen, BLACK, (x_center, y_center), 110)
        pygame.draw.circle(screen, LIGHTSKIN, (x_center, y_center), 100)
        pygame.draw.circle(screen, DARKERBLUE, (x_center, y_center), 5)

        # chiều dài của 2 kim
        sec_len = 95
        min_len = 80

        # minute line & second line
        x_sec = x_center + sec_len * math.sin(6 * secs * math.pi / 180)
        y_sec = y_center - sec_len * math.cos(6 * secs * math.pi / 180)

        x_min = x_center + min_len * math.sin(6 * mins * math.pi / 180)
        y_min = y_center - min_len * math.cos(6 * mins * math.pi / 180)


        pygame.draw.line(screen, BLACK, (x_center, y_center), (x_sec, y_sec), 2)
        pygame.draw.line(screen, DARKERBLUE, (x_center, y_center), (x_min, y_min), 2)


        pygame.display.flip()

    pygame.quit()
except Exception as bug:
    print(bug)  