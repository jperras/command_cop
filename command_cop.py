# -*- encoding: utf-8 -*-

###
# Copyright 2019 Joël Perras <joel@nerderati.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###

###
# Prevent commands from being mistakenly printed to buffers instead of being
# executed due to leading spaces or tabs.
#
#   Upon hitting enter with an input that has leading spaces before a slash e.g.
#   `  /nick vulpine`, the input will be halted and a message will be printed in
#   the core weechat buffer.
#
#   There are currently no commands or settings. Simply install and activate this
#   script and you're good to go.
###

import re
import weechat

SCRIPT_NAME    = "command_cop"
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
