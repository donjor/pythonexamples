import random
import pause


check_orders = True
check_count = 0


while check_orders == True:

    random_num = random.randrange(5)
    print(random_num)

    if random_num == 0: #number is 0,1,2,3,4
        print("random_num = 0, break loop")
        check_orders = False
    else:
        print("random_num != 0, continue looping")


    check_count = check_count + 1

    if check_count >= 10:
        print("max check reached, breaking loop")
        check_orders = False

    pause.seconds(1)
