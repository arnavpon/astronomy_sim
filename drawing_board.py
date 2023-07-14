import tkinter
import logging


class DrawingBoard:

    BACKGROUND_COLOR = "white"
    Window_Width = 1200
    Window_Height = 800
    Timer = 0  # keeps track of lifecycle of board
    Refresh_Sec = 0.01
    SHOULD_ANIMATE = False

    def __init__(self, event_handlers: dict = dict()):
        """
        :param event_handlers: list of events user wants handled as KVP (event, lambda)
        """

        # logging.basicConfig(filename="logs/run.log", filemode="w",
        #                     format="%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s",
        #                     level=logging.INFO)  # write logs to file
        logging.basicConfig(format="%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s", level=logging.INFO)  # write logs to console
        self.Window = self.create_animation_window(event_handlers)
        self.Canvas = self.create_drawing_canvas()
        self.StartButton = None  # init
        self.StopButton = None  # init

    def create_animation_window(self, event_handlers: dict) -> tkinter.Tk:
        """
        Creates Tk window object
        :return: window object
        """

        window = tkinter.Tk()
        for seq, func in event_handlers.items():
            window.bind(seq, func)
        window.bind("<Button-1>", lambda e: print("Mouse click: ", e))  # mouse event
        # window.bind("<Key>", lambda e: print("Keyboard event: ", e))  # keyboard event
        window.title("HTDP Animation Canvas")
        window.geometry(f'{self.Window_Width}x{self.Window_Height}')
        return window

    def create_drawing_canvas(self) -> tkinter.Canvas:
        """
        Creates Tk drawing canvas (origin @ top-left)
        :return: Canvas object
        """

        canvas = tkinter.Canvas(self.Window)
        canvas.configure(bg=self.BACKGROUND_COLOR)
        canvas.pack(fill="both", expand=True)
        return canvas

    def display_window(self, to_animate):
        """
        Runs the root window of the GUI in Tkinter's event loop
        :param to_animate: lambda of the object to animate on canvas
        :return: None
        """

        self.StartButton = self.add_start_button(to_animate)
        self.StopButton = self.add_stop_button()
        self.flash_information_label("Hello!")
        self.Window.mainloop()  # tells tkinter to enter its event loop (blocking!)

    def add_start_button(self, to_animate) -> tkinter.Button:
        """
        Adds button to window that will start the desired animation
        :return: button object
        """

        logging.info("Starting animation...")
        btn = tkinter.Button(self.Window, text='Start Animation', command=lambda: to_animate())
        btn.place(x=100, y=0)
        return btn

    def add_stop_button(self) -> tkinter.Button:
        """
        Adds button to window that will stop the current animation
        :return: button object
        """

        def stop_animation():
            self.SHOULD_ANIMATE = False

        logging.info("stopping animation...")
        btn = tkinter.Button(self.Window, text='Stop', command=stop_animation)
        btn.place(x=250, y=0)
        return btn

    def flash_information_label(self, text: str) -> tkinter.Label:
        """
        Briefly displays the specified text in the window, before fading the text out
        :param text: string to display
        :return: none
        """

        logging.info("flashing info label...")
        lbl = tkinter.Label(self.Window, text=text)
        lbl.place(x=0, y=0)

        def remove_lbl():
            logging.info("calling remove_lbl()")
            lbl.destroy()

        self.Window.after(5000, remove_lbl)
        return lbl