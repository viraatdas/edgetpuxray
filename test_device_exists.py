import usb.core
import usb.backend.libusb1

# Manually setting the backend to libusb1
backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/local/lib/libedgetpu.1.0.dylib")

dev = usb.core.find(idVendor=0x18d1, idProduct=0x9302, backend=backend)
if dev:
    print("Device found")
else:
    print("Device not found")
