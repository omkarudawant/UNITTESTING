import unittest
import sample


class TestSample(unittest.TestCase):
    def test_add_num(self):
        assert sample.add_num(10, 5) == 15

    def test_add_iter(self):
        assert sample.add_iter([10, 5]) == 15

    def test_avg_num(self):
        assert sample.avg_num([3, 3, 3]) == 3
        assert sample.avg_num([5, 10, 15]) == 10.0


if __name__ == "__main__":
    unittest.main()
