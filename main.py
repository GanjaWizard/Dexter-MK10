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
            0.0009,
            'a',
            platform.system()
        ]
        print('DEXTER VIRTUAL INTELLIGENCE MARK 10:', self.build)

    def run(self):
        # OPERATING SYSTEM CHECKER
        if self.build[3] == 'Windows':
            pass
        elif self.build[3] == 'Linux':
            pass
        else:
            print(self.build[3], 'NOT SUPPORTED')
        # ----

    @staticmethod
    def upd_lin_dep():
        subprocess.run(['sudo', 'apt-get', 'install',
                        'bluez', 'pulseaudio-module-bluetooth',
                        'python-gobject', 'python-gobject-2',
                        'bluez-tools'])

    @staticmethod
    def upd_core():
        urlreq.urlretrieve("https://raw.github.com/Oweneaster/Dexter-MK10/master/main.py", "main.py")

    @staticmethod
    def sys_reboot():
        if Core.build[3] == 'Windows':
            subprocess.run(['python', 'main.py'])
        else:
            subprocess.run(['python3', 'main.py'])


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
        print(' SYSTEM IS OUT-OF-DATE',
              '\n  Updating main.py')
        Core.upd_core()
        print('  Updating Core Dependencies')
        Core.upd_lin_dep()
        print('  System Rebooting...\n')
        Core.sys_reboot()

    elif vers == Core.build[1]:
        print(' SYSTEM IS UP-TO-DATE\n')
        Core.run()
    else:
        print(' REPOSITORY NOT SUPPORTED\n')
        Core.run()
