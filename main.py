import time
import random

def introduction():
    print("Ласкаво просимо до пригодницької гри!")
    print("Ви опиняєтеся в темній печері.")
    print("Перед вами два шляхи.")

def choose_path():
    print("Який шлях ви оберете? (1/2/3/4)")
    choice = input()
    if choice == "1":
        path_one()
    elif choice == "2":
        path_two()
    elif choice == "3":
        path_three()
    elif choice == "4":
        path_four()
    else:
        print("Невірний вибір. Спробуйте знову.")
        choose_path()

def path_one():
    print("Ви входите в кімнату, наповнену скарбами.")
    time.sleep(1)
    print("Вітаю, ти багатий!")
    game_over()

def path_two():
    print("Ви зустрічаєте страшного дракона!")
    time.sleep(1)
    print("Ви хочете битися чи бігти? (fight/run)")
    choice = input()
    if choice == "fight":
        dragon_fight()
    elif choice == "run":
        print("Ти біжиш, але дракон тебе ловить.")
        time.sleep(1)
        print("Гра завершена!")
        game_over()
    else:
        print("Невірний вибір. Спробуйте знову.")
        path_two()

def path_three():
    print("Ви потрапили в магічний ліс.")
    time.sleep(1)
    print("Ліс здається живим. Виберіть, куди йти (left/right)")
    choice = input()
    if choice == "left":
        print("Ви зустрічаєте ельфів, які допомагають вам знайти вихід.")
        time.sleep(1)
        print("Ви виходите з лісу невтративши часу!")
        game_over()
    elif choice == "right":
        print("Ви блукаєте в лісі, і не можете знайти вихід.")
        time.sleep(1)
        print("Гра завершена, ви загубились у лісі і померли з голоду!")
        game_over()
    else:
        print("Невірний вибір. Спробуйте знову.")
        path_three()

def path_four():
    print("Ви потрапили в старовинний замок.")
    time.sleep(1)
    print("Замок наповнений загадковими пасажами.")
    print("Виберіть, куди ви хочете піти (left/right)")
    choice = input()
    if choice == "left":
        print("Ви виявили секретну кімнату зі скарбами.")
        time.sleep(1)
        print("Тепер ви багатий!")
        game_over()
    elif choice == "right":
        print("Ви блукаєте в пасажах замку, і не можете знайти вихід.")
        time.sleep(1)
        print("Гра завершена, ви залишилися в замку назавжди!")
        game_over()
    else:
        print("Невірний вибір. Спробуйте знову.")
        path_four()

def dragon_fight():
    print("Ви вступаєте в запеклу битву з драконом...")
    time.sleep(2)
    result = random.choice(["win", "lose"])
    if result == "win":
        print("Ви перемогли дракона!")
        time.sleep(1)
        print("Ти герой!")
        game_over()
    else:
        print("Дракон сильніший і перемагає вас.")
        time.sleep(1)
        print("Гра завершена!")
        game_over()

def game_over():
    print("Хочеш знову пограти? (yes/no)")
    choice = input()
    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Дякуємо за гру! До побачення.")
        exit()
    else:
        print("Невірний вибір. Спробуйте знову.")
        game_over()

def start_game():
    introduction()
    choose_path()

if __name__ == "__main__":
    start_game()
