# USAGE

```
usage: xdg-mk-desktop.py [-h] -n NAME -g GENERIC_NAME -e EXECUTABLE -i ICON -m
                         COMMENT -c CATEGORIES
                         filename

This program will help you to create a .desktop file.

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME
  -g GENERIC_NAME, --generic_name GENERIC_NAME
  -e EXECUTABLE, --executable EXECUTABLE
  -i ICON, --icon ICON
  -m COMMENT, --comment COMMENT
  -c CATEGORIES, --categories CATEGORIES
```

## example:

    xdg-mk-desktop.py -n "My Name" -g "My generic name" -e /usr/bin/x-terminal-emulator -i /usr/share/icons/gnome/scalable/apps/utilities-terminal-symbolic.svg -m "open terminal" -c system my_term.desktop
