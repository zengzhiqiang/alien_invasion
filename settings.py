class Settings():
    '''储存《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.ship_speed_factor = 1.5 #飞船移动速度
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10000
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  #外星人的运动方向，1表示右，-1表示左
        self.ship_limit = 3 #设置飞船数量
        self.speedup_scale = 1.1 #设置加速度
        self.initialize_dynamic_settings()
        self.alien_point = 50
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
        #print(self.alien_point)

    def reset_settings(self):
        pass