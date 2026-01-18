#!/usr/bin/env python

# monitor_wifi.py
import subprocess
from time import sleep

SLEEP_TIME = 1 * 60

# Choose what to ping by setting TARGET_KEY.
# Examples:
# - LAN check: set TARGET_KEY = "gateway" (your router)
# - Internet check: set TARGET_KEY = "internet" (public IP)
TARGETS = {
    "internet": "8.8.8.8",
    "google": "www.google.com",
    "gateway": "192.168.1.1",
}
TARGET_KEY = "internet"

PING_COUNT = 4
PING_TIMEOUT_SECONDS = 1


def ping_host(host: str, count: int = PING_COUNT, timeout_seconds: int = PING_TIMEOUT_SECONDS):
    """Run an Ubuntu-style ping and return (success, output)."""

    cmd = ["ping", "-c", str(count), "-W", str(timeout_seconds), host]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return False, "ping command not found (is iputils-ping installed?)"
    except Exception as exc:
        return False, f"ping failed: {exc}"

    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode == 0, output.strip()

def is_internet_on():
    """Check connectivity by pinging the configured target."""

    host = TARGETS.get(TARGET_KEY)
    if not host:
        print(f"# unknown TARGET_KEY: {TARGET_KEY!r}. Valid keys: {', '.join(TARGETS.keys())}")
        return False

    ok, output = ping_host(host)

    print(f"# ping target: {TARGET_KEY} -> {host}")
    if output:
        print(output)

    return ok


def main():
    while True:
        if not is_internet_on():
            print('# network is down')
        else:
            print('# network is up')
            pass

        print ('# sleeping for ' +  str(SLEEP_TIME) + ' seconds...')
        sleep(SLEEP_TIME)


#############################################################################

if __name__ == "__main__":
    main()