import tkinter as tk
from tkinter import messagebox, simpledialog, Scale, filedialog
import subprocess
import psutil
import threading


def get_java_version():
    result = subprocess.run(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if "version" in str(result.stdout):
        return str(result.stdout).split("\\n")[0].split("\"")[1]
    else:
        return None


def install_java():
    java_version = get_java_version()
    if java_version is None:
        answer = messagebox.askyesno("Frage", "Java ist nicht installiert. Möchten Sie es installieren?")
        if answer:
            subprocess.run(["choco", "install", "openjdk17"], shell=True)
            messagebox.showinfo("Information", "Java 17 wurde erfolgreich installiert!")
        else:
            messagebox.showinfo("Information", "Java wurde nicht installiert.")
    else:
        messagebox.showinfo("Information",
                            f"Java ist bereits installiert. Die installierte Version ist {java_version}.")


def read_output(process, console):
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            console.insert(tk.END, output.strip().decode() + '\n')
            console.see(tk.END)


def create_server(server_jar_path, ram_allocation, console, server_dir):
    command = f"java -Xmx{ram_allocation}G -Xms{ram_allocation}G -jar {server_jar_path} nogui"
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=server_dir)
    threading.Thread(target=read_output, args=(process, console)).start()
    return process


def create_gui():
    window = tk.Tk()
    window.title("CookieTeam Server Manager")

    install_java()

    ram_allocation = Scale(window, from_=2, to=psutil.virtual_memory().total // (1024 ** 3), orient=tk.HORIZONTAL)
    ram_allocation.pack()

    console = tk.Text(window)
    console.pack()

    server_process = None

    def start_server():
        nonlocal server_process
        server_jar_path = filedialog.askopenfilename(title="Wählen Sie die Server-JAR-Datei aus",
                                                     filetypes=[("JAR Files", "*.jar")])
        server_dir = filedialog.askdirectory(title="Wählen Sie den Speicherort des Servers aus")
        server_process = create_server(server_jar_path, ram_allocation.get(), console, server_dir)

    def stop_server():
        nonlocal server_process
        if server_process is not None:
            server_process.terminate()
            server_process = None
            messagebox.showinfo("Information", "Der Server wurde gestoppt.")

    def send_command(command_entrys):
        nonlocal server_process
        if server_process is not None:
            command = command_entrys.get() + '\n'
            server_process.stdin.write(command.encode())
            server_process.stdin.flush()
            command_entrys.delete(0, tk.END)

    def on_close():
        nonlocal server_process
        if server_process is not None:
            server_process.terminate()
        window.destroy()

    btn_start_server = tk.Button(window, text="Starte Server", command=start_server)
    btn_start_server.pack()

    btn_stop_server = tk.Button(window, text="Stoppe Server", command=stop_server)
    btn_stop_server.pack()

    command_entry = tk.Entry(window)
    command_entry.pack()

    btn_send_command = tk.Button(window, text="Sende Befehl", command=lambda: send_command(command_entry))
    btn_send_command.pack()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()


create_gui()
