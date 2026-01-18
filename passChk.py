"""passChk.py

Linux account check.

What it does:
- Reads local user accounts from /etc/passwd
- Looks up password status from /etc/shadow
- Prints:
  1) usernames shorter than a minimum length
  2) accounts that are locked/disabled or have no password set

Notes:
- This is Linux-only. It won't run on Windows Python.
- Reading /etc/shadow usually requires sudo.
""" 

import pwd

try:
    import spwd  # Linux-only: reads /etc/shadow
except ModuleNotFoundError:
    spwd = None


# -------- Settings  --------

# Username policy: flag usernames shorter than x many characters.
MIN_USERNAME_LEN = 6

# On Ubuntu, "real" user accounts usually start at UID 1000.
# System/service accounts are often UID < 1000.
MIN_UID = 1000

# Set to True to include system/service accounts.
INCLUDE_SYSTEM_ACCOUNTS = False


def is_locked_or_unset(shadow_password_field):
    """Return True if the /etc/shadow password field means locked/disabled/unset."""

    # This field is NOT a plaintext password.
    # Common values:
    # - "$6$...." => a password hash exists
    # - "" (empty) => no password set
    # - starts with "!" or "*" => locked/disabled
    if shadow_password_field is None:
        return True

    shadow_password_field = shadow_password_field.strip()
    if shadow_password_field == "":
        return True

    if shadow_password_field.startswith("!") or shadow_password_field.startswith("*"):
        return True

    return False


def main():
    if spwd is None:
        print("This script only works on Linux (needs the 'spwd' module).")
        return

    # These lists collect usernames to report.
    short_usernames = []
    locked_or_unset_accounts = []
    missing_shadow_entry = []

    # Get all local users from /etc/passwd.
    users = pwd.getpwall()

    for user in users:
        username = user.pw_name
        uid = user.pw_uid

        # Optional: skip system accounts (usually UID < 1000 on Ubuntu).
        if not INCLUDE_SYSTEM_ACCOUNTS and uid < MIN_UID:
            continue

        # Check 1: short usernames
        if len(username) < MIN_USERNAME_LEN:
            short_usernames.append(username)

        # Check 2: password status from /etc/shadow
        try:
            shadow_record = spwd.getspnam(username)
        except PermissionError:
            print("Permission denied reading /etc/shadow.")
            print("Try running:")
            print("  sudo python3 passChk.py")
            return
        except KeyError:
            # User exists in /etc/passwd but not in /etc/shadow
            missing_shadow_entry.append(username)
            continue

        shadow_field = shadow_record.sp_pwdp
        if is_locked_or_unset(shadow_field):
            locked_or_unset_accounts.append(username)

    # -------- Print results --------

    print(f"Includes system accounts: {INCLUDE_SYSTEM_ACCOUNTS}")

    print(f"Users with usernames shorter than {MIN_USERNAME_LEN} characters:")
    if not short_usernames:
        print("  (none)")
    else:
        for name in short_usernames:
            print(f"  {name}")

    print("\nUsers with no password set OR locked/disabled accounts:")
    if not locked_or_unset_accounts:
        print("  (none)")
    else:
        for name in locked_or_unset_accounts:
            print(f"  {name}")

    if missing_shadow_entry:
        print("\nUsers missing from /etc/shadow (unusual):")
        for name in missing_shadow_entry:
            print(f"  {name}")


if __name__ == "__main__":
    main()
