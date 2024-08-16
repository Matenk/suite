import unittest
import Unit
import RunnerTest

tournament_runner_test = unittest.TestSuite()
tournament_runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit.TournamentTest))
tournament_runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournament_runner_test)
# не уверен можно ли применить verbosity в данном случае изолированно именно к Runner тестам, учитывая что тест
# сьют общий
# можно, конечно создать 2 тест сьюта и 2 runner в один из которых передать verbosity=2 (пример кода ниже):

"""ПРИМЕР: 
# tournament_test = unittest.TestSuite()
# tournament_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit.TournamentTest))
# 
# runner_test = unittest.TestSuite()
# runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
# 
# runner1 = unittest.TextTestRunner(verbosity=2).run(runner_test)
# runner2 = unittest.TextTestRunner().run(tournament_test)"""


