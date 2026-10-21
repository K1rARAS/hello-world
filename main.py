import time
import sys

if __name__ == "__main__":
    print("Waiting for user input...")
    try:
        input("Press Enter to continue...")
    except EOFError:
        pass

    time.sleep(1)
    print("Hello world")
    input("Press Enter to exit...")
    sys.exit(0)