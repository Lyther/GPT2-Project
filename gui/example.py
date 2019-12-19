from flexx import flx


class Example(flx.Widget):
    def init(self):
        with flx.HBox():
            flx.Button(text='hello', flex=1)
            flx.Button(text='world', flex=2)
