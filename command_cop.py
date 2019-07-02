# -*- encoding: utf-8 -*-

import re
import weechat

SCRIPT_NAME    = "command-cop"
SCRIPT_AUTHOR  = "Joël Perras <joel@nerderati.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Prevent entering of leading spaces before /command."


def command_run_input(data, buffer, command):
    """ Function called when a command "/input xxxx" is run."""

    if command == "/input return": # As in enter was pressed.

        # Get input contents.
        input_s = weechat.buffer_get_string(buffer, 'input')

        # Match leading spaces before commands (slashes) and spaces just after a
        # command slash.
        matches = re.match(r'(?:\s+/|/\s+)(.*)', input_s)
        if matches is not None:
            # Alert in weechat buffer.
            weechat.prnt("", "%sLeading spaces detected in command!" % weechat.color('red'))
            return weechat.WEECHAT_RC_OK_EAT

    return weechat.WEECHAT_RC_OK


if __name__ == '__main__':

    if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', ''):
        weechat.hook_command_run('/input return', 'command_run_input', '')
