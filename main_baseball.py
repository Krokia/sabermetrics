import calc_baseball as bball

def baseball_menu():
    action = ""
    while action != "0":
        print("=================")
        print("Choose an action:")
        print("=================")
        print("1. Calculate OBP")
        print("2. Calculate SLG")
        print("3. Calculate OPS")
        print("4. Calculate K/9")
        print("5. Calculate FIP")
        print("6. Calculate BABIP")
        print("0. Exit")
        action = input("Option: ")
            
        if action == "1":
            bball.calc_obp()
        elif action == "2":
            bball.calc_slg()
        elif action == "3":
            bball.calc_ops()
        elif action == "4":
            bball.calc_k9()
        elif action == "5":
            bball.calc_fip()
        elif action == "6":
            bball.calc_babip()
        elif action != "0":
            print("That option is not available :(")
            
    print("==============")
    print(">> End")
    print("==============")
    
baseball_menu()