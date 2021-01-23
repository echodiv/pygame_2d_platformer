
def shoot_in_enemy_collision(bullet, enemy):
    if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] \
            and bullet.y + bullet.radius > enemy.hitbox[1]:
        if bullet.x + bullet.radius > enemy.hitbox[0] \
                and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
            enemy.hit()
            return True
    return False


def enemy_attack_collision(enemy, hero):
    if hero.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] \
        and hero.hitbox[1] + hero.hitbox[3] > enemy.hitbox[1]:
        if hero.hitbox[0] + hero.hitbox[2] > enemy.hitbox[0] \
            and hero.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                return True
    return False