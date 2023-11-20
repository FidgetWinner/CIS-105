import pyperclip
import webbrowser
import time

def open_google_maps(address):
    base_url = "https://www.google.com/maps/dir/?api=1&destination="
    destination = address.replace(" ", "+")
    url = base_url + destination
    webbrowser.open(url, new =2)

previous_clipboard_content = None
while True:
    clipboard_content = pyperclip.paste()
    if clipboard_content != previous_clipboard_content:
        print("New address copied:", clipboard_content)
        open_google_maps(clipboard_content)
        previous_clipboard_content = previous_clipboard_content

    time.sleep(5) 

    