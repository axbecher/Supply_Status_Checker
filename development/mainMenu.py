import tkinter as tk
import subprocess

def save_credentials():
    subprocess.call("python saveCredentials.py", shell=True)
    run_script_button.config(state="normal")

def save_url():
    subprocess.call("python saveURL.py", shell=True)
    run_script_button.config(state="normal")

def open_urls():
    subprocess.call("open urls.txt", shell=True)

def run_script():
    subprocess.call("python main.py", shell=True)

def quit_program():
    root.quit()

root = tk.Tk()
root.title("Supply Status Checker")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#F2F2F2")

title_label = tk.Label(root, text="Welcome!", font=("Arial", 20, "bold"), bg="#F2F2F2")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#F2F2F2")
frame.pack()

button_1 = tk.Button(frame, text="Save Authentication Data", font=("Arial", 12), width=25, height=2, bg="#BFACE2", command=save_credentials)
button_2 = tk.Button(frame, text="Save URL", font=("Arial", 12), width=25, height=2, bg="#BFACE2", command=save_url)
button_3 = tk.Button(frame, text="Open URL File", font=("Arial", 12), width=25, height=2, bg="#BFACE2", command=open_urls)

button_1.pack(pady=10)
button_2.pack(pady=10)
button_3.pack(pady=10)

script_frame = tk.Frame(root, bg="#F2F2F2")
script_frame.pack()

run_script_button = tk.Button(script_frame, text="Run Script", font=("Arial", 12), width=25, height=2, bg="#BFACE2", fg="white", state="disabled", command=run_script)
run_script_button.pack(pady=20)

quit_button = tk.Button(root, text="QUIT", font=("Arial", 12), bg="#FF5050", fg="white", width=10, command=quit_program)
quit_button.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
