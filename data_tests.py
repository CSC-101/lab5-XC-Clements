import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    def test_Time_eq_1(self):
        other = data.Time(16, 90, 38)
        self.assertEqual((data.Time(16,90,38) == other), True)

    def test_Time_eq_2(self):
        other = "haha I will foil your program!!!"
        self.assertEqual((data.Time(2,19,20) == other), False)

    #### Add tests for Time.__repr__
    def test_Time_repr_1(self):
        tester = data.Time(4,2,1)
        self.assertEqual(repr(tester), 'Hour(s) = 4, Minute(s) = 2, Second(s) = 1')

    def test_Time_repr_2(self):
        tester = data.Time(3,2,1)
        self.assertNotEqual(repr(tester), 12)

    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertEqual(7, point.x)
        self.assertEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertEqual(4, point.x)
        self.assertEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
