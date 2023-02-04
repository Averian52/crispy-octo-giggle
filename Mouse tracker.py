import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
        return False # Returning False if you need to stop the program when Left clicked.
    else:
        print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))

def move_mouse():
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    pyautogui.moveTo(x, y)
    print("Mouse moved to: ({}, {})".format(x, y))

def main():
    choice = input("1. Tracker\n2. Show me\nEnter your choice: ")
    if choice == "1":
        listener = mouse.Listener(on_click=on_click)
        listener.start()
        listener.join()
    elif choice == "2":
        move_mouse()
    else:
        print("Invalid input. Try again.")

if __name__ == "__main__":
    main()  

    