from drawing_board import DrawingBoard
from animate_ball import BallAnimation
from traffic_light_simulator.traffic_light import TrafficLight
import polygon

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = DrawingBoard()  # instantiate board
#    tl = TrafficLight(board)  # instantiate animation object w/ ref to Board
#    board.display_window(tl.animate_traffic_light)  # start animation for object

    # bouncy_ball = BallAnimation(board)
    # board.display_window(bouncy_ball.animate_ball)

    p = polygon.RandomPolygon(board, n_sides=6)
    board.display_window(p.draw)  # animate random polygon drawing