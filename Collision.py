class Collision(object):
    def bullet_and_target(bullet, target):
        if bullet.y - bullet.radius < target.hitbox[1] + target.hitbox[3] \
                and bullet.y + bullet.radius > target.hitbox[1]:
            if bullet.x + bullet.radius > target.hitbox[0] \
                    and bullet.x - bullet.radius < target.hitbox[0] + target.hitbox[2]:
                return True
        return False

    def enemy_attack(enemy, hero):
        if hero.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] \
            and hero.hitbox[1] + hero.hitbox[3] > enemy.hitbox[1]:
            if hero.hitbox[0] + hero.hitbox[2] > enemy.hitbox[0] \
                and hero.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    return True
        return False

    def hero_on_block(block, hero):
        if hero.hitbox[0] > block.hitbox[0] and hero.hitbox[0] < block.hitbox[0] + block.hitbox[2]:
            if block.hitbox[1] - hero.y - 64 <= 3:
                return True
        return False

    def hero_under_block(hero, block):
        pass

    def hero_and_left_border_of_block(hero, block):
        pass

    def hero_and_right_border_of_block(hero, block):
        pass
