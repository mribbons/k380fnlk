# K380 Function Key Toggle

## Overview

This utility allows you to toggle the function key behavior on the **Logitech K380 Bluetooth Keyboard** on Windows, macOS, and Linux **without** needing Logitech's official software.

By default, the K380 keyboard uses **media keys** (e.g., volume control) instead of function keys (F1-F12). This tool lets you switch between **function keys as default** or **media keys as default**.

### Cross-Platform Support

✅ This utility works on **Windows, macOS, and Linux**, ensuring a consistent experience across different operating systems.

## Features

- ✅ **Enable function keys** as default (F1–F12 work normally without Fn key)
- ✅ **Disable function keys** (media keys as default, F1–F12 require Fn key)
- ✅ **Works on Windows, macOS, and Linux**
- ✅ **No background processes** required

## Installation

### 1. Install Dependencies

#### Windows

1. Install Python (if not already installed): [Download Python](https://www.python.org/downloads/)
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

#### macOS

1. Install `hidapi` via Homebrew:
   ```sh
   brew install hidapi
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. If you encounter permission issues, grant **Full Disk Access** to your terminal in **System Preferences > Security & Privacy > Privacy**.

#### Linux

1. Install `hidapi`:
   ```sh
   sudo apt update
   sudo apt install libhidapi-libusb0 libhidapi-hidraw0
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. (Optional) If you get permission errors, add a **udev rule**:
   ```sh
   sudo nano /etc/udev/rules.d/99-k380.rules
   ```
   Add this line:
   ```
   SUBSYSTEM=="hidraw", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="b342", MODE="0666"
   ```
   Reload rules:
   ```sh
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

---

## Usage

Run the script with one of the following options:

### Enable Function Keys as Default (F1–F12 work normally without Fn key)

```sh
python3 set_k380_fkeys.py --enable
```

### Disable Function Keys (media keys as default, F1–F12 require Fn key)

```sh
python3 set_k380_fkeys.py --disable
```

If you get a permission error on **Linux/macOS**, try running it with `sudo`:

```sh
sudo python3 set_k380_fkeys.py --enable
```

---

## Troubleshooting

### 1. "K380 keyboard not found."

- Ensure the keyboard is connected via Bluetooth.
- Try disconnecting and reconnecting the keyboard.
- Run the script with `sudo` (Linux/macOS):
  ```sh
  sudo python3 set_k380_fkeys.py --enable
  ```

### 2. "Failed to send HID command."

- On **Linux**, add the **udev rule** (see Installation section) and restart your system.
- On **macOS**, check **System Preferences > Security & Privacy > Privacy** and grant Full Disk Access to your terminal.
- On **Windows**, try running the script as an administrator.

### 3. "ModuleNotFoundError: No module named 'hid'"

- Run:
  ```sh
  pip install --force-reinstall hidapi
  ```

---

## Contributing

Feel free to submit **pull requests** or open **issues** for improvements!

1. Fork this repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to your fork:
   ```sh
   git push origin feature-branch
   ```
5. Open a pull request.

---

## License

MIT License. See `LICENSE` for details.

---

## Acknowledgments

This project is inspired by:

- [k810fn](https://github.com/keighrim/k810fn)
- [k380-function-keys-conf](https://github.com/jergusg/k380-function-keys-conf)
- [k380-fn-lock-for-windows](https://github.com/dheygere/k380-fn-lock-for-windows)

Enjoy your function keys! 🎉

