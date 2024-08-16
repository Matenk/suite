import unittest
import Runner

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.Garry = Runner.Runner('Garry')
        for run in range(10):
            self.Garry.walk()

        self.assertEqual((self.Garry.distance), 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.Harry = Runner.Runner('Harry')
        for run in range(10):
            self.Harry.run()

        self.assertEqual((self.Harry.distance), 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.Parry = Runner.Runner('Parry')
        for run in range(10):

            self.Parry.run()
        self.Rorry = Runner.Runner('Rorry')
        for run in range(10):
            self.Rorry.walk()

        self.assertNotEqual(self.Rorry.distance, self.Parry.distance)
