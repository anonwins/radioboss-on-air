# radioboss-on-air
 Lights a light through parallel port, whenever Radioboss is using the microphone.

### Usage

List of accepted arguments:

<table><tbody><tr><td><i>argument:</i></td><td><i>description:</i></td><td><i>default value:</i></td></tr><tr><td><strong>-h, --help</strong></td><td>show help message and exit</td><td>&nbsp;</td></tr><tr><td><strong>--rb-path RB_PATH</strong></td><td>Full path to radioboss.exe</td><td><strong>C:\Program Files\RadioBoss\Radioboss.exe</strong></td></tr><tr><td><strong>--port PORT</strong></td><td>The LPT port address.</td><td><strong>888</strong></td></tr><tr><td><strong>--on-value ON_VALUE</strong></td><td>The LPT value for ON.</td><td><strong>255</strong></td></tr><tr><td><strong>--off-value OFF_VALUE</strong></td><td>The LPT value for OFF.</td><td><strong>0</strong></td></tr><tr><td><strong>--interval INTERVAL</strong></td><td>Number of seconds between each check.</td><td><strong>1</strong></td></tr><tr><td><strong>--initial-state {on,off}</strong></td><td>Forces this state on load.</td><td><strong>off</strong></td></tr><tr><td><strong>--turn-off-on-error {yes,no}</strong></td><td>Turn light off in case of status reading error.</td><td><strong>yes</strong></td></tr></tbody></table>