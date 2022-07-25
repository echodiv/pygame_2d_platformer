class EnemyNotFoundError(Exception):
    def __init__(self):
        super().__init__("Emeny not found")


class BulletNotFoundError(Exception):
    def __init__(self):
        super().__init__("Hero not found")


class BlockNotFoundError(Exception):
    def __init__(self):
        super().__init__("Block not found")
