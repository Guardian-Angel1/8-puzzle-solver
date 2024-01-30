from solvability_check import *
from generate_instances import *
from A_star_algo import *


random.seed(101)
def main_menu():
    while True:
        choice = 0
        if choice == 0:
            print("\nWelcome to Prakhar's Implementation of 8 puzzle Problem")
            print("======================Menu======================")
            print("1. Use your own input")
            print("2. Generate random examples")
            print("4. Exit")
            print("================================================\n")
            
            

            choice = input("Enter your choice [1-4]: ")

            if choice == '1':
                inp = []
                goal = []
                print("Enter your input state of the puzzle in row major order:")
                for i in range(9):
                    x = int(input())
                    inp.append(x)

                inp = np.array(inp)
                inp = inp.reshape(3,3)
                print("Enter your goal state of the puzzle in row major order:")
                for i in range(9):
                    x = int(input())
                    goal.append(x)

                goal = np.array(goal)
                goal = goal.reshape(3,3)
                if not check_solvability(inp, 3):
                    print("This instance of the 8 puzzle is not solvable")
                else:
                    run_algo(inp, goal)
                choice = 0
                
                
            elif choice == '2':
                po=int(input("Enter number of instances to generate: "))
                instances = generate_instances(3, po)
                for i in instances:
                    print(i)
                    print()
                
                c = 0
                goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                goal = np.array(goal)
                goal = goal.reshape(3,3)

                print("The goal state is given by: \n", goal)

                if c==0:
                    print("==================================MENU 2==================================")
                    print("\nWhich heuristic function do you want to use to run the A* algorithm?")
                    print("1. Hamming Priority")
                    print("2. Manhattan Distance")
                    print("3. Manhattan with Linear Conflict")
                    print("4. Back")
                    print("==========================================================================")


                    c= int(input("Enter your choice [1-4]: "))
                    if c == 1:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_hamming()
                            print(i)
                            print("==================RESULTS==================")
                            print(f" Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\nTime taken: {t}")
                            print("===========================================")

                    if c == 2:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_manhattan()
                            print(i)
                            print("==================RESULTS==================")
                            print(f" Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\nTime taken: {t}")
                            print("===========================================")
                    if c == 3:
                        for i in instances:
                            puzz = Puzzle(i, goal)
                            t, p, l, n = puzz.run_manhattan_linear()
                            print(i)
                            print("==================RESULTS==================")
                            print(f"Length of the Solution: {l}\n Number of nodes taken out from the frontier: {n}\nTime taken: {t}")
                            print("===========================================")
                    if c == 0 :
                        choice = 0
            
            elif choice == '4':
                print("GoodBye")
                print("Exiting the program.")
                print("Have a nice day!")
                break
            else:
                print("Invalid choice. Please choose valid option.")

if __name__ == "__main__":
    main_menu()