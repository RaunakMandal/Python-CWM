from abc import ABC, abstractmethod
# abstract base class


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox")


class DropDown(UIControl):
    def draw(self):
        print("dropdown")


def draw(controls):
    for i in controls:
        i.draw()


ddl = DropDown()
text = TextBox()
draw([ddl, text])
