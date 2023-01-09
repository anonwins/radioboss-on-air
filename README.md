# radioboss-on-air
 Lights a light through parallel port, whenever Radioboss is using the microphone.

### Requirements

*   [ ] Windows 10+
*   [ ] Python _(not required for binary releases)_
*   [ ] Microphone
*   [ ] LPT relay to control the ON-AIR light
*   [ ] Radioboss ([https://www.djsoft.net](https://www.djsoft.net/))
*   [ ] PyInstaller _(required for compiling to EXE)_ (pip install pyinstaller)
*   [ ] PyInstaller-Versionfile _(required for compiling to EXE)_ (pip install pyinstaller-versionfile)

### Usage

List of accepted arguments:

<table><tbody>
<tr><td><i>argument:</i></td><td><i>description:</i></td><td><i>default value:</i></td></tr>
<tr><td>-h, --help</td><td>show help message and exit</td><td>&nbsp;</td></tr>
<tr><td>--rb-path RB_PATH</td><td>Full path to radioboss.exe</td><td>C:\Program Files\RadioBoss\Radioboss.exe</td></tr>
<tr><td>--port PORT</td><td>The LPT port address.</td><td>888</td></tr>
<tr><td>--on-value ON_VALUE</td><td>The LPT value for ON.</td><td>255</td></tr>
<tr><td>--off-value OFF_VALUE</td><td>The LPT value for OFF.</td><td>0</td></tr>
<tr><td>--interval INTERVAL</td><td>Number of seconds between each check.</td><td>1</td></tr>
<tr><td>--initial-state {on,off}</td><td>Forces this state on load.</td><td>off</td></tr>
<tr><td>--turn-off-on-error {yes,no}</td><td>Turn light off in case of status reading error.</td><td>yes</td></tr>
</tbody></table>

### Compile to EXE

Compiling to exe allows you to run the script on machines with no python installed.

Simply run _**compile\_to\_exe.bat**_