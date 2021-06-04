class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Logging...")
        super().append(object)


text = Text("Fuck")
print(text.duplicate())
text2 = TrackableList()
print(text2.append("Fuck"))
