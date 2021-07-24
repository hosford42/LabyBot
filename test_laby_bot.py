import unittest

import laby_bot
from laby_bot import robot


class TestDesignedLevels(unittest.TestCase):

    def test_level_0(self):
        robot.load_level('levels/0.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_1a(self):
        robot.load_level('levels/1a.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_1b(self):
        robot.load_level('levels/1b.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_1c(self):
        robot.load_level('levels/1c.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_2a(self):
        robot.load_level('levels/2a.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_2b(self):
        robot.load_level('levels/2b.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_2c(self):
        robot.load_level('levels/2c.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_3a(self):
        robot.load_level('levels/3a.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_3b(self):
        robot.load_level('levels/3b.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_4a(self):
        robot.load_level('levels/4a.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_4b(self):
        robot.load_level('levels/4b.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_counting_the_rocks(self):
        robot.load_level('levels/counting-the-rocks.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped

    def test_level_this_is_crazy(self):
        robot.load_level('levels/this-is-crazy.laby')
        laby_bot.main()
        assert robot.MANAGER.controller.escaped


class TestGeneratedLevels(unittest.TestCase):

    def test_small_level(self):
        for _ in range(40):
            robot.generate_level(5, 5)
            laby_bot.main()
            assert robot.MANAGER.controller.escaped

    def test_regular_level(self):
        for _ in range(20):
            robot.generate_level(10, 10)
            laby_bot.main()
            assert robot.MANAGER.controller.escaped

    def test_big_level(self):
        for _ in range(10):
            robot.generate_level(20, 20)
            laby_bot.main()
            assert robot.MANAGER.controller.escaped

    def test_huge_level(self):
        for _ in range(5):
            robot.generate_level(40, 40)
            laby_bot.main()
            assert robot.MANAGER.controller.escaped

    def test_ridiculous_level(self):
        robot.generate_level(200, 200)
        robot.hide()
        robot.MANAGER.controller.show()
        laby_bot.main()
        robot.MANAGER.controller.show()
        assert robot.MANAGER.controller.escaped


if __name__ == '__main__':
    unittest.main()
