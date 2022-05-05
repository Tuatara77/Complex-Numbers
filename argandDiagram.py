from complex import Complex
import tkinter
try: import numpy
except ModuleNotFoundError:
    import os
    os.system("pip install numpy")
    import numpy
try: import matplotlib.pyplot as pyplot
except ModuleNotFoundError:
    import os
    os.system("pip install matplotlib")
    import matplotlib.pyplot as pyplot


class TkinterWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry(f"{300}x{400}+{100}+{100}")




class ArgandDiagram:
    def __init__(self, *numbers):
        self.axislength = 5
        self.axes = pyplot.axes()
        self.axes.grid()
        self.axes.set_xlabel("Real")
        self.axes.set_ylabel("Imaginary")
        self.axes.set_title('Argand Diagram')

        for number in numbers:
            if number.real() > self.axislength: self.axislength = number.real()+2
            if number.imag() > self.axislength: self.axislength = number.imag()+2
        
        pyplot.xlim(-self.axislength, self.axislength)
        pyplot.ylim(-self.axislength, self.axislength)

        for number in numbers:
            self.axes.plot(*[numpy.linspace(0, number.real(), 2), numpy.linspace(0, number.imag(), 2)])
            self.axes.text(number.real(), number.imag(), f"{number}")
        
        pyplot.tight_layout()
        pyplot.show()


complexlist = [Complex(1,1), Complex(-2.5,4)]
ArgandDiagram(*complexlist)