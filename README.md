# radioboss-on-air
 Lights a light through parallel port, whenever Radioboss is using the microphone.

## usage

  -h, --help            show this help message and exit
  --rb-path RB_PATH     Full path to radioboss.exe (default: C:\Program Files\RadioBoss\Radioboss.exe)
  --port PORT           The LPT port address. (default: 888)
  --on-value ON_VALUE   The LPT value for ON. (default: 255)
  --off-value OFF_VALUE
                        The LPT value for OFF. (default: 0)
  --interval INTERVAL   Number of seconds between each check. (default: 1)
  --initial-state {on,off}
                        Forces this state on load. (default: off)
  --turn-off-on-error {yes,no}
                        Turn light off in case of status reading error. (default: yes)
