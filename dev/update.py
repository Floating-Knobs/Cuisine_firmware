import os
import platform
import serial.tools.list_ports

def find_com_port():
    ports = list(serial.tools.list_ports.comports())
    
    for port in ports:
        if "USB" in port.description.upper():
            return port.device

    return None

def find_hex_file(folder="."):
    for file in os.listdir(folder):
        if file.endswith(".hex"):
            return os.path.join(folder, file)
    
    return None

def upload_hex_file(hex_file_path=None, com_port=None):
    if com_port is None:
        com_port = find_com_port()

    if com_port is None:
        print("Error: Could not find the COM port. Please connect the MCU.")
        return

    if hex_file_path is None:
        hex_file_path = find_hex_file()
        
        if hex_file_path is None:
            print("Error: No .hex file found in the folder.")
            return

    avrdude_command = (
        f"avrdude -C ./avrdude.conf -c arduino -D "
        f"-b 115200 -p atmega4809 -P \"{com_port}\" -U flash:w:{hex_file_path}:i"
    )

    print(f"Uploading hex file {hex_file_path} to MCU on {com_port}...")
    os.system(avrdude_command)
    print("Upload complete.")

if __name__ == "__main__":
    upload_hex_file()
# python c:/Python312/Lib/site-packages/pyinstaller --onefile update.py
