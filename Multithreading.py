import time
import threading
print("\nMain Thread started")


def th_func(n):
    print(f"\nthread {n} started!")
    time.sleep(3)
    print(f"\nthread {n} finished!")


threads = [threading.Thread(target=th_func, args=[i]) for i in range(10)]
for th in threads:
    th.start()
for th in threads:
    th.join()

print("", 4+5)
print("\nMain Thread finished!")
