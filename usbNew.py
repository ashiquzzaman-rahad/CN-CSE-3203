import usb.core
import usb.util

def list_usb_devices():
    # Find all USB devices
    devices = usb.core.find(find_all=True)
    
    # Iterate through devices and print information
    for device in devices:
        print(f"Device: {device}")
        print(f"  ID Vendor: {hex(device.idVendor)}")
        print(f"  ID Product: {hex(device.idProduct)}")
        try:
            manufacturer = usb.util.get_string(device, device.iManufacturer)
        except usb.core.USBError:
            manufacturer = None
        try:
            product = usb.util.get_string(device, device.iProduct)
        except usb.core.USBError:
            product = None
        try:
            serial_number = usb.util.get_string(device, device.iSerialNumber)
        except usb.core.USBError:
            serial_number = None
        print(f"  Manufacturer: {manufacturer}")
        print(f"  Product: {product}")
        print(f"  Serial Number: {serial_number}")
        print()

if __name__ == "__main__":
    list_usb_devices()
