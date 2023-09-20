import random

# 初始化游戏参数
GRID_SIZE = 20
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
player_funds = 1000
round_number = 1  # 添加局数计数器

# 不同战舰的属性
ships = {
    '小战舰': {'价格': 200, '攻击范围': 3, '攻击力': 20},
    '中战舰': {'价格': 500, '攻击范围': 5, '攻击力': 50},
    '大战舰': {'价格': 1000, '攻击范围': 7, '攻击力': 100}
}

# 外星人和其他敌方战舰的位置
alien_x, alien_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
enemy_ships = [{'类型': '小战舰', 'x': random.randint(0, GRID_SIZE - 1), 'y': random.randint(0, GRID_SIZE - 1)} for _ in range(3)]

# 初始化敌方战舰的生命和攻击范围
for enemy_ship in enemy_ships:
    enemy_ship['生命'] = random.randint(100, 200)
    enemy_ship['攻击范围'] = random.randint(3, 6)
    enemy_ship['攻击力'] = random.randint(20, 50)

def display_grid():
    for row in grid:
        print(' '.join(row))
    print()

def place_ship(ship_type, x, y):
    if grid[y][x] == ' ':
        grid[y][x] = ship_type
        print(f"{ship_type}已部署在({x}, {y})")
    else:
        print("该位置已经被占据，请选择其他位置。")

def attack_enemy_ship(ship_type, x, y):
    for enemy_ship in enemy_ships:
        if enemy_ship['x'] == x and enemy_ship['y'] == y:
            enemy_ship_attrs = ships[enemy_ship['类型']]
            distance = max(abs(enemy_ship['x'] - x), abs(enemy_ship['y'] - y))
            if distance <= enemy_ship['攻击范围']:
                damage = max(0, ships[ship_type]['攻击力'] - distance)
                enemy_ship['生命'] -= damage
                print(f"{ship_type}攻击了敌方{enemy_ship['类型']}，造成了{damage}点伤害。")
                if enemy_ship['生命'] <= 0:
                    enemy_ships.remove(enemy_ship)
                    print(f"敌方{enemy_ship['类型']}被摧毁！")
            else:
                print(f"{ship_type}无法攻击敌方{enemy_ship['类型']}，距离太远。")
            return True
    return False

def alien_attack():
    global player_funds
    for ship_type, ship_attrs in ships.items():
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grid[y][x] == ship_type:
                    for enemy_ship in enemy_ships:
                        distance = max(abs(enemy_ship['x'] - x), abs(enemy_ship['y'] - y))
                        if distance <= ship_attrs['攻击范围']:
                            damage = max(0, ship_attrs['攻击力'] - distance)
                            enemy_ship['生命'] -= damage
                            print(f"{ship_type}攻击了敌方{enemy_ship['类型']}，造成了{damage}点伤害。")
                            if enemy_ship['生命'] <= 0:
                                enemy_ships.remove(enemy_ship)
                                print(f"敌方{enemy_ship['类型']}被摧毁！")
    print(f"玩家现有资金: ${player_funds}")

def generate_enemy_ships():
    new_enemy_ships = []
    for _ in range(3):
        enemy_ship = {'类型': random.choice(list(ships.keys())), 'x': random.randint(0, GRID_SIZE - 1), 'y': random.randint(0, GRID_SIZE - 1)}
        enemy_ship['生命'] = random.randint(100, 200)
        enemy_ship['攻击范围'] = random.randint(3, 6)
        enemy_ship['攻击力'] = random.randint(20, 50)
        new_enemy_ships.append(enemy_ship)
    return new_enemy_ships

def check_failure_condition():
    if round_number < 3:
        return False  # 前两局不检查失败条件
    enemy_count = len(enemy_ships)
    player_count = sum(1 for row in grid for cell in row if cell != ' ' and cell != 'A')
    if player_count == 0:
        return True
    enemy_area_count = 0
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[y][x] == 'E':
                continue
            enemy_cells = 0
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == 'E':
                        enemy_cells += 1
            if enemy_cells >= 1:
                enemy_area_count += 1
    return enemy_area_count >= GRID_SIZE * GRID_SIZE / 3

# 提前告知外星人和敌方战舰的位置
print(f"外星人位于({alien_x}, {alien_y})")
for i, enemy_ship in enumerate(enemy_ships, start=1):
    print(f"敌方战舰{i}位于({enemy_ship['x']}, {enemy_ship['y']})")

# 游戏主循环
while True:
    display_grid()

    if (player_funds <= 0 or not enemy_ships) or check_failure_condition():
        print("游戏结束！")
        break

    print("可选战舰：")
    for i, (ship_type, ship_attrs) in enumerate(ships.items(), start=1):
        print(f"{i}. {ship_type} - 价格: ${ship_attrs['价格']}, 攻击范围: {ship_attrs['攻击范围']}, 攻击力: {ship_attrs['攻击力']}")

    choice = input("选择要投放的战舰（输入编号）或输入X发起攻击或输入Q退出游戏: ")

    if choice.upper() == 'Q':
        break
    elif choice.upper() == 'X':
        for i, enemy_ship in enumerate(enemy_ships, start=1):
            print(f"敌方战舰{i}生命: {enemy_ship['生命']}, 攻击范围: {enemy_ship['攻击范围']}, 攻击力: {enemy_ship['攻击力']}")

        if check_failure_condition():
            print("你失败了！")
            break

        # 玩家攻击
        attack_x, attack_y = map(int, input("选择要攻击的敌方战舰的坐标（输入x和y坐标，以空格分隔）: ").split())
        if attack_enemy_ship('大战舰', attack_x, attack_y):
            grid[attack_y][attack_x] = ' '  # 清除敌方战舰
        else:
            print("无效的攻击目标。")

        # 随机生成新的敌方战舰
        new_enemy_ships = generate_enemy_ships()
        enemy_ships.extend(new_enemy_ships)
        print("新的敌方战舰已出现！")

        # 外星人和敌方战舰攻击
        grid[alien_y][alien_x] = 'A'
        for enemy_ship in enemy_ships:
            grid[enemy_ship['y']][enemy_ship['x']] = 'E'

        print("外星人和敌方战舰向你发起了攻击！")

        alien_attack()

        # 结束一局后增加经费
        round_income = random.randint(1000, 1500)
        player_funds += round_income
        print(f"本局结束，获得经费: ${round_income}")

        # 增加局数计数器
        round_number += 1
    else:
        try:
            choice = int(choice)
            if 1 <= choice <= len(ships):
                ship_type = list(ships.keys())[choice - 1]
                if player_funds >= ships[ship_type]['价格']:
                    player_funds -= ships[ship_type]['价格']
                    x, y = map(int, input(f"选择在哪个位置部署{ship_type}（输入x和y坐标，以空格分隔）: ").split())
                    if x == alien_x and y == alien_y:
                        print("无法部署到外星人的位置。")
                    elif any(enemy_ship['x'] == x and enemy_ship['y'] == y for enemy_ship in enemy_ships):
                        print("无法部署到敌方战舰的位置。")
                    else:
                        place_ship(ship_type, x, y)
                else:
                    print("资金不足，无法购买该战舰。")
            else:
                print("无效的选择。")
        except ValueError:
            print("无效的输入。")
