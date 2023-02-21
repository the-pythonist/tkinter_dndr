
__author__ = {"twitter": "the_pythonist"}


class DragDropResizeWidget:
    def __init__(self, widget):
        self.widget = widget
        self.widget_cursor = self.widget["cursor"]

    def __cursorChange(self, event):
        self.widget["cursor"] = self.widget_cursor

    def __startDrag(self, event):
        self.widget.start_drag_x = event.x
        self.widget.start_drag_y = event.y

    def __motionDrag(self, event):
        self.widget["cursor"] = "bogosity"
        self.widget.place_configure(anchor="nw")
        new_x = (self.widget.winfo_x() + event.x) - self.widget.start_drag_x
        new_y = (self.widget.winfo_y() + event.y) - self.widget.start_drag_y
        self.widget.place(x=new_x, y=new_y)

    def make_draggable(self):
        """Makes the widget ONLY have drag and drop support"""
        self.widget.bind("<Button-1>", self.__startDrag)
        self.widget.bind("<Button1-Motion>", self.__motionDrag)
        self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

    def __make_resizable(self, event):
        self.xx = self.widget.winfo_x() + int(self.widget.place_info()["width"])
        self.yy = self.widget.winfo_y() + int(self.widget.place_info()["height"])
        self.ttx = event.x + self.widget.winfo_x()
        self.tty = event.y + self.widget.winfo_y()

        if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self.widget["cursor"] = "bottom_right_corner"
            self.widget.bind("<Button1-Motion>", self.__motionBottomRight)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif ((self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (
                self.widget.winfo_x() == self.ttx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self.widget["cursor"] = "bottom_left_corner"
            self.widget.bind("<Button1-Motion>", self.__motionBottomLeft)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif ((self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (
                self.widget.winfo_y() == self.tty - 3)) & (
                (self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (
                self.widget.winfo_x() == self.ttx - 3)):
            self.widget["cursor"] = "top_left_corner"
            self.widget.bind("<Button1-Motion>", self.__motionTopLeft)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif ((self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (
                self.widget.winfo_y() == self.tty - 3)) & (
                (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
            self.widget["cursor"] = "top_right_corner"
            self.widget.bind("<Button1-Motion>", self.__motionTopRight)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
            self.widget["cursor"] = "right_side"
            self.widget.bind("<Button1-Motion>", self.__motionRight)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
            self.widget["cursor"] = "bottom_side"
            self.widget.bind("<Button1-Motion>", self.__motionBottom)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif (self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (
                self.widget.winfo_x() == self.ttx - 3):
            self.widget["cursor"] = "left_side"
            self.widget.bind("<Button1-Motion>", self.__motionLeft)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        elif (self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (
                self.widget.winfo_y() == self.tty - 3):
            self.widget["cursor"] = "top_side"
            self.widget.bind("<Button1-Motion>", self.__motionTop)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

        else:
            self.widget.bind("<Button1-Motion>", self.__nullify_bind)
            self.widget["cursor"] = self.widget_cursor

    def make_resizable(self):
        """Makes the widget only resizable from all corners and edges of the widget"""
        self.widget.bind("<Motion>", self.__make_resizable)

    def __make_draggable_and_resizable(self, event):
        self.xx = self.widget.winfo_x() + int(self.widget.place_info()["width"])
        self.yy = self.widget.winfo_y() + int(self.widget.place_info()["height"])
        self.ttx = event.x + self.widget.winfo_x()
        self.tty = event.y + self.widget.winfo_y()

        if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self.widget["cursor"] = "bottom_right_corner"
            self.widget.bind("<Button1-Motion>", self.__motionBottomRight)

        elif ((self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (
                self.widget.winfo_x() == self.ttx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self.widget["cursor"] = "bottom_left_corner"
            self.widget.bind("<Button1-Motion>", self.__motionBottomLeft)

        elif ((self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (
                self.widget.winfo_y() == self.tty - 3)) & (
                (self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (
                self.widget.winfo_x() == self.ttx - 3)):
            self.widget["cursor"] = "top_left_corner"
            self.widget.bind("<Button1-Motion>", self.__motionTopLeft)

        elif ((self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (
                self.widget.winfo_y() == self.tty - 3)) & (
                (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
            self.widget["cursor"] = "top_right_corner"
            self.widget.bind("<Button1-Motion>", self.__motionTopRight)

        elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
            self.widget["cursor"] = "right_side"
            self.widget.bind("<Button1-Motion>", self.__motionRight)

        elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
            self.widget["cursor"] = "bottom_side"
            self.widget.bind("<Button1-Motion>", self.__motionBottom)

        elif (self.widget.winfo_x() == self.ttx - 1) | (self.widget.winfo_x() == self.ttx - 2) | (self.widget.winfo_x() == self.ttx - 3):
            self.widget["cursor"] = "left_side"
            self.widget.bind("<Button1-Motion>", self.__motionLeft)

        elif (self.widget.winfo_y() == self.tty - 1) | (self.widget.winfo_y() == self.tty - 2) | (self.widget.winfo_y() == self.tty - 3):
            self.widget["cursor"] = "top_side"
            self.widget.bind("<Button1-Motion>", self.__motionTop)


        else:
            self.widget["cursor"] = self.widget_cursor
            self.widget.bind("<Button-1>", self.__startDrag)
            self.widget.bind("<Button1-Motion>", self.__motionDrag)
            self.widget.bind("<ButtonRelease-1>", self.__cursorChange)

    def make_draggable_and_resizable(self):
        """Makes the widget both draggable and resizable from all corners and edges of the widget"""
        self.widget.bind("<Motion>", self.__make_draggable_and_resizable)

    def __motionTop(self, event):
        self.widget.place_configure(x=self.widget.winfo_x(), y=(self.widget.winfo_y() + int(self.widget.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.widget.place_info()["height"])
        self.widget.place_configure(height=new_height)

    def __motionBottom(self, event):
        self.widget.place_configure(x=self.widget.winfo_x(), y=self.widget.winfo_y(), anchor="nw")
        new_height = int(self.widget.place_info()["height"]) + (event.y - int(self.widget.place_info()["height"]))
        self.widget.place_configure(height=new_height)

    def __motionLeft(self, event):
        self.widget.place_configure(x=(self.widget.winfo_x() + int(self.widget.place_info()["width"])), y=self.widget.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.widget.place_info()["width"])
        self.widget.place_configure(width=new_width)

    def __motionRight(self, event):
        self.widget.place_configure(x=self.widget.winfo_x(), y=self.widget.winfo_y(), anchor="nw")
        new_width = int(self.widget.place_info()["width"]) + (event.x - int(self.widget.place_info()["width"]))
        self.widget.place_configure(width=new_width)

    def __motionTopLeft(self, event):
        self.widget.place_configure(x=self.widget.winfo_x() + int(self.widget.place_info()["width"]),
                             y=self.widget.winfo_y() + int(self.widget.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.widget.place_info()["width"])
        new_height = 0 - event.y + int(self.widget.place_info()["height"])
        self.widget.place_configure(width=new_width, height=new_height)

    def __motionTopRight(self, event):
        self.widget.place_configure(x=self.widget.winfo_x(), y=self.widget.winfo_y() + int(self.widget.place_info()["height"]), anchor="sw")
        new_width = int(self.widget.place_info()["width"]) + (event.x - int(self.widget.place_info()["width"]))
        new_height = (0 - event.y) + int(self.widget.place_info()["height"])
        self.widget.place_configure(width=new_width, height=new_height)

    def __motionBottomLeft(self, event):
        self.widget.place_configure(x=(self.widget.winfo_x() + int(self.widget.place_info()["width"])), y=self.widget.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.widget.place_info()["width"])
        new_height = int(self.widget.place_info()["height"]) + (event.y - int(self.widget.place_info()["height"]))
        self.widget.place_configure(width=new_width, height=new_height)

    def __motionBottomRight(self, event):
        self.widget.place_configure(x=self.widget.winfo_x(), y=self.widget.winfo_y(), anchor="nw")
        new_width = int(self.widget.place_info()["width"]) + (event.x - int(self.widget.place_info()["width"]))
        new_height = int(self.widget.place_info()["height"]) + (event.y - int(self.widget.place_info()["height"]))
        self.widget.place_configure(width=new_width, height=new_height)

    def __nullify_bind(self, event):
        pass


__author__ = {"LinkedIn": "Samuel Amogbonjaye", "twitter": "the_pythonist"}


