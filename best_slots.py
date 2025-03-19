import random

print("Лучшие игровые автоматы на деньги - Демо!")
spins = 4
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {4 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Крути лучшие автоматы и становись легендой в топ-казино!")
