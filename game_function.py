import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

'''
def check_events(ship):
    ''''''响应按键和鼠标事件''''''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #检测键盘按下
            if event.key == pygame.K_RIGHT: #判断按下右键
                #向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #ship.rect.centerx -= 1
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
'''

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像，并切换到新屏幕 '''
    #每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets: #绘制子弹
        bullet.draw_bullet()
    #for alien in aliens: #显示外星人代码
        #alien.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()
    play_button.draw_button()

def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可以容纳多少外星人'''
    #print(ai_settings.screen_height)
    #print(alien_height)
    #print(ship_height)
    #input()
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    #available_space_x = ai_settings.screen_width - 2 * alien_width #计算屏幕可用宽度
    #number_aliens_x = int(available_space_x / (2 * alien_width)) #计算可以放置的外星人数量
    number_alien_x = get_number_aliens_x(ai_settings, alien_width)
    '''
    for alien_number in range(number_aliens_x): #创建一群外星人
        alien = Alien(ai_settings, screen) #创建一个外新人
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien) #将外星人加入编组
    '''
    number_rows = get_number_rows(ai_settings, ship_height, alien_height)
    for alien_row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, alien_row_number)

def get_number_aliens_x(ai_settings, alien_width): #计算可以放置的外星人数量
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, alien_row_number): #创建外星人
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_row_number
        aliens.add(alien)

def check_keydown_events(event,ai_settings, screen, stats, ship, bullets):
    '''响应按键'''
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE:
        '''当按下空格键时创建子弹，并将其加入子弹的编组'''
        '''
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        '''
        fire_bullet(ai_settings, screen, stats, ship, bullets)
        #print(bullets)
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def fire_bullet(ai_setting, screen, stats, ship, bulltes):
    if len(bulltes) < ai_setting.bullet_allowed and stats.game_active:
        new_bullet = Bullet(ai_setting, screen, ship)
        bulltes.add(new_bullet)

def check_keyup_event(event, ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    events = pygame.event.get()
    for event in events:
        #print(events)
        #input()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''响应鼠标按下'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_score()
        sb.prep_ship()
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #ai_settings.increase_speed()
        #print(ai_settings.ship_speed_factor)
        ai_settings.initialize_dynamic_settings()
        #创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_bullets(ai_settings,screen,stats, sb, ship, aliens,bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, bullets, aliens)
    #collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''
    if aliens:
        pass
    else:
        create_fleet(ai_settings, screen, ship, aliens)
    '''

def check_bullet_alien_collisions(ai_settings, screens, stats, sb, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #print(collisions)
    #if collisions:
        #stats.score += ai_settings.alien_point
        #sb.prep_score()
    for aliens in collisions.values():
        stats.score += ai_settings.alien_point * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
        #print(aliens)
    #print(len(collisions.values()))
    if aliens:
        pass
    else:
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        ai_settings.increase_speed()
        #print(ai_settings.ship_speed_factor)
        create_fleet(ai_settings, screens, ship, aliens)

def update_aliens(ai_settings, status, sb, screen, ship, alines, bullets):
    check_fleet_edges(ai_settings, alines)
    if pygame.sprite.spritecollideany(ship, alines):
        ship_hit(ai_settings, status, sb, screen, ship, alines, bullets)
    check_aliens_bottom(ai_settings, status, sb, screen, ship, alines, bullets)
    alines.update()

def check_fleet_edges(ai_settings, aliens):
    '''检查外星人是否碰到屏幕边缘'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''在外星人碰撞到边缘时修改运动方向并向下移动一个单位'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    #将ship_left减1
    if stats.ships_left > 1:
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #暂停   为什么先运行暂停在运行其他代码？
        sleep(0.5)
        stats.ships_left -= 1
        sb.prep_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''检查是否有外星人达到屏幕底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    '''检查是否产生了新的最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()