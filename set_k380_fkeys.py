import hid
import argparse
import sys

# Constants
K380_VID = 0x46D  # Logitech Vendor ID
K380_PID = 0xB342  # K380 Product ID
TARGET_USAGE = 1
TARGET_USAGE_PAGE = 65280

# HID sequences for function keys
K380_SEQ_FKEYS_ON = bytes([0x10, 0xFF, 0x0B, 0x1E, 0x00, 0x00, 0x00])
K380_SEQ_FKEYS_OFF = bytes([0x10, 0xFF, 0x0B, 0x1E, 0x01, 0x00, 0x00])

def set_function_keys(enable):
    """Enable or disable function keys as default on Logitech K380 keyboard."""
    try:
        # Enumerate devices
        for device in hid.enumerate():
            if device['vendor_id'] == K380_VID and device['product_id'] == K380_PID:
                if device['usage'] == TARGET_USAGE and device['usage_page'] == TARGET_USAGE_PAGE:
                    print(f"Found K380 keyboard: {device['path']}")

                    h = hid.device()
                    h.open_path(device['path'])  # Open using device path

                    print(f"K380 keyboard opened. Setting function keys to {'ON' if enable else 'OFF'}...")
                    
                    data = K380_SEQ_FKEYS_ON if enable else K380_SEQ_FKEYS_OFF

                    # Try normal write first
                    res = h.write(data)
                    if res < 0:
                        print("Write failed. Trying send_feature_report()...")
                        res = h.send_feature_report(data)
                    
                    if res < 0:
                        print("Error: Failed to send HID command.")
                    else:
                        print(f"Function keys successfully set to {'ON' if enable else 'OFF'}.")
                    
                    h.close()
                    return res >= 0
        
        print("K380 keyboard not found.")
    except Exception as e:
        print(f"Error: {e}")
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enable or disable function keys on Logitech K380 keyboard.")
    parser.add_argument("--enable", action="store_true", help="Enable function keys (F1-F12 as default).")
    parser.add_argument("--disable", action="store_true", help="Disable function keys (media keys as default).")

    args = parser.parse_args()

    if args.enable and args.disable:
        print("Error: Cannot use --enable and --disable together.")
        sys.exit(1)
    elif args.enable:
        set_function_keys(True)
    elif args.disable:
        set_function_keys(False)
    else:
        print("Error: You must specify either --enable or --disable.")
        sys.exit(1)
