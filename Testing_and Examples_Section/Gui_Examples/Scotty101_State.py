
# This program is derived from one by scotty101 (acknowledged with thanks) to help in examining and/or
# setting the state of Raspberry Pi GPIO ports.  All of the GPIO ports can have their input state monitored
# continuously (with or without pull-up or pull-down resistors) or set to output True or False logic levels.  
# The ports are initially presented in a passive state so as to avoid disruption of UART, I2C or SPI buses.  
# However, subsequent manipulation of the GPIO ports may well cause such disruption if insufficient care is taken.
# Provided such care is taken, this program can be run while UART, I2C and SPI buses are being used by other programs.  
# This program is invoked using a command such as: sudo python GPIO_manager.py
# This program is in the public domain and is freely available without warranty of any sort. 


from Tkinter import *
import RPi.GPIO as pi
import tkSimpleDialog
pi.setwarnings(False)

class LED(Frame):
    """A Tkinter LED Widget.
    a = LED(root,10)
    a.set(True)
    current_state = a.get()"""
    OFF_STATE = 0
    ON_STATE = 1
    
    def __init__(self,master,size=10,**kw):
        self.size = size
        Frame.__init__(self,master,width=size,height=size)
        self.configure(**kw)
        self.state = LED.OFF_STATE
        self.c = Canvas(self,width=self['width'],height=self['height'])
        self.c.grid()
        self.led = self._drawcircle((self.size/2)+1,(self.size/2)+1,(self.size-1)/2)
    def _drawcircle(self,x,y,rad):
        """Draws the circle initially"""
        color="white"
        return self.c.create_oval(x-rad,y-rad,x+rad,y+rad,width=rad/5,fill=color,outline='black')
    def _change_color(self):
        """Updates the LED colour"""
        if self.state == LED.ON_STATE:
            color="green"
        else:
            color="red"
        self.c.itemconfig(self.led, fill=color)
    def set(self,state):
        """Set the state of the LED to be True or False"""
        self.state = state
        self._change_color()
    def get(self):
        """Returns the current state of the LED"""
        return self.state

class GPIO(Frame):
    """Each GPIO class draws a Tkinter frame containing:
    - A Label to show the GPIO Port Name
    - A data direction spin box to select pin as input or output
    - A checkbox to set an output pin on or off
    - An LED widget to show the pin's current state"""

    gpio_modes = ("Passive","Input with pull-up","Input with pull-down","Input")
# Passive mode is replaced by Output mode after the 1st manipulation of each Spinbox occurs    
    def __init__(self,parent,pin=0,hpin=0,name=None,**kw):
        self.pin = pin
        if name == None:
            if hpin > 9:
                self.name = "Header Pin %s" % (str(hpin))
            else:
                self.name = "Header Pin  %s" % (str(hpin)) + " "
        Frame.__init__(self,parent,width=150,height=20,relief=SUNKEN,bd=1,padx=5,pady=5) 
        self.bind('<Double-Button-1>', lambda e, s=self: self._configurePin(e.y))
        self.parent = parent
        self.configure(**kw)
        self.state = False
        self.active = False
        self.cmdState = IntVar()
        self.Label = Label(self,text=self.name)
        self.mode_sel = Spinbox(self,values=self.gpio_modes,justify=CENTER,wrap=True,command=self.setMode)
        self.set_state = Checkbutton(self,text="High/Low",variable=self.cmdState,command=self.toggleCmdState)
        self.led = LED(self,20)
        self.Label.grid(column=0,row=0)
        self.mode_sel.grid(column=1,row=0)
        self.set_state.grid(column=2,row=0)
        self.led.grid(column=3,row=0)
        self.set_state.config(state=DISABLED)

    def isOutput(self):
        """Returns True if the current pin is an output"""
        return (self.mode_sel.get() == "Output")

    def setMode(self):
        """Sets the GPIO port to match the value in the spinbox"""
        self.active = True
        if (self.mode_sel.get() == "Passive"):
            self.mode_sel.delete(0,7) # Replace "Passive" descriptor with "Output" in Spinbox
            self.mode_sel.insert(INSERT,"Output") 
            self.set_state.config(state=NORMAL)
            pi.setup(self.pin,pi.OUT)
            self.state = self.cmdState.get()
            self.updateLED()
            self.updatePin()
        elif (self.mode_sel.get() == "Input"):
            self.set_state.config(state=DISABLED)
            pi.setup(self.pin,pi.IN)
        elif (self.mode_sel.get() == "Input with pull-up"):
            self.set_state.config(state=DISABLED)
            pi.setup(self.pin,pi.IN, pull_up_down=pi.PUD_UP)
        else:
            self.set_state.config(state=DISABLED)
            pi.setup(self.pin,pi.IN, pull_up_down=pi.PUD_DOWN)
        self.updateLED()

    def toggleCmdState(self):
        """Reads the current state of the checkbox, updates LED widget
        and sets the gpio port state."""
        self.state = self.cmdState.get()
        self.updateLED()
        self.updatePin()

    def updatePin(self):
        """Sets the GPIO port state to the current state"""
        pi.output(self.pin,self.state)

    def updateLED(self):
        """Refreshes the LED widget depending on the current state"""
        self.led.set(self.state)

    def updateInput(self):
        """Updates the current state if the pin is an input and sets the LED"""
        if not self.isOutput():
            if (self.active == True):
                state = pi.input(self.pin)
                self.state = state
                self.updateLED()

class App(Frame):
    def __init__(self,parent=None, **kw):
        Frame.__init__(self,parent,**kw)
        self.parent = parent
        pi.setmode(pi.BCM)
        self.ports = []
        col_idx = range(1,18)
        gpio = (2,3,4,14,15,17,18,27,22,23,24,10,9,25,11,8,7)
        headerpin = (3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26)
        for col,p,hp in zip(col_idx,gpio,headerpin):
            self.ports.append(GPIO(self,pin=p,hpin=hp))
            self.ports[col-1].grid(row=col)

        self.update()

    def onClose(self):
        """This is used to run the Rpi.GPIO cleanup() method to return pins to be an input
        and then destory the app and its parent."""
        pi.cleanup()
        self.destroy()
        self.parent.destroy()

    def readStates(self):
        """Cycles through the assigned ports and updates them based on the GPIO input"""
        for port in self.ports:
            port.updateInput()
                    
    def update(self):
        """Runs every 100ms to update the state of the GPIO inputs"""
        self.readStates()
        self._timer = self.after(100,self.update)
        

def main():
    root = Tk()
    root.title("Raspberry Pi GPIO Manager")
    a = App(root)
    a.grid()
    """When the window is closed, run the onClose function."""
    root.protocol("WM_DELETE_WINDOW",a.onClose)
    root.mainloop()
   

if __name__ == '__main__':
    main()