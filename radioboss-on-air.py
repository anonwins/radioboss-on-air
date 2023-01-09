########################################################################
#                                                                      #
#                          RADIOBOSS-ON-AIR                            #
#                                                                      #
#                Lights a light through parallel port,                 #
#              whenever Radioboss is using the microphone.             #
#                                                                      #
########################################################################

import ctypes, sys, subprocess, os, time

########################################################################
# CONFIG                                                               #
########################################################################

RadiobossPath  = "C:\\RadioBoss-6.2.1-Portable\\radioboss.exe"

ComPort        = 888
OnValue        = 4
OffValue       = 0

CheckInterval  = 1      # in seconds
InitialState   = 'off'
TurnOffOnError = True

########################################################################
# FUNCTIONS                                                            #
########################################################################

def __DllFunc(name, ret, args):               # Loads a DLL
    func = inpout[name]
    func.restype = ret
    func.argtype = args
    return func

sign_status = False
def toggle_sign(state):                       # Turns the sign on/off
    global sign_status
    if (state=='on'): 
        code = OnValue
        sign_status = True
    elif (state=='off'):
        code = OffValue
        sign_status = False
    else: return
    inpout.DlPortWritePortUchar(ComPort,code)

def is_radioboss_using_the_mic(rb_path):      # Returns True/False if Radioboss is using the mic (string on error).
    # get reg entry value
    reg_basepath = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\microphone\\NonPackaged"
    reg_path = reg_basepath+"\\"+rb_path.replace('\\','#')
    result = subprocess.run(['reg','query',reg_path,"/v","LastUsedTimeStop"],capture_output=True)
    # check for error
    res_error = result.stderr.decode('utf-8')
    if (res_error): return res_error
    res_out = result.stdout.decode('utf-8')
    # find result line
    res_line = False
    for line in res_out.split("\n"):
        if "REG_QWORD" in line:
            res_line = line.strip()
    # check last used time
    return res_line.endswith('0x0')

########################################################################
# MAIN PROGRAM                                                         #
########################################################################

# INITIALIZE PROGRAM WINDOW
software_title = 'radioboss-on-air'
ctypes.windll.kernel32.SetConsoleTitleW(software_title)
print(software_title+'\r\n')

# LOAD INPOUT32.DLL
script_dir = os.path.dirname(os.path.realpath(__file__))
inpout = ctypes.WinDLL(script_dir+"\\inpoutx64.dll")
DlPortWritePortUchar = __DllFunc("DlPortWritePortUchar", ctypes.c_void_p, (ctypes.c_ushort, ctypes.c_ubyte))

# ENFORCE INITIAL STATE
print('Setting initial state: '+InitialState)
toggle_sign(InitialState)

# START THE LOOP
failed = False
while True:

    # GET RADIOBOSS MIC STATUS
    new_state = False
    rb_status = is_radioboss_using_the_mic(RadiobossPath)

    if (rb_status==True):                        # ON AIR
        if (not sign_status): new_state = 'on'

    elif (rb_status==False):                     # OFF AIR
        if (sign_status): new_state = 'off'

    else:                                        # ERROR
        if (not failed):
            print('Could not locate registry value. Is Radioboss installed and running?')
            failed = True
            if (TurnOffOnError): toggle_sign('off')

    # CHANGE THE STATE IF NEEDED
    if (new_state):
        print('Changing state: '+new_state)
        toggle_sign(new_state)
        if (failed): failed = False

    time.sleep(CheckInterval)