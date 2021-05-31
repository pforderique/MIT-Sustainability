'''
This is the MAIN GUI for the ISIMIP Project.
Allows for comparison of isimip5_models
'''

from tkinter import Tk, Label
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from isimip5.analysis.helpercode.timeseries import extract_per_year as isimip5_extract_per_year
from isimip6.analysis.helpercode.timeseries import extract_per_year as isimip6_extract_per_year
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#theme colors
BURGANDY = '#630019'
DARK_BURGANDY = '#3d0110'
LIGHT_BEIGE = '#e6c88e'
DARK_GREY = '#454545'
FONT_LARGE = ("Times New Roman Bold", 25)
FONT_MEDIUM = ("Times New Roman Bold", 13)

# data
isimip5_models = ('GFDL','IPSL', 'HadGEM2', 'MIROC5', 'OBSERVATION')
isimip5_variables = ('pr', 'tasmax')
isimip5_ssps = ('rcp85','GSWP3')

isimip6_models = ('GFDL','IPSL', 'MRI', 'OBSERVATION')
isimip6_variables = ('pr', 'tasmax')
isimip6_ssps = ('ssp585', 'W5E5v1.0')

class IsimipVisualizer(Tk):

    def __init__(self):
        super().__init__()

        self.title('ISIMIP Comparison Visualizer')
        self.geometry('1100x700')
        self.config(bg=DARK_BURGANDY)

        self.model5 = isimip5_models[0]
        self.variable5 = isimip5_variables[0]
        self.ssp5 = isimip5_ssps[0]
        self.model6 = isimip6_models[0]
        self.variable6 = isimip6_variables[0]
        self.ssp6 = isimip6_ssps[0]

        self.version = "BOTH" #BOTH, isimip5 only, isimip6 only
        self.show_isimip5 = True
        self.show_isimip6 = True

        self._create_window_title()
        self._add_version_selection()
        self._add_isimip5_selection_boxes()
        self._add_isimip6_selection_boxes()

    def _create_window_title(self):
        titleLabel = Label(self, text="ISIMIP Comparison Visualizer", font=FONT_LARGE, bg=DARK_BURGANDY,fg='white')
        titleLabel.pack(pady=10)
        
    def _set_model5(self, event):
        self.model5 = self.model5combo.get()
        if self.model5 == 'OBSERVATION':
            self.ssp5 = 'GSWP3'
            self.ssp5combo.current(len(isimip5_ssps) - 1)
        self.create_visual()

    def _set_variable5(self, event):
        self.variable5 = self.var5combo.get()
        self.create_visual()

    def _set_ssp5(self, event):
        self.ssp5 = self.ssp5combo.get()
        if self.ssp5 == 'GSWP3':
            self.model5 = 'OBSERVATION'
            self.model5combo.current(len(isimip5_models) - 1)
        self.create_visual()

    def _set_model6(self, event):
        self.model6 = self.model6combo.get()
        if self.model6 == 'OBSERVATION':
            self.ssp6 = 'W5E5v1.0'
            self.ssp6combo.current(len(isimip6_ssps) - 1)
        self.create_visual()

    def _set_variable6(self, event):
        self.variable6 = self.var6combo.get()
        self.create_visual()

    def _set_ssp6(self, event):
        self.ssp6 = self.ssp6combo.get()
        if self.ssp6 == 'W5E5v1.0':
            self.model6 = 'OBSERVATION'
            self.model6combo.current(len(isimip6_models) - 1)
        self.create_visual()

    def _set_version(self, event):
        self.version = self.versionCombo.get()
        print(self.version)
        if self.version == "isimip5 only": self.show_isimip5, self.show_isimip6 = True, False
        elif self.version == "isimip6 only": self.show_isimip5, self.show_isimip6 = False, True
        elif self.version == "both": self.show_isimip5, self.show_isimip6 = True, True
        self.create_visual()

    def _add_version_selection(self, xpos=0.32, ypos=0.12):
        # version
        lbl_combo = Label(self, text="Select Comparison:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos)
        self.versionCombo = Combobox(self,values=("isimip5 only", "isimip6 only", "both"),state="readonly",width=35)
        self.versionCombo.place(relx=xpos+0.15,rely=ypos)
        self.versionCombo.current(2)
        self.versionCombo.bind("<<ComboboxSelected>>", self._set_version)

    def _add_isimip5_selection_boxes(self, xpos=0.02, ypos=0.3, version_label="Select ISIMIP5 Data:"):
        # version label (isimip5 or 6)
        version_lbl = Label(self, text=version_label, font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        version_lbl.place(relx=xpos,rely=ypos)

        # model
        lbl_combo = Label(self, text=">>> Model:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.05)
        self.model5combo = Combobox(self,values=isimip5_models,state="readonly",width=10)
        self.model5combo.place(relx=xpos+0.12,rely=ypos+0.05)
        self.model5combo.current(0)
        self.model5combo.bind("<<ComboboxSelected>>", self._set_model5)

        # variable
        lbl_combo = Label(self, text=">>> Variable:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.1)
        self.var5combo = Combobox(self,values=isimip5_variables,state="readonly",width=10)
        self.var5combo.place(relx=xpos+0.12,rely=ypos+0.1)
        self.var5combo.current(0)
        self.var5combo.bind("<<ComboboxSelected>>", self._set_variable5)

        # ssp
        lbl_combo = Label(self, text=">>> ssp:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.15)
        self.ssp5combo = Combobox(self,values=isimip5_ssps,state="readonly",width=10)
        self.ssp5combo.place(relx=xpos+0.12,rely=ypos+0.15)
        self.ssp5combo.current(0)
        self.ssp5combo.bind("<<ComboboxSelected>>", self._set_ssp5)

    def _add_isimip6_selection_boxes(self, xpos=0.02, ypos=0.6, version_label="Select ISIMIP6 Data:"):
        # version label (isimip5 or 6)
        version_lbl = Label(self, text=version_label, font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        version_lbl.place(relx=xpos,rely=ypos)

        # model
        lbl_combo = Label(self, text=">>> Model:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.05)
        self.model6combo = Combobox(self,values=isimip6_models,state="readonly",width=10)
        self.model6combo.place(relx=xpos+0.12,rely=ypos+0.05)
        self.model6combo.current(0)
        self.model6combo.bind("<<ComboboxSelected>>", self._set_model6)

        # variable
        lbl_combo = Label(self, text=">>> Variable:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.1)
        self.var6combo = Combobox(self,values=isimip6_variables,state="readonly",width=10)
        self.var6combo.place(relx=xpos+0.12,rely=ypos+0.1)
        self.var6combo.current(0)
        self.var6combo.bind("<<ComboboxSelected>>", self._set_variable6)

        # ssp
        lbl_combo = Label(self, text=">>> ssp:", font=FONT_MEDIUM,bg=DARK_BURGANDY,fg='white')
        lbl_combo.place(relx=xpos,rely=ypos+0.15)
        self.ssp6combo = Combobox(self,values=isimip6_ssps,state="readonly",width=10)
        self.ssp6combo.place(relx=xpos+0.12,rely=ypos+0.15)
        self.ssp6combo.current(0)
        self.ssp6combo.bind("<<ComboboxSelected>>", self._set_ssp6)

    def create_visual(self):
        color5, color6 = 'tab:red', 'tab:cyan'
    
        figure = Figure(figsize=(8,5.8), dpi=90)
        figure.patch.set_facecolor(LIGHT_BEIGE)
        ax1 = figure.add_subplot(111)
        ax1.tick_params(axis='y', labelcolor=color5)

        FIGURE_TITLE = ""

        if self.show_isimip5:
            data = isimip5_extract_per_year(self.model5, self.variable5, self.ssp5)
            print("isimip5 data plotted:", self.model5, self.variable5, self.ssp5)

            FIGURE_TITLE += f"| ISIMIP5: {self.model5} {self.variable5} {self.ssp5} |"
            ax1.set_ylabel(self.variable5)

            if self.model5 == "OBSERVATION": start_year = 1901
            else: start_year = 2006

            YEARS_5 = [year for year in range(start_year, start_year+len(data))]
            ax1.plot(YEARS_5[:len(data)], data, 'o-', color=color5)

        if self.show_isimip6:
            data = isimip6_extract_per_year(self.model6, self.variable6, self.ssp6)
            print("isimip6 data plotted:", self.model6, self.variable6, self.ssp6)

            FIGURE_TITLE += f"| ISIMIP6: {self.model6} {self.variable6} {self.ssp6} |"

            if self.model6 == "OBSERVATION": start_year = 1979
            else: start_year = 2015

            YEARS_6 = [year for year in range(start_year, start_year+len(data))]

            if self.show_isimip5 and self.variable5 == self.variable6:
                ax1.plot(YEARS_6[:len(data)], data, 'o-', color=color6) # use same plot
            else:
                #? instantiate a second axes that shares the same x-axis
                ax2 = ax1.twinx()
                ax2.tick_params(axis='y', labelcolor=color6)
                ax2.set_ylabel(self.variable6)
                ax2.plot(YEARS_6[:len(data)], data, 'o-', color=color6) # use same plot

        ax1.set_title(FIGURE_TITLE)
        ax1.set_xlabel('YEARS')
        ax1.legend(['isimip5', 'isimip6'])

        #embedding
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25,rely=0.2)

if __name__ == "__main__":
    root = IsimipVisualizer()
    root.mainloop()