import os
import ctypes
import winreg as reg

# Disable USB ports
usb_key = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
try:
    reg.CreateKey(reg.HKEY_LOCAL_MACHINE, usb_key)
    reg.SetValueEx(reg.HKEY_LOCAL_MACHINE, os.path.join(usb_key, "Start"), 0, reg.REG_DWORD, 4)
except Exception as e:
    print("Error:", e)

# Disable Bluetooth
bt_key = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters"
try:
    reg.CreateKey(reg.HKEY_LOCAL_MACHINE, bt_key)
    reg.SetValueEx(reg.HKEY_LOCAL_MACHINE, os.path.join(bt_key, "BluetoothEnabled"), 0, reg.REG_DWORD, 0)
except Exception as e:
    print("Error:", e)

# Restrict Command Prompt
try:
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 128)
except Exception as e:
    print("Error:", e)

# Modify hosts file to block facebook.com
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
try:
    with open(hosts_path, "a") as file:
        file.write("\n127.0.0.1 facebook.com")
except Exception as e:
    print("Error:", e)