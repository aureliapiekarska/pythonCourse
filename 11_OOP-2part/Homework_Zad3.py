class pen():
    def pen(self):
        print('Write the word')

class pinapple():
    def pinapple(self):
        print('Pinapple')


class penpinapple(pen, pinapple):
    def pinapplepen(self):
        print('Pinapple consist of the word apple')


penpinapple_1 = penpinapple().pen()
penpinapple_2 = penpinapple().pinapple()
penpinapple_3 = penpinapple().pinapplepen()