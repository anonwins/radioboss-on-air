########################################################################
#                                                                      #
#                          RADIOBOSS-ON-AIR                            #
#                                                                      #
#                Lights a light through parallel port,                 #
#              whenever Radioboss is using the microphone.             #
#                                                                      #
########################################################################

import ctypes, sys, subprocess, os, time, argparse, signal
from os.path import exists

########################################################################
# CONFIG                                                               #
########################################################################

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--rb-path',default="C:\\Program Files\\RadioBoss\\Radioboss.exe",help="Full path to radioboss.exe (default: C:\\Program Files\\RadioBoss\\Radioboss.exe)")
parser.add_argument('--port',default=888,type=int,help="The LPT port address. (default: 888) (not used when --hardware-instance is provided)")
parser.add_argument('--on-value',default=255,type=int,help="The LPT value for ON. (default: 255) (not used when --hardware-instance is provided)")
parser.add_argument('--off-value',default=0,type=int,help="The LPT value for OFF. (default: 0) (not used when --hardware-instance is provided)")
parser.add_argument('--interval',default=1,type=float,help="Number of seconds between each check. (default: 1)")
parser.add_argument('--initial-state',default="off",choices=['on','off'],help="Force this state on load. (default: off)")
parser.add_argument('--turn-off-on-error',default="yes",choices=['yes','no'],help="Turn light off in case of status reading error. (default: yes)")
parser.add_argument('--turn-off-on-exit',default="yes",choices=['yes','no'],help="Turn off the light before exiting. (default: yes)")
parser.add_argument('--start-minimized',default="no",choices=['yes','no'],help="Automatically minimize the window when the script loads. (default: no)")
parser.add_argument('--hardware-id',default="",help="If you provide that, port and values won't be used.")
args = parser.parse_args()

# minimize window if requested
if (args.start_minimized=='yes'):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),6)

########################################################################
# FUNCTIONS                                                            #
########################################################################

def __DllFunc(name, ret, args):               # Loads a DLL
    func = inpout[name]
    func.restype = ret
    func.argtype = args
    return func

light_status = False
def toggle_light(state):                       # Turns the light on/off
    global light_status
    if (state=='on'): 
        code = args.on_value
        light_status = True
        command = '/enable-device'
    elif (state=='off'):
        code = args.off_value
        light_status = False
        command = '/disable-device'
    else: return
    if (args.hardware_instance==""):
        inpout.DlPortWritePortUchar(args.port,code)
    else:
        result = subprocess.run(['pnputil',command,args.hardware_instance],capture_output=True)

def is_radioboss_using_the_mic(rb_path):      # Returns True/False if Radioboss is using the mic (string on error).
    # get reg entry value
    reg_basepath = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\microphone\\NonPackaged"
    reg_path = reg_basepath+"\\"+rb_path.replace('\\','#')
    result = subprocess.run(['reg','query',reg_path,"/v","LastUsedTimeStop"],capture_output=True)
    # check for error
    res_error = result.stderr.decode('utf-8')
    if (res_error): return res_error
    # find result line
    res_out = result.stdout.decode('utf-8')
    res_line = False
    for line in res_out.split("\n"):
        if "REG_QWORD" in line:
            res_line = line.strip()
    # check last used time
    return res_line.endswith('0x0')

def exit_gracefully():                        # Exits without KeyboardInterrupt, and sets final light state.
    if (args.turn_off_on_exit=='yes'):
        print('Setting final state: off')
        toggle_light('off')
    sys.exit(0)

########################################################################
# MAIN PROGRAM                                                         #
########################################################################

# REGISTER A GRACEFUL EXIT
signal.signal(signal.SIGINT, lambda x, y: exit_gracefully())

# EXIT IF RADIOBOSS.EXE CANNOT BE  FOUND
if (not exists(args.rb_path)):
    print('Radioboss executable not found. Specify with --rb-path. See -h for help.')
    sys.exit(0)

# INITIALIZE PROGRAM WINDOW
software_title = 'radioboss-on-air'
ctypes.windll.kernel32.SetConsoleTitleW(software_title)

# LOAD INPOUT32.DLL
script_dir = os.path.dirname(os.path.realpath(__file__))
inpout = ctypes.WinDLL(script_dir+"\\inpoutx64.dll")
DlPortWritePortUchar = __DllFunc("DlPortWritePortUchar", ctypes.c_void_p, (ctypes.c_ushort, ctypes.c_ubyte))

# ENFORCE INITIAL STATE
print('Setting initial state: '+args.initial_state)
toggle_light(args.initial_state)

# START THE LOOP
failed = False
while True:

    # GET RADIOBOSS MIC STATUS
    new_state = False
    rb_status = is_radioboss_using_the_mic(args.rb_path)

    if (rb_status==True):                        # ON AIR
        if (not light_status): new_state = 'on'

    elif (rb_status==False):                     # OFF AIR
        if (light_status): new_state = 'off'

    else:                                        # ERROR
        if (not failed):
            print('Could not locate registry value. You must use mic with Radioboss at least once.')
            failed = True
            if (args.turn_off_on_error=='yes'): toggle_light('off')

    # CHANGE THE STATE IF NEEDED
    if (new_state):
        if (failed):
            print('Radioboss registry located.')
            failed = False
        print('Changing state: '+new_state)
        toggle_light(new_state)

    time.sleep(args.interval)