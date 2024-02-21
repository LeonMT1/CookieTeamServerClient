import tkinter as tk
from tkinter import messagebox, simpledialog, Scale, filedialog
import subprocess
import psutil
import threading
import os
import json

path_file = "paths.json"


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


def save_paths(server_jar_path, server_dir):
    with open(path_file, 'w') as f:
        json.dump({"server_jar_path": server_jar_path, "server_dir": server_dir}, f)


def load_paths():
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            paths = json.load(f)
            return paths["server_jar_path"], paths["server_dir"]
    else:
        return None, None


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
        server_jar_path, server_dir = load_paths()
        if server_jar_path is None and server_dir is None or server_jar_path == "" and server_dir == "":
            server_jar_path = filedialog.askopenfilename(title="Wählen Sie die Server-JAR-Datei aus",
                                                         filetypes=[("JAR Files", "*.jar")])
            server_dir = filedialog.askdirectory(title="Wählen Sie den Speicherort des Servers aus")
        server_process = create_server(server_jar_path, ram_allocation.get(), console, server_dir)
        save_paths(server_jar_path, server_dir)
        if server_jar_path == "" or server_jar_path is None:
            messagebox.showerror("Fehler", "Es wurde keine Server-JAR-Datei ausgewählt\n Bitte wähle jetzt eine aus.")
            server_jar_path = filedialog.askopenfilename(title="Wählen Sie die Server-JAR-Datei aus",
                                                         filetypes=[("JAR Files", "*.jar")])
            save_paths(server_jar_path, server_dir)
        if server_dir == "" or server_dir is None:
            messagebox.showerror("Fehler", "Es wurde kein Speicherort ausgewählt\n Bitte wähle jetzt einen aus.")
            server_dir = filedialog.askdirectory(title="Wählen Sie den Speicherort des Servers aus")
            save_paths(server_jar_path, server_dir)

    def stop_server():
        nonlocal server_process
        if server_process is not None:
            server_process.terminate()
            server_process = None
            messagebox.showinfo("Information", "Der Server wurde gestoppt.")

    def restart_server():
        nonlocal server_process
        if server_process is not None:
            server_process.terminate()
            server_process = None
            messagebox.showinfo("Information", "Der Server wird neu gestartet.")
            start_server()

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

    def settings_page():
        settings_window = tk.Toplevel(window)
        settings_window.title("Einstellungen")

        def update_labels():
            server_jar_path, server_dir = load_paths()
            if server_jar_path is None:
                server_jar_path = "Keine Server-JAR-Datei ausgewählt"
            if server_dir is None:
                server_dir = "Kein Speicherort ausgewählt"
            btn_text_javapath.config(text=f"{server_jar_path}")
            btn_text_serverdir.config(text=f"{server_dir}")

        def java_path():
            java_path = filedialog.askopenfilename(title="Wählen Sie den Pfad zu Java aus",
                                                   filetypes=[("JAR Files", "*.jar")])
            subprocess.run(["setx", "JAVA_HOME", java_path], shell=True)
            server_jar_path, server_dir = load_paths()
            save_paths(java_path, server_dir)
            messagebox.showinfo("Information", "Der Pfad zu Java wurde erfolgreich gesetzt.")
            update_labels()

        def directory_path():
            server_dir = filedialog.askdirectory(title="Wählen Sie den Speicherort des Servers aus")
            save_paths(server_jar_path, server_dir)
            messagebox.showinfo("Information", "Der Speicherort des Servers wurde erfolgreich gesetzt.")
            update_labels()

        server_jar_path, server_dir = load_paths()
        if server_jar_path is None:
            server_jar_path = "Keine Server-JAR-Datei ausgewählt"
        if server_dir is None:
            server_dir = "Kein Speicherort ausgewählt"

        btn_java_ = tk.Button(settings_window, text="Java Pfad setzen", command=java_path)
        btn_java_.pack()

        btn_directory_ = tk.Button(settings_window, text="Server Ordner setzen", command=directory_path)
        btn_directory_.pack()

        btn_text_javapath = tk.Label(settings_window, text=f"{server_jar_path}")
        btn_text_javapath.pack()

        btn_text_serverdir = tk.Label(settings_window, text=f"{server_dir}")
        btn_text_serverdir.pack()

    btn_settings = tk.Button(window, text="Einstellungen", command=settings_page)
    btn_settings.pack()

    btn_start_server = tk.Button(window, text="Starte Server", command=start_server)
    btn_start_server.pack()

    btn_stop_server = tk.Button(window, text="Stoppe Server", command=stop_server)
    btn_stop_server.pack()

    btn_restart_server = tk.Button(window, text="Server neu starten", command=restart_server)
    btn_restart_server.pack()

    command_entry = tk.Entry(window)
    command_entry.pack()

    btn_send_command = tk.Button(window, text="Sende Befehl", command=lambda: send_command(command_entry))
    btn_send_command.pack()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()


create_gui()
