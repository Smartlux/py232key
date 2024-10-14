# py232key

This Python script reads data from a serial port, applies a regular expression to extract specific information, and simulates keystrokes based on the extracted data. It's useful for automating data entry from measuring devices with an RS-232 port, such as scales and balances.

## Features

- Configurable serial port settings (port, baud rate, data bits, stop bits, parity)
- Custom regex pattern for data extraction (extracts first number in each line by default)
- Simulates keyboard input based on extracted data

## Requirements

- Python 3.6+
- pySerial
- pynput

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Smartlux/py232key.git
   cd py232key
   ```

2. Install the required packages:
   ```
   pip install pyserial pynput
   ```

## Usage

Run the script from the command line with the following syntax:

```
python py232key.py -p PORT [options]
```

### Required Arguments:

- `-p PORT, --port PORT`: The serial port to use (e.g., /dev/ttyUSB0 on Linux or COM3 on Windows)

### Optional Arguments:

- `-b BAUD, --baud BAUD`: Baud rate (default: 9600)
- `-d {5,6,7,8}, --databits {5,6,7,8}`: Number of data bits (default: 8)
- `-s {1,1.5,2}, --stopbits {1,1.5,2}`: Number of stop bits (default: 1)
- `--parity {N,E,O,M,S}`: Parity (default: N)
- `-r REGEX, --regex REGEX`: Custom regex for matching (default: '(-?[0-9]+\.?[0-9]*)')
- `-e ENCODING, --encoding ENCODING`: Encoding for serial data (default: ASCII)
- `-h, --help`: Show help message and exit

### Terminating the Script

To terminate the script, press `Ctrl+C` in the terminal where the script is running. This will trigger a KeyboardInterrupt, which the script catches to perform a clean shutdown, including closing the serial port.

## Examples

1. Basic usage (extract the first number using default settings):
   ```
   python py232key.py -p COM3
   ```

2. Using 2400 baud, 7 data bits, and even parity:
   ```
   python py232key.py -p COM3 -b 2400 -d 7 --parity E
   ```

3. Using a custom regex to extract numbers after 'N' with default parameters:
   ```
   python py232key.py -p COM3 -r "^N\ *?([0-9]*\.?[0-9]+)"
   ```

## How It Works

1. The script opens the specified serial port with the given settings.
2. It continually reads lines from the serial port.
3. Each line is searched for a match using the specified regex pattern.
4. If a match is found, the script extracts the data from the first capturing group and simulates typing it, followed by pressing Enter.
5. The process repeats until the script is terminated or an error occurs.

### Line Termination

The `ser.readline()` function reads until it encounters a line terminator. By default, it recognizes the following as line terminators:

- `\n` (LF, line feed)
- `\r` (CR, carriage return)
- `\r\n` (CRLF, carriage return + line feed)

If your serial device uses a different line terminator, you may need to modify the script to handle it appropriately.

## Error Handling

The script includes error handling for common issues:
- Serial port connection errors
- Data decoding errors
- Regex matching failures

Error messages are printed to the console for debugging purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). This license allows commercial use but requires that any modifications to the code must be made available under the same open-source terms. For more details, see the [LICENSE](LICENSE) file or visit [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Asking for help

Before asking for help, please ensure that your serial device is properly configured and sending data to the specified port. You can test this using a terminal application to confirm that data is being received.

Here are some recommended terminal applications:

- **Windows**: [HTerm](https://www.der-hammer.info/pages/terminal.html)
- **Linux**: `minicom`
- **macOS**: [CoolTerm](https://freeware.the-meiers.org/)

If the device is sending data and you still encounter issues, feel free to open a GitHub issue and provide detailed information about the problem.

### Important Notice for Linux Users on Wayland

If you are using Linux with Wayland, please be aware that `pynput` is facing significant limitations which may affect the keystroke simulation functionality. For more information and updates, please refer to this issue: [pynput Issue #331](https://github.com/moses-palmer/pynput/issues/331).
