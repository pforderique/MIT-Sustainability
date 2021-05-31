from tkinter import Tk, Label
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from helpercode.timeseries import extract_per_year
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#theme colors
BURGANDY = '#630019'
DARK_BURGANDY = '#3d0110'
LIGHT_BEIGE = '#e6c88e'
DARK_GREY = '#454545'
FONT_LARGE = ("Times New Roman Bold", 25)
FONT_MEDIUM = ("Times New Roman Bold", 13)

# data
MODELS = ('GFDL','IPSL', 'OBSERVATION')
VARIABLES = ('pr', 'tasmax')
SSPS = ('rcp85','GSWP3')

class IsimipVisualizer(Tk):

    def __init__(self):
        super().__init__()

        self.title('ISIMIP Visualizer')
        self.geometry('1100x700')
        self.config(bg=DARK_BURGANDY)

        self.model = MODELS[0]
        self.variable = VARIABLES[1]
        self.ssp = SSPS[0]

        self._create_window_title()
        self._add_selection_boxes(3, 3, 3)
        
    def _set_model(self, event):
        self.model = self.modelcombo.get()

        if self.model == 'OBSERVATION':
            self.ssp = 'GSWP3'
            self.sspcombo.current(len(SSPS) - 1)

        self.create_visual()

    def _set_variable(self, event):
        self.variable = self.varcombo.get()
        self.create_visual()

    def _set_ssp(self, event):
        self.ssp = self.sspcombo.get()

        if self.ssp == 'GSWP3':
            self.model = 'OBSERVATION'
            self.modelcombo.current(len(MODELS) - 1)

        self.create_visual()

    def _create_window_title(self):
        titleLabel = Label(self, text="ISIMIP5 Visualizer", font=FONT_LARGE, bg=DARK_BURGANDY,fg='white')
        titleLabel.pack(pady=10)

    def _add_selection_boxes(self, xpos, ypos, data):
        # model
        lbl_combo = Label(self, text="Select Model:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=0.02,rely=0.2)
        self.modelcombo = Combobox(self,values=MODELS,state="readonly",width=35)
        self.modelcombo.place(relx=0.02,rely=0.25)
        self.modelcombo.current(0)
        self.modelcombo.bind("<<ComboboxSelected>>", self._set_model)

        # variable
        lbl_combo = Label(self, text="Select Variable:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=0.02,rely=0.3)
        self.varcombo = Combobox(self,values=VARIABLES,state="readonly",width=35)
        self.varcombo.place(relx=0.02,rely=0.35)
        self.varcombo.current(0)
        self.varcombo.bind("<<ComboboxSelected>>", self._set_variable)

        # ssp
        lbl_combo = Label(self, text="Select ssp:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=0.02,rely=0.4)
        self.sspcombo = Combobox(self,values=SSPS,state="readonly",width=35)
        self.sspcombo.place(relx=0.02,rely=0.45)
        self.sspcombo.current(0)
        self.sspcombo.bind("<<ComboboxSelected>>", self._set_ssp)


    def create_visual(self):
        data = extract_per_year(self.model, self.variable, self.ssp)
        print(self.model, self.variable, self.ssp)

        figure = Figure(figsize=(8,5.8), dpi=90)
        figure.patch.set_facecolor(LIGHT_BEIGE)
        ax = figure.add_subplot(111)

        ax.set_title(f"{self.model} {self.variable} {self.ssp}")
        ax.set_xlabel('YEARS')
        ax.set_ylabel(self.variable)

        YEARS = [year for year in range(2006, 2100)]
        if self.model == 'OBSERVATION':
            YEARS = [yr for yr in range(1901, 1901+len(data))]
            self.ssp = 'GSWP3'

        ax.plot(YEARS[:len(data)], data, 'o-')

        #embedding
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25,rely=0.2)

if __name__ == "__main__":
    root = IsimipVisualizer()
    root.mainloop()