## Summary

This is a somewhat silly script for [WeeChat](https://weechat.org/), a
command-line multipurpose chat client, whose sole purpose is to prevent you from
entering in a typical IRC command that has leading slashes and is thus sent to
the channel buffer instead of being interpreted as a command by the IRC client
and/or server.

For example, if you want to change nicks on IRC, you can do it by sending the
following command:

![tolstoy nick change](https://snaps.nerderati.com/VE0iRla28G0aIm2s.png)

However, if you mistakenly have some leading spaces before or after the slash,
like:

![tolstoy nick change with leading spaces](https://snaps.nerderati.com/g16whVZYRPkZD7rO.png)

the command will not be interpreted as such, and will instead simply be sent to
the channel. This has happened to be enough due to my rampant usage of the
[`go.py`](https://weechat.org/scripts/source/go.py.html/) script that I got fed
up and wrote this separate script to prevent me from making dumb mistakes.

## Usage

Once the script is installed, usage is straightforward and unconfigurable. The
script hooks into the input event that is triggered when you hit 'enter' and
want to send the text to the buffer. In the event that it detects leading spaces
before or after the slash character, the input will *not* be sent to the buffer,
and you will receive an alert string in the core weechat buffer indicating this
fact:

![weechat core alert](https://snaps.nerderati.com/4NQO6fBJUHdyqyrw.png)


### Details

It turns out that writing scripts for WeeChat is pretty difficult, due to the
somewhat scattered documentation across the scripts API and the C-based plugin
API. I would have preferred a slightly different approach here – highlighting
the leading spaces as if they were a spelling mistake instead of sending an
error to the core weechat bufffer – but this is good enough for me at the
moment.


## Installation

You can install this script directly, which may be more up-to-date than what is
available elsewhere:

```
cd ~/.weechat/python/
wget 'https://raw.githubusercontent.com/jperras/command_cop/master/command_cop.py'
cd autoload/
ln -s ../command_cop.py .

```

If you prefer to clone the repository instead of `wget`'ing the script, you can
do the following:

```
git clone 'https://github.com/GermainZ/weechat-vimode.git'
git clone 'https://github.com/jperras/command_cop.git'
ln -s /path/to/git/repo/command_cop.py ~/.weechat/python/autoload/command_cop.py

```
