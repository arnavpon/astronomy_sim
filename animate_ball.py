from drawing_board import DrawingBoard


class BallAnimation:
    Ball_Start_XPosition = 50
    Ball_Start_YPosition = 50
    Ball_Radius = 30
    Ball_min_movement = 5

    def __init__(self, board: DrawingBoard):
        self.Board = board

    def animate_ball(self, xinc: int = 5, yinc: int = 5):
        """
        Animates a ball object in the specified Tkinter window
        :param board: DrawingBoard | window in which to animate object
        :param xinc: int | amount ball should move in x direction
        :param yinc: int | amount ball should move in y direction
        :return: none
        """

        self.Board.SHOULD_ANIMATE = True  # set indicator at start
        ball = self.Board.Canvas.create_oval(BallAnimation.Ball_Start_XPosition - BallAnimation.Ball_Radius,
                                        BallAnimation.Ball_Start_YPosition - BallAnimation.Ball_Radius,
                                        BallAnimation.Ball_Start_XPosition + BallAnimation.Ball_Radius,
                                        BallAnimation.Ball_Start_XPosition + BallAnimation.Ball_Radius,
                                        fill="Red", outline="Black", width=4)
        while self.Board.SHOULD_ANIMATE:
            self.Board.Canvas.move(ball, xinc, yinc)
            self.Board.Window.update()
            ball_pos = self.Board.Canvas.coords(ball)
            al, bl, ar, br = ball_pos
            if al < abs(xinc) or ar > self.Board.Window_Width-abs(xinc):
                xinc = -xinc
            if bl < abs(yinc) or br > self.Board.Window_Height-abs(yinc):
                yinc = -yinc