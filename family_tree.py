class Person(object):

    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.children = []

    def addChild(self, child):
        self.children.append(child)
    
    def dump(self):
        self.putName()
        for child in self.children:
            print '  %s' % child.getName()

    def putName(self):
        print self.first + ' ' + self.last
    
    def getName(self):
        return self.first + ' ' + self.last

def main():
    bob = Person('robert', 'main')
    claudia = Person('claudia', 'main')
    laura = Person('laura', 'main')
    andrea = Person('andrea', 'elder')
    nicole = Person('nicole', 'elder')
    thomas = Person('thomas', 'elder')
    bob.addChild(thomas)
    bob.addChild(nicole) 
    bob.addChild(andrea)
    bob.addChild(laura) 
    bob.addChild(claudia)
    bob.dump()

if __name__ == '__main__':
   main()
