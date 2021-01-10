# Reloading-Press-Monitor

**A disclaimer:**  The logo I am currently using is to one of my favorite websites. They own it and I found it on Google images. You can change it to what ever you like or a family crest or any other personal logo. The code will automatically resize it.

This has been a fun adventure and I feel I graduated from Newb to Novice working on this. Press monitoring computers have been around for a while now, but are expensive in the 500 to 2k dollar range. Why not make a customisable one for less than 200 bucks?

This is a work in progress as I gain experience in github and python, so bare with me as I learn. Critiques, ideas, and pointers are welcome. I wanted something so I am making it and shareing. Plus the fun of creating something. The end goal is to have something modular and easy to understand that anyone with any level of experience can pick up and enter some user defined inputs and have press monitor to suit their needs for any style press.  
Tasks left:  
- [ ] Code Powder Resevior Sensore (recieved)  
- [ ] Figure out bullet not present system. May have to wait till i get my press back.
- [ ] Start figuring out how to make this modular.
- [ ] Programming LCD. The new LCD was recieved and works.
- [ ] Contemplatiing a powder cop die sensor. Still in research and design.  
- [ ] Bullet not present sensor. Still in research and design.
- [ ] Convince wife to let me get a Dillion to make a full auto press and try out all the posibilities.  


## GUI_Working Folder

As of right now the functionality is as follows:

- 1_Old_Guizero: These were made with guizero. They have no functionality. I couldnt figure out how to incorporate OPencv. So left this  as reference and to show learning progression.  
- 2_Old_Tkinter: This is where i converted guizero code into tkinter code. Wasnt hard and slightly intuitive. Starting to wonder if I should go back to this. Create the static widgets and call them in. Then have the functional widgets in one place.  
- 3_1_Class_TK_Gui: I converted the old tkinter into a class basesd writing style. I was hoping to add better readability. This is now the main program file.  
  - Functionality is as follows:  
    - The forms works. You can clear and save reloading log into csv. App has its own log which you can copy and paste out of. You may also use the file, copy selection to copy your data to clip board and the simply paste into your own excel or open office file.
    - The recipe editor works and updates the pet loads combo box. You can edit your pet loads file your self with your favorite excel eqavalent program. You must save as CSV file format though. Onboard editor works 4.0 though.
    - Both camera buttons work. You must verify your cam buttons device numbers. Plug two usb cams in and see what they are. Then manually input those numbers. Current defaults are 0 and 1. Thats what mine are. 
    - I have not written user manual yet. The file and functionality is there for when I get everything done. This will be the last thing I do.  
    - Current GPIO functionality: Counters work and export correctly. Motors vibrate correctly. Low primer warning works now with timing function, so warning gets set if no primers seen for .2 seconds.  Binding works and works like limit switches and if cycle takes longer than preset amount alert is set (this is for automation). Low case and low bullets work. If feeding takes longer than preset time then alert is set to refill hoppers. Bullet and case feeding functionality works. **For the Alerts:** Clicking the button resets the alerts. So if a lock is written for automation (not yet written) then clicking button would restart the automation. The silence button just shuts off the buzzer you can clear the fault. Then click the button and resume.  

- 3_2_Relaoding_Log: This is where the form is logged. Removed count entry and count is now pulled from the count box. This file is needed for program to function.  
- 3_3_Cartridge_Recipe: This is just an example I created of the recipe data base the user can define and call in to prefill entry widgets. This is the file that gets edited when you remove and add pet loads. Also the file you can manually edit if you so choose. This file is also needed for functinality.  
- TK_Cam.py: An example I found that that I used to veiw the webcams.    
- View_2.py: This is the python file that started this quest. Lets you view two webcams at once via OpenCV. You may need to check the labeling of your capture device. I use VLC to see which capture device is which. This is if you just want to see two webcams at once. Requires OpenCV to be installed.  

## Sensors Folder

Where all the working sensors are:

- Open_Press_Count.py. Code works as it should. ***UPDate: Thanks to Jmorris from Cast Bullets for the primer counter idea. Stolen and imnplemted. S1 counts rounds up from zero and primers down from 100 and pulses the primer and powder vibrator motors. S2 resets round counter and S3 resets Primer counter back to 100 (user defined so change if you want). Need to add another switch to pause counter.  
- low_primer_warning: Event timed trigger solved. Once light is sensed for 3 seconds the alarm is raised. This will prevent false alarms during primer feeding. Then if light is sensed for longer tha 8 seconds a low bullet and case allarm goes off. *I had use a different method in the code. This does work as is but not in the GUI code.*  
- Bullet_and_Case_Feeder.py: This will operate the case feeder and bullet feeder at once with two relays.  
- There are single relay operations if one just wants to drive a single relay. Files named accoredingly becuase my bullet and case feeders are wired differently.  

## Idea Folder

- GUI picture is GUI i plan on making.  
- Idea_Flow_Chart: Shows how i want it all to work.  
- RPI_curcuit.cddx: A curcuit diagram file to show how i am currently wired up  
- RPI_circut: a picture of the above file. Its my wire schematic.  

## Examples and testing

- This where I keep all the examples and test files I have been using. There is a copy of the 3_1_TkinterGui I keep for reference.  
- Inwork_Gui.Py is the file I am activel editing and testing. Once functional I copy and past to the 3_1_TkinterGui.

## PCB

All PCBs amd schematics were made with EasyEDA. Its free and not too bad to learn for a newb. Learned a lot about design rules. 

Here are all the PCB designs to incorporate all the electronics neccassy for functionality. The Gerber files are what is needed if you wish to have it proffessional made like I did. The BOM file is a list of all the parts needed. There are schematics for the PCB and a SVG to show a picture preview.


## Electronics_Enclosure

Here is the STLs and preview images of the elctronics enclosures I designed. The LCD enclosure is tiltable. The project box is a clam shell design with cuts out for all of the connectors. Both of theses designs are still in the prototype phase and not finnished.

## Usefull Links

- Link to Thingivers for Lee Low Primer warning sensor houseing.KPK3iF gets full credit for creating it. I tested it and it works great. You just drill a small throught the primer feeder trough:  https://www.thingiverse.com/thing:4303576  
- In case you wonder how i watch the primers with a bore came: https://www.thingiverse.com/thing:3980090, full credit to RHaggmark for creating it.  
- If you are wondering how the case feeder connects to my reloading press: https://www.tinkercad.com/things/eshs1PygjrH. 
- Link to the TinkerCad Open Source Monitor if you wish to change it : https://www.tinkercad.com/things/efoQFT3AIY3
- Link to the TinkerCad Open Source Monitor if you wish to change it: https://www.tinkercad.com/things/7L2IhnNIFGC 
- Case Feeder I use: https://www.thingiverse.com/thing:3607034 use the remixed case dropper.  
- Bullet Feeder: Sorry everyone Thingiverse took down the OBF again created by AmmoMike.
  
God Bless you all that are good at 3D design. I suck at it but my parts are useable.
