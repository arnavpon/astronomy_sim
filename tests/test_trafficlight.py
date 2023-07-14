import unittest
from traffic_light_simulator.traffic_light import TrafficLight
from traffic_light_simulator.traffic_light_state import TrafficLightState


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.State = TrafficLightState()

    def test_state_green(self):
        self.assertEqual(self.State.set_next_state(), TrafficLightState.TL_STATE_YELLOW)  # add assertion here


if __name__ == '__main__':
    unittest.main()