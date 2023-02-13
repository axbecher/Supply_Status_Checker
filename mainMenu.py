import tkinter as tk
import subprocess

def saveCredentials():
    subprocess.call("python saveCredentials.py", shell=True)
    runScriptButton.config(state="normal")

def saveURL():
    subprocess.call("python saveURL.py", shell=True)
    runScriptButton.config(state="normal")

def openURLs():
    subprocess.call("open urls.txt", shell=True)

def runScript():
    subprocess.call("python main.py", shell=True)

def quitProgram():
    root.quit()

root = tk.Tk()
root.title("GUI cu 4 butoane")
root.geometry("200x200")

saveCredentialsButton = tk.Button(root, text="Save Credentials", command=saveCredentials)
saveURLButton = tk.Button(root, text="Save URL", command=saveURL)
openURLsButton = tk.Button(root, text="Open URLs", command=openURLs)
runScriptButton = tk.Button(root, text="Run Script", state="disabled", command=runScript)
quitButton = tk.Button(root, text="QUIT", command=quitProgram)

saveCredentialsButton.pack()
saveURLButton.pack()
openURLsButton.pack()
runScriptButton.pack()
quitButton.pack()

root.mainloop()