from random import randint
import signal


def time_is_up(signal, frame):
    raise Exception("Time is UP !!!")


def ice_breaks():
    if roll_a_dice() < 4:
        print("Oh No!!! Ice breaks and you start to fall down")
        fall_down()
        return True
    else:
        return False


def fall_down():
    if roll_a_dice() >= 5:
        print("Somehow you managed to grab rocks on slope of the mountain")
    else:
        print("Members of rescue team saw how you fall from a great distance.")
        print("You will be always remembered as one of the eagles.")
        print("Rest in Peace.")
        print(" ____________ ")
        print("|            |")
        print("|            |")
        print("|   R.I.P.   |")
        print("|            |")
        print("|            |")
        print("|         [*]|")
        play_again()


def stone_hit():
    print("You were hit by the stone!")
    gods_throw = roll_a_dice()
    if gods_throw in [1, 2, 3]:
        print("Massive punch throws you out of the slope, you start to fall down!")
    else:
        print("You are one of a hard mother fucker! Falling stones just don't bother you.")


def falling_rocks():
    print(" !!!!!! Look out!!! There are heavy stones cooing at you !!!!!")
    print("Quick!!, you need to decide what you do!")
    print("""
        1)Jump left - type 1
        2)Jump right - arrow right
        3)Stay on your place - arrow up""")
    signal.signal(signal.SIGALRM, time_is_up)
    signal.alarm(10)
    rock_path = check_rock_path()
    try:
        if input(">>>") == rock_path:
            stone_hit()
        else:
            print("You are fast! You had dodged the stone! ")
    except:
        print("You haven't moved")
        if rock_path == "2":
            print("It was bad decision, rock was coming right at you!")
            stone_hit()
        else:
            print("That was a clever 'move'! Rock felt ")


def check_rock_path():
    determinant = roll_a_dice()
    if determinant in (1, 2):
        return "1"
    elif determinant in (3, 4):
        return "2"
    elif determinant in (5, 6):
        return "3"


def track_1_1():
    print("You have chosen a though path this time, you will loose a lot of strenghth to get to the top.")
    print("Are you sure you want to continue to climb this way? Every second counts!")
    decision = input(">>>")
    if decision in ["yes", "yea", "sure"]:
        print("You start to climb, there is a lot of ice on slope. You see a lot of cracks on ice surface.")
        ice_breaks()


def play_again():
    print("<<<>>> Your game has ended but, don't be afraid, you can always play one more time <<<>>>")
    print("Do you want to play one more time?")
    print("1)Yes")
    print("2)No")
    answer = input(">>>")
    if answer in ("1", "yes", "Yes"):
        start()
    else:
        "XoXoXoXo See You again!"
        exit(0)


def track_1_2():
    print("You are lucky! You have chosen easy path, still there is always chance that something bad will happen.")
    print("But those are the mountains, you never know...")
    falling_rocks()


def track_1_3():
    print("Path you have chosen is likely to be quite hard, there will be nowhere to rest.")
    print("Some more steps will need to be taken to provide shelter.")
    print("At least there is no ice on mountain slope")


def roll_a_dice():
    """Method to generate random number from 1 to 6
    :return: number from 1 to 6
    """
    return randint(1, 6)


def start():
    print("Welcome brave alpinst, you are member of rescue team for one poor guy who stayed at top")
    print("You will have to face many difficult choices, you better prepare!")
    print("You start from the base situated at the bottom of the mountain")
    print("           /\                 ")
    print("          /  \_               ")
    print("         /     \              ")
    print("       _/       \_            ")
    print("      /           \           ")
    print("     /             \          ")
    print("                              ")
    print("       ^    ^    ^            ")
    print("Chose which way you want to start: ")
    print("1)left")
    print("2)right")
    print("3)center")
    while True:
        decision = input(">>>")
        if decision in ["1", "left"]:
            track_1_1()
        elif decision == "3" or decision == "center":
            track_1_2()
        elif decision == "2" or decision == "right":
            track_1_3()
        else:
            print("Quickly make decision, there is no more time left! Poor guy is counting on you!")


start()
