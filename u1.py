import usb.core
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend()
dev = usb.core.find(backend=backend)
if dev is None:
    raise ValueError('Device not found')
