#!/usr/bin/env python
from xdg.DesktopEntry import DesktopEntry
from xdg.Exceptions import ValidationError
import argparse
import sys

__author__ = 'tsi'

categories = ["AudioVideo", "Audio", "Video", "Development", "Education", "Game", "Graphics", "Network", "Office",
              "Science", "Settings", "System", "Utility",
              'Building', 'Debugger', 'IDE', 'GUIDesigner', 'Profiling', 'RevisionControl', 'Translation', 'Calendar',
              'ContactManagement', 'Database', 'Dictionary', 'Chart', 'Email', 'Finance', 'FlowChart', 'PDA',
              'ProjectManagement', 'Presentation', 'Spreadsheet', 'WordProcessor', '2DGraphics', 'VectorGraphics',
              'RasterGraphics', '3DGraphics', 'Scanning', 'OCR', 'Photography', 'Publishing', 'Viewer', 'TextTools',
              'DesktopSettings', 'HardwareSettings', 'Printing', 'PackageManager', 'Dialup', 'InstantMessaging', 'Chat',
              'IRCClient', 'Feed', 'FileTransfer', 'HamRadio', 'News', 'P2P', 'RemoteAccess', 'Telephony',
              'TelephonyTools', 'VideoConference', 'WebBrowser', 'WebDevelopment', 'Midi', 'Mixer', 'Sequencer',
              'Tuner', 'TV', 'AudioVideoEditing', 'Player', 'Recorder', 'DiscBurning', 'ActionGame', 'AdventureGame',
              'ArcadeGame', 'BoardGame', 'BlocksGame', 'CardGame', 'KidsGame', 'LogicGame', 'RolePlaying', 'Shooter',
              'Simulation', 'SportsGame', 'StrategyGame', 'Art', 'Construction', 'Music', 'Languages',
              'ArtificialIntelligence', 'Astronomy', 'Biology', 'Chemistry', 'ComputerScience', 'DataVisualization',
              'Economy', 'Electricity', 'Geography', 'Geology', 'Geoscience', 'History', 'Humanities',
              'ImageProcessing', 'Literature', 'Maps', 'Math', 'NumericalAnalysis', 'MedicalSoftware', 'Physics',
              'Robotics', 'Spirituality', 'Sports', 'ParallelComputing', 'Amusement', 'Archiving', 'Compression',
              'Electronics', 'Emulator', 'Engineering', 'FileTools', 'FileManager', 'TerminalEmulator', 'Filesystem',
              'Monitor', 'Security', 'Accessibility', 'Calculator', 'Clock', 'TextEditor', 'Documentation', 'Adult',
              'Core', 'KDE', 'GNOME', 'XFCE', 'GTK', 'Qt', 'Motif', 'Java', 'ConsoleOnly']

parser = argparse.ArgumentParser(description="This program will help you to create a .desktop file.")
parser.add_argument("-n", "--name", required=True)
parser.add_argument("-g", "--generic_name", required=True)
parser.add_argument("-e", "--executable", type=file, required=True)
parser.add_argument("-i", "--icon", type=file, required=True)
parser.add_argument("-m", "--comment", required=True)
parser.add_argument("-c", "--categories", required=True)
parser.add_argument("filename")
try:
    args = parser.parse_args()
except IOError as e:
    print e
    sys.exit(e.errno)
file_name = args.filename
if not file_name.endswith(".desktop"):
    file_name += ".desktop"
de = DesktopEntry(file_name)
de.set("Name", args.name)
de.set("GenericName", args.generic_name)
de.set("Exec", args.executable.name)
de.set("Icon", args.icon.name)
de.set("Comment", args.comment)
de.set("Categories", ';'.join(map(str.capitalize, args.categories.split(';'))))
try:
    de.validate()
    de.write()
    sys.exit(0)
except IOError as e:
    print e
    sys.exit(e.errno)
except ValidationError as e:
    print e
    if "is not a registered Category" in e.message:
        print "\nValid categories:"
        print "-----------------"
        print "\n".join(sorted(categories))
        print "\nOr anything that starting with 'X-'"
    sys.exit(45)
except Exception as e:
    print e
    sys.exit(1)
