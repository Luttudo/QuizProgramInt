import unittest

class TestFlightReservationSystem(unittest.TestCase):
    def setUp(self):
        self.system = FlightReservationSystem()
        self.system.add_flight("AA123", 100)

    def test_reserve_valid_flight(self):
        self.system.reserve_flight("AA123", 3)
        self.assertEqual(self.system.flights["AA123"], 97)

    def test_reserve_invalid_flight(self):
        self.system.reserve_flight("BB456", 2)
        self.assertEqual(self.system.flights.get("BB456"), None)

    def test_reserve_insufficient_seats(self):
        self.system.reserve_flight("AA123", 110)
        self.assertEqual(self.system.flights["AA123"], 100)

    def test_cancel_reservation(self):
        self.system.reserve_flight("AA123", 5)
        self.system.cancel_reservation("AA123", 2)
        self.assertEqual(self.system.flights["AA123"], 97)

    def test_cancel_invalid_flight(self):
        self.system.cancel_reservation("BB456", 1)
        self.assertEqual(self.system.flights.get("BB456"), None)

if __name__ == "__main__":
    unittest.main()
