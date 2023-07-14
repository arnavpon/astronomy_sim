import logging
import time

from drawing_board import DrawingBoard
from traffic_light_simulator.traffic_light_state import TrafficLightState


class TrafficLight:
    """
    Visual representation of a traffic light that is animated in window
    """

    LIGHT_RADIUS = 25
    FRAME_X_TL_CORNER = 300
    FRAME_Y_TL_CORNER = 300
    FRAME_X_BR_CORNER = 600
    FRAME_Y_BR_CORNER = 500

    @property
    def frame_width(self) -> int:
        return abs(TrafficLight.FRAME_X_BR_CORNER - TrafficLight.FRAME_X_TL_CORNER)

    @property
    def frame_height(self) -> int:
        return abs(TrafficLight.FRAME_Y_BR_CORNER - TrafficLight.FRAME_Y_TL_CORNER)

    def __init__(self, board: DrawingBoard):
        """
        Generates UI for a traffic light with a rectangular frame, positioned horizontally, with circular lights centered in each third of the frame
        :param board: window in which to draw
        :param state: state object for TL
        """

        self.Board = board
        self.State = TrafficLightState()
        self.frame = board.Canvas.create_rectangle(TrafficLight.FRAME_X_TL_CORNER, TrafficLight.FRAME_Y_TL_CORNER, TrafficLight.FRAME_X_BR_CORNER, TrafficLight.FRAME_Y_BR_CORNER)  # rect from TL -> BR corners
        self.green_light = self.get_traffic_light_centered_at(self.get_center_of_segment(0))
        self.yellow_light = self.get_traffic_light_centered_at(self.get_center_of_segment(1))
        self.red_light = self.get_traffic_light_centered_at(self.get_center_of_segment(2))
        self.switch_light(self.get_light_for_state(), on=True)  # turn on initial light

    def get_center_of_segment(self, segment: int) -> tuple:
        """
        For the specified segment of the traffic light (0, 1, 2), gives the coordinates of the center
        :param segment: int | segment # of the traffic light, e.g. 0 -> green, 1 -> yellow
        :return: x, y coordinate pair
        """

        center_y = TrafficLight.FRAME_Y_TL_CORNER + self.frame_height / 2  # centered y point is always the same
        if segment in [0, 1, 2]:
            # Center x is calculated by dividing the frame into 3 identical horizontal segments & getting the midpoint
            center_x = TrafficLight.FRAME_X_TL_CORNER + segment * (self.frame_width / 3) + self.frame_width / 6
        else:
            msg = f"[get_center_of_segment] Unknown segment value: {segment}"
            logging.error(msg)
            raise msg
        return center_x, center_y


    def get_traffic_light_centered_at(self, center: tuple):
        """
        Creates a Canvas Oval object centered at the coordinates x, y
        :param center | tuple of (x_coordinate, y_coordinate)
        :return: Tkinter object Id of created Oval
        """

        x, y = center
        return self.Board.Canvas.create_oval(x - TrafficLight.LIGHT_RADIUS,
                                             y - TrafficLight.LIGHT_RADIUS,
                                             x + TrafficLight.LIGHT_RADIUS,
                                             y + TrafficLight.LIGHT_RADIUS,
                                             outline="Black", width=2)

    def animate_traffic_light(self):
        """
        Animates function of a traffic light, proceeding through states over time, and coloring/uncoloring the appropriate balls
        :return: None
        """

        logging.info("Running traffic light simulator...")
        self.Board.flash_information_label("Starting simulator...")
        self.Board.SHOULD_ANIMATE = True  # reset indicator
        while self.Board.SHOULD_ANIMATE:
            time.sleep(3)
            print(self.State.State)
            old_state = self.get_light_for_state()
            self.switch_light(old_state, on=False)  # turn previous light off
            self.State.set_next_state()  # update state
            print(self.State.State)
            new_state = self.get_light_for_state()
            self.switch_light(new_state, on=True)  # turn previous light off
            self.Board.Window.update()

    def get_light_for_state(self):
        """
        Gets the associated light object for the current state
        :return: Canvas object Id
        """

        if self.State.State == TrafficLightState.TL_STATE_GREEN:
            return self.green_light
        if self.State.State == TrafficLightState.TL_STATE_YELLOW:
            return self.yellow_light
        if self.State.State == TrafficLightState.TL_STATE_RED:
            return self.red_light
        else:
            raise f"Error: unknown state {self.State.State}"

    def switch_light(self, light_object, on: bool):
        """
        Switches the input light object on or off
        :param light_object: light object
        :param on: True if switching ON, False if switching OFF
        :return: None
        """

        if not on:  # remove fill
            self.Board.Canvas.itemconfig(light_object, fill=self.Board.BACKGROUND_COLOR)
        elif light_object == self.green_light:
            self.Board.Canvas.itemconfig(light_object, fill="green")
        elif light_object == self.yellow_light:
            self.Board.Canvas.itemconfig(light_object, fill="yellow")
        elif light_object == self.red_light:
            self.Board.Canvas.itemconfig(light_object, fill="red")
        else:
            raise f"Error: unknown light object"