import serial
import re
import argparse
from pynput.keyboard import Controller, Key

# Set up argument parser
parser = argparse.ArgumentParser(description="Read data from a serial port and simulate keystrokes.")
parser.add_argument('-p', '--port', required=True, help="The serial port to use (e.g., /dev/ttyUSB0 on Linux or COM3 on Windows)")
parser.add_argument('-b', '--baud', type=int, default=9600, help="Baud rate (default: 9600)")
parser.add_argument('-d', '--databits', type=int, choices=[5, 6, 7, 8], default=8, help="Number of data bits (default: 8)")
parser.add_argument('-s', '--stopbits', type=float, choices=[1, 1.5, 2], default=1, help="Number of stop bits (default: 1)")
parser.add_argument('--parity', choices=['N', 'E', 'O', 'M', 'S'], default='N', help="Parity (default: N)")
parser.add_argument('-r', '--regex', default=r'(-?[0-9]+\.?[0-9]*)', help="Custom regex for matching (default: '(-?[0-9]+\.?[0-9]*)')")
parser.add_argument('-e', '--encoding', default='ASCII', help="Encoding for serial data (default: ASCII)")

# Parse arguments
args = parser.parse_args()

# Create a keyboard controller
keyboard = Controller()

try:
    # Configure the serial port
    ser = serial.Serial(
        port=args.port,
        baudrate=args.baud,
        bytesize=args.databits,
        parity=args.parity,
        stopbits=args.stopbits,
        timeout=1
    )
    print(f"Successfully opened {args.port}")

    while True:
        # Read a line from the serial port
        try:
            line = ser.readline().decode(args.encoding, errors='strict').strip()
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            break
        except UnicodeDecodeError as e:
            print(f"Error decoding data: {e}. This might indicate a serial port misconfiguration.")
            break

        if line:
            print("Received:", repr(line))  # Use repr to show non-printable characters

            # Extract the match using the provided regex
            match = re.search(args.regex, line)
            if match:
                full_match = match.group(0)  # The entire matched string
                extracted = match.group(1)  # The content of the first capturing group
                print("Full match:", repr(full_match))
                print("Extracted:", repr(extracted))

                # Simulate keystrokes
                keyboard.type(extracted)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            else:
                print("No match found with the given regex.")

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print(f"Closed {args.port}")
