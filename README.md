# Minecraft Server Creator
This is a simple script that creates a Minecraft server on your computer. It is written in Python and uses the `subprocess` module to run the server. It also uses the `os` module to create the server files and directories.
<br/>
<br/>
When you see are Errors or Bugs, please report them in the Issues tab. When you have any ideas or suggestions, please report them in the Issues tab too.
### Program Language
Python <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/>
<br/>
### Programed by
noting yet
### Tested on
<p>X = Does not work</p>
<p>| = Probably works</p>
<p>✓ = Tested works 100%</p>
<table>
<tbody>
<tr>
<td>OS→<br/>Python↓&nbsp;</td>
<td><img src="https://seeklogo.com/images/W/windows-10-icon-logo-5BC5C69712-seeklogo.com.png" width="25" height="25" alt="win10">&nbsp;</td>
<td><img src="https://i.imgur.com/d4TKyFD.png" height="25" alt="win11">&nbsp;</td>
<td><img src="https://cdn-icons-png.flaticon.com/512/518/518713.png" height="29" alt="linux">&nbsp;</td>
<td><img src="https://cdn-icons-png.flaticon.com/512/2/2235.png" height="25" alt="mac">&nbsp;</td>
</tr>
<tr>
<td>3.12&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.11&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.10&nbsp;</td>
<td>✓&nbsp;</td>
<td>✓&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.9&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
</tbody>
</table>

### How to use
1. Go to Releases and download the latest version.
2. Start the downloaded file (If Java is not installed, the program will close and you have to download Java).
3. Then choose the amount of RAM you want to allocate to the server (on the top of the window).
4. Press "Starte Server" and then first choose your Server Jar (You can download a Server Jar from here: [Paper](https://papermc.io/)).
5. Then choose the directory where the server files should be located.
6. Voilà! The server is now running, and you can connect to it with the IP: `localhost`.

### PyInstaller Command
First you need to install PyInstaller with the following command:
```
pip install pyinstaller
```
Then you can use the following command to create a executable file:
```
pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --name "Server Client" --hide-console "hide-early"  "main.py"
```
Your executable file is now in the `dist` directory.

### To-Do List
- [ ] Create a simple GUI and Beautify it
- [ ] Add a function to automatically download the server jar
- [ ] Add Multi-Language Support
- [ ] Add Multi-OS Support
- [ ] Add Mod Support (Forge and Fabric)
- [ ] Add a function to automatically download Modpacks
- [ ] Add a function to automatically download Plugins
- [ ] Add a function to automatically download Resourcepacks
- [ ] Add a function to automatically download Maps (maybe)
- [ ] Made the server settings customizable
- [ ] Add a function to automatically update the server
- [ ] Add a function to backup the server
- [ ] Add a function to automatically restart the server

### Known Bugs
Nothing yet

---
# Minecraft Server Creator (German)
Dies ist ein einfaches Skript, das einen Minecraft-Server auf Ihrem Computer erstellt. Es ist in Python geschrieben und benutzt das `subprocess` Modul um den Server zu starten. Außerdem verwendet es das Modul `os`, um die Serverdateien und -verzeichnisse zu erstellen.<br/>
<br/>
Wenn Sie Fehler oder Bugs entdecken, melden Sie diese bitte auf der Registerkarte "Probleme". Wenn Sie Ideen oder Vorschläge haben, melden Sie diese bitte auch auf der Registerkarte "Probleme".### Program Language
Python <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/>
<br/>
### Programed by
noting yet
### Tested on
<p>X = Funktioniert nicht</p>
<p>| = Funktioniert vieleicht</p>
<p>✓ = Funktioniert zu 100 %</p>
<table>
<tbody>
<tr>
<td>OS→<br/>Python↓&nbsp;</td>
<td><img src="https://seeklogo.com/images/W/windows-10-icon-logo-5BC5C69712-seeklogo.com.png" width="25" height="25" alt="win10">&nbsp;</td>
<td><img src="https://i.imgur.com/d4TKyFD.png" height="25" alt="win11">&nbsp;</td>
<td><img src="https://cdn-icons-png.flaticon.com/512/518/518713.png" height="29" alt="linux">&nbsp;</td>
<td><img src="https://cdn-icons-png.flaticon.com/512/2/2235.png" height="25" alt="mac">&nbsp;</td>
</tr>
<tr>
<td>3.12&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.11&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.10&nbsp;</td>
<td>✓&nbsp;</td>
<td>✓&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
<tr>
<td>3.9&nbsp;</td>
<td>I&nbsp;</td>
<td>I&nbsp;</td>
<td>X&nbsp;</td>
<td>X&nbsp;</td>
</tr>
</tbody>
</table>

### How to use
1. Gehen Sie zu Releases und laden Sie die neuste Version herunter.
2. Starten Sie die heruntergeladene Datei (Wenn Java nicht installiert ist, schließt sich das Programm und sie müssen Java herunterladen).
3. Wählen Sie dann die Menge des Arbeitsspeichers, die Sie dem Server zuweisen möchten (oben im Fenster).
4. Drücken Sie auf "Starte Server" und wählen Sie dann zuerst Ihr Server Jar (Sie können ein Server Jar von hier herunterladen: [Paper](https://papermc.io/)).
5. Wählen Sie dann das Verzeichnis, in dem die Serverdateien gespeichert werden sollen.
6. Voilà! Der Server läuft jetzt, und Sie können sich mit der IP-Adresse `localhost` mit ihm verbinden.

### PyInstaller Command
Zuerst müssen Sie PyInstaller mit dem folgenden Befehl installieren:
```
pip install pyinstaller
```
Dann können Sie den folgenden Befehl verwenden, um eine ausführbare Datei zu erstellen:
```
pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --name "Server Client" --hide-console "hide-early"  "main.py"
```
Ihre ausführbare Datei befindet sich jetzt im Verzeichnis `dist`.

### To-Do-Liste
- [ ] Eine einfache GUI erstellen und verschönern
- [ ] Funktion zum automatischen Download des Server-Jars hinzufügen
- [ ] Mehrsprachige Unterstützung hinzufügen
- [ ] Multi-OS-Unterstützung hinzufügen
- [ ] Mod-Unterstützung hinzufügen (Forge und Fabric)
- [ ] Hinzufügen einer Funktion zum automatischen Herunterladen von Modpacks
- [ ] Funktion zum automatischen Herunterladen von Plugins hinzufügen
- [ ] Funktion zum automatischen Herunterladen von Resourcepacks hinzufügen
- [ ] Funktion zum automatischen Herunterladen von Maps hinzufügen (vielleicht)
- [ ] Servereinstellungen anpassbar machen
- [ ] Funktion zum automatischen Aktualisieren des Servers hinzufügen
- [ ] Funktion zum Sichern des Servers hinzufügen
- [ ] Funktion zum automatischen Neustart des Servers hinzufügen

### Bekannte Fehler
Noch keine
