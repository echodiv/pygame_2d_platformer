
class EnemyNotFoundError(Exception):
    def __init__(self):
        super().__init__("Emeny not found")


class BulletNotFoundError(Exception):
    def __init__(self):
        super().__init__("Hero not found")