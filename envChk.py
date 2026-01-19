import psutil, datetime
import json
import os

print("\n=== System Status ===\n")

# ==== Boot time ====
boot_timestamp = psutil.boot_time()
boot_time = datetime.datetime.fromtimestamp(boot_timestamp)
print(f"Boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

# ==== Temperature sensors ====
temps = psutil.sensors_temperatures()
print("\nTemperature sensors (readable):")

if not temps:
    print("  No temperature sensors detected.")
else:
    for sensor_name, entries in temps.items():
        print(f"  {sensor_name}:")
        for entry in entries:
            label = entry.label or "Unnamed"
            print(
                f"    {label}: "
                f"{entry.current}°C "
                f"(high={entry.high}°C, critical={entry.critical}°C)"
            )

# Raw JSON output
# print("\nTemperature sensors (raw JSON):")
# print(json.dumps(temps, indent=2, default=str))

# ==== CPU ====
print("\n--- CPU ---")
cpu_percent = psutil.cpu_percent(interval=1)
logical = psutil.cpu_count(logical=True)
physical = psutil.cpu_count(logical=False)

print(f"CPU usage: {cpu_percent}%")
print(f"CPU cores: {physical} physical / {logical} logical")

# Linux/Unix: load average = average runnable processes over time
if hasattr(os, "getloadavg"):
    load1, load5, load15 = os.getloadavg()
    print(f"Load avg (1m, 5m, 15m): {load1:.2f}, {load5:.2f}, {load15:.2f}")


# ==== Memory ====
print("\n--- Memory ---")

vm = psutil.virtual_memory()
sm = psutil.swap_memory()

print(f"RAM: {vm.percent}% used ({vm.used / (1024**3):.2f} GB / {vm.total / (1024**3):.2f} GB)")
print(f"RAM available: {vm.available / (1024**3):.2f} GB")

print(f"Swap: {sm.percent}% used ({sm.used / (1024**3):.2f} GB / {sm.total / (1024**3):.2f} GB)")

# ==== Disk ====
print("\n--- Disk ---")

partitions = psutil.disk_partitions(all=False)
if not partitions:
    print("No disk partitions detected.")
else:
    for p in partitions:
        # Skip pseudo/virtual filesystems (common on Linux)
        if p.fstype in ("tmpfs", "devtmpfs", "squashfs", "overlay"):
            continue

        try:
            usage = psutil.disk_usage(p.mountpoint)
        except PermissionError:
            print(f"{p.mountpoint}: Permission denied")
            continue

        print(
            f"{p.mountpoint} ({p.fstype}): {usage.percent}% used "
            f"({usage.used / (1024**3):.2f} GB / {usage.total / (1024**3):.2f} GB)"
        )



print("\n=====================\n")