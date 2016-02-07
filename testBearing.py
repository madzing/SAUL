import unittest
from Bearing import Bearing

class TestBearing(unittest.TestCase):
    def test_createBearings(self):
        self.assertEqual(Bearing(-5).bearing,Bearing(355).bearing)
        self.assertEqual(Bearing(0).bearing,Bearing(360).bearing)
        self.assertEqual(Bearing(-180).bearing,Bearing(180).bearing)
        
    def test_getDiffTo(self):
        x = Bearing(350)
        y = Bearing(15)
        z = Bearing(270)
        self.assertEqual(x.getDiffTo(y),25)
        self.assertEqual(y.getDiffTo(x),-25)
        
        self.assertEqual(x.getDiffTo(z),-80)
        self.assertEqual(z.getDiffTo(x),80)

        self.assertEqual(y.getDiffTo(z),-105)
        self.assertEqual(z.getDiffTo(y),105)

    def test_getDiffTo360degree(self):
        x = Bearing(350)
        y = Bearing(15)
        z = Bearing(270)
        self.assertEqual(x.getDiffTo360degree(x),10)
        self.assertEqual(x.getDiffTo360degree(y),15)
        self.assertEqual(x.getDiffTo360degree(z),90)

    def test_add(self):
        x = Bearing(30)
        y = Bearing(15)
        z = Bearing(350)
        
        self.assertEqual(x.add(y).bearing,45)
        self.assertEqual(x.add(15).bearing,45)

        self.assertEqual(x.add(325).bearing,355)
        self.assertEqual(x.add(-35).bearing,355)

        self.assertEqual(z.add(50).bearing,40)

    def test_substract(self):
        x = Bearing(30)
        y = Bearing(15)
        z = Bearing(350)

        self.assertEqual(x.substract(y).bearing,15)
        self.assertEqual(x.substract(15).bearing,15)

        self.assertEqual(y.substract(30).bearing,345)
        self.assertEqual(y.substract(-330).bearing,345)

        self.assertEqual(y.substract(x).bearing,345)

    def test_calculateMeanBearing(self):
        bearingList1 = [Bearing(10),Bearing(350),Bearing(5),Bearing(355)]
        bearingTupel1 =(Bearing(10),Bearing(350),Bearing(5),Bearing(355))
        self.assertEqual(Bearing.calculateMeanBearing(bearingList1).bearing,Bearing(0).bearing)
        self.assertEqual(Bearing.calculateMeanBearing(bearingTupel1).bearing,Bearing(0).bearing)

if __name__ == '__main__':
    unittest.main()
