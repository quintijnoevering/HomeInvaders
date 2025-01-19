from chip import ChipStack

# Start de Matter-stack
stack = ChipStack()
devices = stack.discover_devices()

# Print gevonden apparaten
if devices:
    print("Gevonden Matter-apparaten:")
    for device in devices:
        print(f"- {device.name} (ID: {device.id})")
else:
    print("Geen apparaten gevonden.")
