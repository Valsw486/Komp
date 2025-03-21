from abc import ABC, abstractmethod


# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом!"


class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука!"


# Класс Monster
class Monster:
    def __init__(self, health):
        self.health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")


# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster: Monster):
        if self.weapon:
            print(self.weapon.attack())
            monster.take_damage(10)  # Урон фиксированный для простоты
            print(f"Здоровье монстра: {monster.health}")  # Выводим текущее здоровье монстра


# Шаг 4: Реализуем механизм боя
def battle(fighter: Fighter, monster: Monster):
    # Первый удар
    fighter.attack_monster(monster)

    # Проверяем, жив ли монстр
    if monster.is_alive():
        # Меняем оружие на лук
        fighter.change_weapon(Bow())
        fighter.attack_monster(monster)

    # Проверяем, побежден ли монстр после второго удара
    if not monster.is_alive():
        print("Бой завершен!")  # Сообщение о завершении боя


# Пример использования
if __name__ == "__main__":
    fighter = Fighter("Артур")
    monster = Monster(20)  # Изменено здоровье монстра на 20

    # Боец выбирает меч и атакует
    fighter.change_weapon(Sword())
    battle(fighter, monster)