import pygame
from pygame.sprite import Sprite  #Sprite为pygame的一个类，协助创建对象群。（精灵？)

class Bullet(Sprite):
    '''对飞船发射的子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船所在位置创建一个子弹对象'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #在0,0处设置表示子弹的矩形。
        self.rect.centerx = ship.rect.centerx #设置子弹的X位置
        self.rect.top = ship.rect.top #设置子弹的起始Y位置
        self.y = float(self.rect.y) #设置子弹Y位置可以小数表示
        self.color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        self.y -= self.bullet_speed_factor  #更新表示子弹位置的小数
        self.rect.y = self.y #将更新后的子弹位置传递给子弹

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
