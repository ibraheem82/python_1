class RecordName:

    def __init__(self, names):
        self.nanes = names

    def getNames(self):
        for i in self.names:
            if len(i) < 5:
                print("incomplete names")

            # return (len(i))


y = RecordName("olanrewaju")
y.getNames()