# py232key

This Python script reads data from a serial port, applies a regular expression to extract specific information, and simulates keystrokes based on the extracted data. It's useful for automating data entry from measuring devices with an RS-232 port, such as scales and balances.

It is meant to be an open-source alternative to our [232key virtual keyboard wedge](https://www.232key.com) software and runs under Windows, Linux and macOS.

## Features

- Configurable serial port settings (port, baud rate, data bits, stop bits, parity)
- Custom regex pattern for data extraction (extracts first number in each line by default)
- Simulates keyboard input based on extracted data using [pynput](https://pypi.org/project/pynput/)

## Requirements

- Python 3.6+
- pySerial
- pynput

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Smartlux/py232key.git
   ```
   ```
   cd py232key
   ```
   
2. Install the required packages:
   ```
   pip install pyserial pynput
   ```

## Usage

Run the script from the command line with the following syntax:

```
python py232key.py PORT [options]
```

### Required Arguments:

- `PORT`: The serial port to use (e.g., /dev/ttyUSB0 on Linux or COM3 on Windows)

### Optional Arguments:

- `-b BAUD, --baud BAUD`: Baud rate (default: 9600)
- `-d {5,6,7,8}, --databits {5,6,7,8}`: Number of data bits (default: 8)
- `-s {1,1.5,2}, --stopbits {1,1.5,2}`: Number of stop bits (default: 1)
- `-p {N,E,O,M,S}. --parity {N,E,O,M,S}`: Parity (default: N)
- `-r REGEX, --regex REGEX`: Custom regex for matching (default: '(-?[0-9]+\.?[0-9]*)')
- `-e ENCODING, --encoding ENCODING`: Encoding for serial data (default: ASCII)
- `-h, --help`: Show help message and exit

### Terminating the Script

To terminate the script, press `Ctrl+C` in the terminal where the script is running. This will trigger a KeyboardInterrupt, which the script catches to perform a clean shutdown, including closing the serial port.

## Examples

1. Basic usage (extract the first number using default settings):
   ```
   python py232key.py /dev/ttyUSB0
   ```

2. Using 2400 baud, 7 data bits, and even parity:
   ```
   python py232key.py COM3 -b 2400 -d 7 --parity E
   ```

3. Using a custom regex to extract numbers after 'N' with default parameters:
   ```
   python py232key.py /dev/ttyUSB0 -r "^N\ *?([0-9]*\.?[0-9]+)"
   ```

## How It Works

1. The script opens the specified serial port with the given settings.
2. It continually reads lines from the serial port.
3. Each line is searched for a match using the specified regex pattern.
4. If a match is found, the script extracts the data from the first capturing group and simulates typing it, followed by pressing Enter.
5. The process repeats until the script is terminated or an error occurs.

### Line Termination

The `ser.readline()` function returns when it encounters the `\n` terminator (LF, line feed).

If your serial device uses a different line terminator, the function will return after one second (timeout).

See the [pySerial documentation](https://pyserial.readthedocs.io/en/latest/shortintro.html#shortintro-readline) for further information.

## Error Handling

The script includes error handling for common issues:
- Serial port connection errors
- Data decoding errors
- Regex matching failures

Error messages are printed to the console for debugging purposes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

Copyright 2024 Smartlux SARL.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

The name "232key" is a registered trademark of [Smartlux SARL](https://www.smartlux.com). This license does not grant any rights to use the trademarked name.

## Asking for help

Before asking for help, please ensure that your serial device is properly configured and connecting and that it is actually sending data to the specified port. You can test this using a terminal application to confirm that data is being received.

Here are some recommended terminal applications:

- **Windows**: [HTerm](https://www.der-hammer.info/pages/terminal.html)
- **Linux**: `minicom`
- **macOS**: [CoolTerm](https://freeware.the-meiers.org/)

If the device is sending data and you still encounter issues, feel free to open a GitHub issue and provide detailed information about the problem.

### Important Notice for Linux Users on Wayland

If you are using Linux with Wayland, please be aware that `pynput` is facing significant limitations which may affect the keystroke simulation functionality. For more information and updates, please refer to this issue: [pynput Issue #331](https://github.com/moses-palmer/pynput/issues/331).
