import tkinter as tk
import sys
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import csv
import datetime


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.output()
        self.Output_Control()

    def Output_Control(self):
        self.form_control = tk.Frame(root)
        self.form_control.grid(column=3, row=3)
        self.clear_btn = ttk.Button(self.form_control, text="Clear", command=None)
        self.clear_btn.pack(side="right", padx=4, pady=4)
        self.export_btn = ttk.Button(self.form_control, text="Export", command=self.Write_To_File())
        self.export_btn.pack(side="right",padx=4, pady=4)


    def output(self):
    #Data Labels
        self.fourth_frame = tk.Frame(root)
        self.fourth_frame.grid(column=0, row=4)
        self.date_label = ttk.Label(self.fourth_frame, text="Date")
        self.date_label.grid(column=0, row=0)
        self.caliber_label = ttk.Label(self.fourth_frame, text="Caliber")
        self.caliber_label.grid(column=1, row=0)
        self.bullet_MFG_label = ttk.Label(self.fourth_frame, text="Bul MFG")
        self.bullet_MFG_label.grid(column=2, row=0)
        self.bullet_type_label = ttk.Label(self.fourth_frame, text="Bul Type")
        self.bullet_type_label.grid(column=3, row=0)
        self.powder_CHG_label = ttk.Label(self.fourth_frame, text="Pwd CH")
        self.powder_CHG_label.grid(column=4, row=0)
        self.powder_type_label = ttk.Label(self.fourth_frame, text="Pwd")
        self.powder_type_label.grid(column=5, row=0)
        self.powder_vol_label = ttk.Label(self.fourth_frame, text="Pwd Vol")
        self.powder_vol_label.grid(column=6, row=0)
        self.case_type_label = ttk.Label(self.fourth_frame, text="Case")
        self.case_type_label.grid(column=7, row=0)
        self.case_length_label = ttk.Label(self.fourth_frame, text="Length")
        self.case_length_label.grid(column=8, row=0)
        self.COAL_label = ttk.Label(self.fourth_frame, text="COAL")
        self.COAL_label.grid(column=9, row=0)
        self.primer_label = ttk.Label(self.fourth_frame, text="Primer")
        self.primer_label.grid(column=10, row=0)
        self.rounds_loaded_label = ttk.Label(self.fourth_frame, text="Rounds")
        self.rounds_loaded_label.grid(column=11, row=0)
    #Form Input Boxes
        self.to_day = datetime.datetime.now()
        self.date_box = ttk.Entry(self.fourth_frame,width=10)
        self.date_box.grid(column=0, row=1)
        self.date_box.insert(0, self.to_day.strftime("%d%b%Y")) #Sets default current date
        self.caliber_box = ttk.Entry(self.fourth_frame)
        self.caliber_box.grid(column=1, row=1)
        self.bullet_MFG_box = ttk.Entry(self.fourth_frame, width=10)
        self.bullet_MFG_box.grid(column=2, row=1)
        self.bullet_type_box = ttk.Entry(self.fourth_frame, width=10)
        self.bullet_type_box.grid(column=3, row=1)
        self.powder_CHG_box = ttk.Entry(self.fourth_frame, width=6)
        self.powder_CHG_box.grid(column=4, row=1)
        self.powder_type_box = ttk.Entry(self.fourth_frame,width=10)
        self.powder_type_box.grid(column=5, row=1)
        self.powder_volume_Box = ttk.Entry(self.fourth_frame,width=6)
        self.powder_volume_Box.grid(column=6, row=1)
        self.case_type = ttk.Entry(self.fourth_frame,width=10)
        self.case_type.grid(column=7, row=1)
        self.case_length_Box = ttk.Entry(self.fourth_frame,width=5)
        self.case_length_Box.grid(column=8, row=1)
        self.COAL_box = ttk.Entry(self.fourth_frame,width=10)
        self.COAL_box.grid(column=9, row=1)
        self.primer_box = ttk.Entry(self.fourth_frame,width=7)
        self.primer_box.grid(column=10, row=1)
        self.rounds_loaded_Box = ttk.Entry(self.fourth_frame,width=6)
        self.rounds_loaded_Box.grid(column=11, row=1)
        

    def Write_To_File(self):
        with open('test.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.date_box.get(0,"end"), self.caliber_box.get(0,"end"),
                        self.caliber_box.get(), self.bullet_MFG_box.get(),
                        self.bullet_type_box.get(), self.powder_CHG_box.get(),
                        self.powder_type_box.get(), self.powder_volume_Box.get(),
                        self.case_type.get(), self.case_length_Box.get(),
                        self.COAL_box.get(), self.primer_box.get(),
                        self.rounds_loaded_Box.get()])

if __name__ == "__main__":
    root=tk.Tk()
    root.title('Auto Logger')
    app=App(master=root)
    app.mainloop()
    root.mainloop()