PROTECTED_PROCESSES = [
    'system',
    'svchost',
    'winlogon',
    'csrss',
    'services',
    'lsass',
    'wininit',
    'smss'
]

ALLOWED_COMMANDS = [
    'cpu',
    'ram',
    'battery',
    'disk',
    'processes',
    'weather',
    'hello',
    'voice'
]

DANGEROUS_COMMANDS = ['kill', 'open']


def validate_command(user_input):
    """
    Check if a command is safe to execute.
    Returns (is_safe, message)
    """
    # Extract base command (first word)
    parts = user_input.split()
    if not parts:
        return False, "Empty command"

    base = parts[0].lower()  # This gets "kill" from "kill notepad"

    # Check if command is allowed OR is a dangerous command
    if base not in ALLOWED_COMMANDS and base not in DANGEROUS_COMMANDS:
        return False, f"Command '{base}' not recognized"

    return True, "Command allowed"


def validate_kill_target(process_name):
    """
    Check if process is safe to kill
    Returns (is_safe, message)
    """
    # Check for empty or wildcard first
    if not process_name or process_name in ['*', '.', 'all']:
        return False, "Invalid process name"

    # Then check against protected processes
    for protected in PROTECTED_PROCESSES:
        if protected in process_name.lower():
            return False, f"Cannot kill protected system process: {protected}"

    # If we get here, it's safe
    return True, "Target appears safe"

def confirm_dangerous_action(command, target=None):
    """
    Ask for confirmation before execution
    """
    if target:
        print(f"\n WARNING: You are about to {command} '{target}'")
    else:
        print(f"\n WARNING: You are about to run '{command}'")

    response = input("Type 'yes' to confirm:").lower()
    return response == 'yes'


