# VIRTUAL INTELLIGENCE: DEXTER
# MARK 10 / MKX
# AUTHOR : EASTER LTD

import urllib.request as urlreq
from time import time, sleep


class MarkXCore:

    def __init__(self):
        self.build = [
            time(),
            0.0002,
            'a',
        ]
        print('DEXTER VIRTUAL INTELLIGENCE MARK 10:', self.build)

    def run(self):
        print('\n\nHello World.')


if __name__ == '__main__':
    # SOFT INITIALIZATION
    Core = MarkXCore()
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
        print(' SYSTEM IS OUT-OF-DATE')
        import requests
        requests.get()
        print(html)
    elif vers == Core.build[1]:
        print(' SYSTEM IS UP-TO-DATE')
        Core.run()
    else:
        print(' REPOSITORY NOT SUPPORTED')
        exit()