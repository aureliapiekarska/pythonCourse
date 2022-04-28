class Pen():
    def pen(self):
        print('Write the word')

class Pinapple():
    def pinapple(self):
        print('Pinapple')


class Penpinapple(Pen, Pinapple):
    def pinapplepen(self):
        print('Pinapple consist of the word apple')

Penpinapple().pen()
Penpinapple().pinapple()
Penpinapple().pinapplepen()