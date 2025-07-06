import os

def launch_app(cmd):
    if "notepad" in cmd:
        os.system("start notepad")
        return "Opening Notepad."
    elif "chrome" in cmd:
        os.system("start chrome")
        return "Launching Google Chrome."
    elif "vs code" in cmd or "vscode" in cmd:
        os.system("code")
        return "Opening VS Code."
    else:
        return "I couldn't find that app yet."
