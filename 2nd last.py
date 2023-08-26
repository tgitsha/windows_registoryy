import winreg

def read_registry_value(key, subkey, value_name):
    try:
        registry_key = winreg.OpenKey(key, subkey)
        value, value_type = winreg.QueryValueEx(registry_key, value_name)
        winreg.CloseKey(registry_key)
        return value
    except Exception as e:
        print("Error:", e)
        return None

# Example usage
key = winreg.HKEY_LOCAL_MACHINE
subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion"
value_name = "ProgramFilesDir"

value = read_registry_value(key, subkey, value_name)

if value is not None:
    print(f"The value of {value_name} is: {value}")