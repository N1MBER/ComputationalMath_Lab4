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
                print("Please choose a mode:\n"
                      "\t1. With ready data\n"
                      "\t2. With your data\n")
                num = int(input("Variant: ").strip())
                if num == 1:
                    worker = ServiceWorker.ServiceWorker(1)
                    del worker
                    continue
                elif num == 2:
                    worker = ServiceWorker.ServiceWorker(2)
                    del worker
                    continue
                else:
                    ServiceWorker.getReadyAnswer(1)
                    continue
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