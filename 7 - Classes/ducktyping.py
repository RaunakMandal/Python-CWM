class TextBox():
    def draw(self):
        print("textbox")


class DropDown():
    def draw(self):
        print("dropdown")


def draw(controls):
    for i in controls:
        i.draw()


ddl = DropDown()
text = TextBox()
draw([ddl, text])
