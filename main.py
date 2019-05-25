# VIRTUAL INTELLIGENCE: DEXTER
# MARK 10 / MKX
# AUTHOR : EASTER LTD

import platform
import subprocess
import urllib.request as urlreq
from time import time


class MarkXCore:

    def __init__(self):
        self.build = [
            time(),
            0.0008,
            'a',
            platform.system()
        ]
        print('DEXTER VIRTUAL INTELLIGENCE MARK 10:', self.build)

    def run(self):
        # OPERATING SYSTEM CHECKER
        if self.build[3] == 'Windows':
            pass
        elif self.build[3] == 'Linux':
            subprocess.run(['sudo', 'apt-get', 'install',
                            'bluez', 'pulseaudio-module-bluetooth',
                            'python-gobject', 'python-gobject-2',
                            'bluez-tools'])
        else:
            print(self.build[3], 'NOT SUPPORTED')
        # ----

if __name__ == '__main__':
    # SOFT INITIALIZATION
    Core = MarkXCore()
    urlreq.urlcleanup()
    print('>> SYSTEM UPDATE')
    # CHECK UPDATE REPOSITORY
    http = urlreq.urlopen("https://github.com/Oweneaster/Dexter-MK10")
    html = http.read()

    def disc(html, label):
        data = str(html).split(label)[1]
        result = data.split('</p>\\n<blockquote>\\n<p>')[1].split('</p>')[0]
        return result

    vers = float(disc(html=html, label='/VERSION'))
    print(' LATEST VERSION:', vers)

    # SYSTEM VERSION CHECKING
    if vers > Core.build[1]:
        print(' SYSTEM IS OUT-OF-DATE\n  Updating...')
        data = urlreq.urlretrieve("https://raw.github.com/Oweneaster/Dexter-MK10/master/main.py", "main.py")
        print('  Success!\n')
        if Core.build[3] == 'Windows':
            subprocess.run(['python', 'main.py'])
        else:
            subprocess.run(['python3', 'main.py'])

    elif vers == Core.build[1]:
        print(' SYSTEM IS UP-TO-DATE\n')
        Core.run()
    else:
        print(' REPOSITORY NOT SUPPORTED\n')
        Core.run()
