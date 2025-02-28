# Emulator.py

## Overview
`emulator.py` is a Python-based emulator designed to run `.gba` ROM files. This project enables users to load and play Game Boy Advance games with basic control functionality and emulation support.

## Features
- Loads and runs `.gba` ROM files
- Provides basic controls for gameplay
- Supports save states
- Includes debugging tools for developers

## Requirements
To run `emulator.py`, you need the following dependencies installed:

- Python 3.8+
- pygame
- numpy
- pyboy (if using PyBoy for GBA emulation)
- Any additional dependencies specified in `requirements.txt`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/emulator.py.git
   ```
2. Navigate into the directory:
   ```sh
   cd emulator.py
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To start the emulator, run:
```sh
python emulator.py [path_to_rom.gba]
```
Example:
```sh
python emulator.py pokemon_firered.gba
```

## Controls
| Key | Function |
|------|----------|
| Arrow Keys | D-Pad Movement |
| A | A Button |
| S | B Button |
| Enter | Start |
| Backspace | Select |
| L | L Shoulder Button |
| R | R Shoulder Button |
| Escape | Exit Emulator |

## Save States
- Press `F5` to save the current game state
- Press `F8` to load the last saved state

## Contributing
If you would like to contribute to `emulator.py`, follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Submit a pull request

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Disclaimer
This software is intended for educational and preservation purposes. We do not condone or support piracy. Please ensure you own the ROMs you use with this emulator.

