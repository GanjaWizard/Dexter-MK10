# VIRTUAL INTELLIGENCE: DEXTER
# MARK 10 / MKX
# AUTHOR : EASTER LTD

import urllib.request as urlreq
from time import time
from datetime import date


class MarkXCore:

    def __init__(self):
        self.build = [
            time(),
            0.0007,
            'a',
        ]
        print('DEXTER VIRTUAL INTELLIGENCE MARK 10:', self.build)

    def run(self):
        print('\n\nHello World.')
        print('\nThe time is currently ', time())


if __name__ == '__main__':
    # SOFT INITIALIZATION
    Core = MarkXCore()
    urlreq.urlcleanup()
    print('>> SYSTEM UPDATE')
    # CHECK UPDATE REPOSITORY
    http = urlreq.urlopen("https://github.com/Oweneaster/mkx")
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
        data = urlreq.urlretrieve("https://raw.github.com/Oweneaster/mkx/master/main.py", "main.py")
        print('  Success!')
    elif vers == Core.build[1]:
        print(' SYSTEM IS UP-TO-DATE')
        Core.run()
    else:
        print(' REPOSITORY NOT SUPPORTED')
        exit()
