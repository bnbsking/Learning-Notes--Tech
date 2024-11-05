import sys, pygame, time, random
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
IMAGEWIDTH, IMAGEHEIGHT = 100, 100
background_color = (189, 252, 201)

def get_random_position(widow_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)
    return random_x, random_y

class Mosquito(pygame.sprite.Sprite):
    def __init__(self, width, height, random_x, random_y, widow_width, window_height):
        super().__init__()
        self.raw_image = pygame.image.load('./mosquito.png').convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random_x, random_y)
        self.width = width
        self.height = height
        self.widow_width = widow_width
        self.window_height = window_height

def main():
    # environment
    pygame.init()
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('bobo hit mosquito')
    # moving parameters
    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
    reload_mosquito_event = USEREVENT + 1
    pygame.time.set_timer(reload_mosquito_event, 1500)
    # interface parameters
    points, time = 0, 30
    point_font = pygame.font.SysFont(None, 40)
    time_font = pygame.font.SysFont(None, 40)
    hit_font = pygame.font.SysFont(None, 50)
    finish_font = pygame.font.SysFont(None, 100)
    hit_text_surface = None

    while True:
        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_mosquito_event:
                # 偵測到重新整理事件，固定時間移除蚊子，換新位置
                mosquito.kill()
                # 蚊子新位置
                random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
            elif event.type == MOUSEBUTTONDOWN and time>0:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在蚊子圖片上
                if random_x < pygame.mouse.get_pos()[0] < random_x + IMAGEWIDTH and random_y < pygame.mouse.get_pos()[1] < random_y + IMAGEHEIGHT:
                    mosquito.kill()
                    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    hit_text_surface = hit_font.render('Hit!!', True, (255, 0, 0))
                    points += 5

        # 背景顏色，清除畫面
        window_surface.fill(background_color)

        # 遊戲分數儀表板
        point_surface = point_font.render('Points: {}'.format(points), True, (0, 0, 255))
        time_surface = time_font.render('Time: {}'.format(round(time)), True, (0, 0, 0))
        finish_surface = finish_font.render('GAME OVER', True, (255,100,100))
        
        # 渲染物件
        window_surface.blit(mosquito.image, mosquito.rect)
        window_surface.blit(point_surface, (10, 0))
        window_surface.blit(time_surface, (500, 0))
        if time<0:
            window_surface.blit(finish_surface, (200, 250))
        
        # 顯示打中提示文字
        if hit_text_surface:
            window_surface.blit(hit_text_surface, (10, 50))
            hit_text_surface = None

        if time>=0:
            time-=0.005
        pygame.display.update()
     
if __name__ == '__main__':
    main()
