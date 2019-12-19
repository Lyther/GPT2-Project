from gui.example import *
from flexx import flx

app = flx.App(Example)
app.export('example.html', link=0)