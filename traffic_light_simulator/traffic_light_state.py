import logging


class TrafficLightState:
    TL_STATE_GREEN = 0
    TL_STATE_YELLOW = 1
    TL_STATE_RED = 2

    def __init__(self):
        # TL always starts w/ green state
        self.State = self.TL_STATE_GREEN

    def set_next_state(self) -> int:
        """
        Consumes current state, updates state, & returns new state for traffic light
        Example - input: 0, output: 1; input: 1, output: 2, input 2, output 0
        :return: next state of light based on current state
        """

        if self.State == TrafficLightState.TL_STATE_GREEN:
            self.State = TrafficLightState.TL_STATE_YELLOW
        elif self.State == TrafficLightState.TL_STATE_YELLOW:
            self.State = TrafficLightState.TL_STATE_RED
        elif self.State == TrafficLightState.TL_STATE_RED:
            self.State = TrafficLightState.TL_STATE_GREEN
        else:
            msg = f"[get_next_state] Error: unknown traffic light state: {self.State}"
            logging.error(msg)
            raise msg
        return self.State

    @classmethod
    def color_for_state(cls, state: int) -> str:
        """
        Returns a string color representation for the given state
        :param state: numeric value of state
        :return: str | name of color corresponding with numeric state
        """

        if state == TrafficLightState.TL_STATE_GREEN:
            return "GREEN"
        elif state == TrafficLightState.TL_STATE_YELLOW:
            return "YELLOW"
        elif state == TrafficLightState.TL_STATE_RED:
            return "RED"
        else:
            msg = f"[color_for_state] Error: unknown traffic light state: {state}"
            logging.error("")
            raise msg