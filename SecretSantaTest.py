import unittest

class TestData(unittest.TestCase):
    def setUp(self):
        self.names = ['Daniel', 'Maria', 'Martin', 'Kristina', 'Isabella', 'Ingemar']

    def get_names(self, folder):
        names_from = []
        names_to = []
        for name in self.names:
            file_content = open(folder + '/' + name + ".txt", encoding='iso-8859-1', mode='r').read()
            names_from.append(file_content.split('Hej ')[1].split('!\n')[0])
            names_to.append(file_content.split('Du ska ge julklapp till ')[1].split('!')[0])
        return names_from, names_to

    def verify_names(self, names_from, names_to):
        self.assertEqual(len(names_from), len(self.names))
        self.assertEqual(len(names_to), len(self.names))
        self.assertTrue(all([name in names_from for name in self.names]))
        self.assertTrue(all([name in names_to for name in self.names]))

    def test_real(self):
        names_from, names_to = self.get_names('RealData')
        self.verify_names(names_from, names_to)

    def test_pos(self):
        names_from, names_to = self.get_names('TestData')
        self.verify_names(names_from, names_to)

    @unittest.expectedFailure
    def test_duplicate_from(self):
        names_from, names_to = self.get_names('TestDataDuplicateFrom')
        self.verify_names(names_from, names_to)

    @unittest.expectedFailure
    def test_duplicate_to(self):
        names_from, names_to = self.get_names('TestDataDuplicateTo')
        self.verify_names(names_from, names_to)

    @unittest.expectedFailure
    def test_cannot_give_to_self(self):
        names_from, names_to = self.get_names('TestDataGiveToSelf')
        self.verify_names(names_from, names_to)

if __name__ == '__main__':
    runner = unittest.main()