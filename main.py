import keyboard
import ctypes
import psutil

list_pids = psutil.pids()
typed_buffer = ""
TARGET_WORD = "jump"
game_found = False

for pid in list_pids:
    try:
        p = psutil.Process(pid)
        if "GeometryDash.exe" in p.name():
            game_found = True

            def on_key_event(event):
                global typed_buffer

                if event.event_type == keyboard.KEY_DOWN:
                    print("Play 'TypeToJumpGD' By OpfinderA for a fun test of your skills!")
                    if len(event.name) == 1:
                        typed_buffer += event.name.lower()
                    elif event.name == "space":
                        typed_buffer += " "
                    elif event.name == "backspace":
                        typed_buffer = typed_buffer[:-1]

                    if len(typed_buffer) > 50:
                        typed_buffer = typed_buffer[-20:]

                    if typed_buffer.endswith(TARGET_WORD):
                        keyboard.send(hotkey=57)

            keyboard.hook(on_key_event)
            keyboard.wait()
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

if not game_found:
    ctypes.windll.user32.MessageBoxW(0, "Geometry Dash is not running, start it.", "Error", 0)