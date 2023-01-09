## radioboss-on-air

Lights a light through parallel port, whenever Radioboss is using the microphone.

### Requirements

*   Windows 10+
*   Python _(not required for binary releases)_
*   Microphone
*   LPT relay to control the ON-AIR light
*   Radioboss ([https://www.djsoft.net](https://www.djsoft.net/))
*   PyInstaller _(required for compiling to EXE)_ (pip install pyinstaller)
*   PyInstaller-Versionfile _(required for compiling to EXE)_ (pip install pyinstaller-versionfile)

### Usage

List of accepted arguments:

<table><tbody><tr><td><i>argument:</i></td><td><i>description:</i></td><td><i>default value:</i></td></tr><tr><td>-h, --help</td><td>show help message and exit</td><td>&nbsp;</td></tr><tr><td>--rb-path RB_PATH</td><td>Full path to radioboss.exe</td><td>C:\Program Files\RadioBoss\Radioboss.exe</td></tr><tr><td>--port PORT</td><td>The LPT port address.</td><td>888</td></tr><tr><td>--on-value ON_VALUE</td><td>The LPT value for ON.</td><td>255</td></tr><tr><td>--off-value OFF_VALUE</td><td>The LPT value for OFF.</td><td>0</td></tr><tr><td>--interval INTERVAL</td><td>Number of seconds between each check.</td><td>1</td></tr><tr><td>--initial-state {on,off}</td><td>Forces this state on load.</td><td>off</td></tr><tr><td>--turn-off-on-error {yes,no}</td><td>Turn light off in case of status reading error.</td><td>yes</td></tr><tr><td>--start-minimized {yes,no}</td><td>Automatically minimize the window when the script loads.</td><td>no</td></tr></tbody></table>

### Compile to EXE

Compiling to exe allows you to run the script on machines with no python installed. You can also get the EXE from /releases.

Simply run _**compile\_to\_exe.bat**_

### Some things to note

1.  Inpoutx64.dll is included. You'll have to tweek the script a bit if you want to use inpout32.dll. The compiled EXE contains the dll inside.
2.  The port is decimal so 0x378 is 888 (the default).
3.  The values are 8-bit integers so 0-255.
4.  If you get Radioboss Registry error make sure you've used the microphone at least once with radioboss.