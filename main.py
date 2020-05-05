from Solvers import Interpolation
from Solvers import ServiceWorker

print("Welcome to interpolation solver!")


while 1:
    print("What you want?\n"
          "\t1. Solve.\n"
          "\t2. Exit\n")
    try:
        answer = int(input("Please choose a variant: ").strip())
        if answer == 1:
            while 1:
                print("Please choose a variant of interpolation:\n"
                      "\t1. With a given non-constant step.\n"
                      "\t2. With a constant step.\n"
                      "\t3. Back\n")
                var = int(input("Please choose a variant: ").strip())
                if var == 1:
                    worker = ServiceWorker.ServiceWorker(1)
                    del worker
                    continue
                elif var == 2:
                    worker = ServiceWorker.ServiceWorker(2)
                    del worker
                    continue
                elif var == 3:
                    break
        elif answer == 2:
            print("Exit...")
            break
    except TypeError:
        ServiceWorker.getReadyAnswer(1)
        continue
    except ValueError:
        ServiceWorker.getReadyAnswer(1)
        continue
    except KeyboardInterrupt:
        print("Exit...")
        break
