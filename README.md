# Reloading-Press-Monitor
This is a great under taking taken by a Newb with zero experince. Press monitoring computers have been around for a while now, but are expensive in the 500 to 2k dollar range. Why not make a customisable one for less than 200 bucks.

This is a work in progress and I am inexperienced with github and python so bare with me as I learn. Critics, ideas, and pointers are welcome. I wanted something so i am making it and shareing. Plus the fun of creating something. The end goal is to have something modular and easy to understand that anyone with any level of experience can pick up and enter some user defined inputs and have press monitor to suit their needs for any style press.

GUI_Working: This is code that is working. As of thise time it is none functional.

***Functional Working update: The form clear button works and the form export buttons work. The CAM 1 and CAM2 buttons now work. Make sure you assign them to the correct camera.

-1_Old_Guizero: These were made with guizero. They have no functionality. I couldnt figure out how to incorporate OPencv. So left this as reference and to show learning progression.
-2_Old_Tkinter: This is where i converted guizero code into tkinter code. Wasnt hard and slightly intuitive. Starting to wonder if I should go back to this. Create the static widgets and call them in. Then have the functional widgets in one place.
-3_1_Class_TK_Gui: I converted the old tkinter into a class basesd writing style. I was hoping to add better readability. Adding funtionality its proving to be hard. Thought I would start with the forma data export functionality.... Three days and still havent gotten it to work.
 -3_2_Relaoding_Log: This is just an example of the output I am trying to get.
 -3_3_Cartridge_Recipe: This is just an example i created of the recipe data base the user can define and call in to prefill entry widgets.

-TK_Cam.py: An example to use for later so i can create tkinter cam frames. Lets you veiw one webcam currently.
-View_2.py: Lets you view two webcams at once via OpenCV. You may need to check the labeling of your capture device. I use VLC to see which capture device is which. This is if you just want to see two webcams at once. Requires OpenCV to be installed.

Sensors Folder: Where all the working sensors

-Open_Press_Count.py. Code works as it should. ***UPDate: Thanks to Jmorris from Cast Bullets for the primer counter idea. Stolen and imnplemted. S1 counts rounds up from zero and primers down from 100 and pulses the primer and powder vibrator motors. S2 resets round counter and S3 resets Primer counter back to 100 (user defined so change if you want). Need to add another switch to pause counter. 

-low_primer_warning: Event timed trigger solved. Code is working good now. Once light is sensed for 3 seconds the alarm is raised. This will prevent false alarms during primer feeding. ***Idea: use this code as a template to make code for case feeder and bullet feeder. Then if light is sensed for longer tha 8 seconds a low bullet and case allarm goes off.

-Bullet_and_Case_Feeder.py: This will operate the case feeder and bullet feeder at once with two relays.

-There are single relay operations if one just wants to drive a single relay. Files named accoredingly becuase my bullet and case feeders are wired differently.

Idea Folder:
-GUI picture is GUI i plan on making.
-Idea_Flow_Chart: Shows how i want it all to work.
-RPI_curcuit.cddx: A curcuit diagram file to show how i am currently wired up
-RPI_circut: a picture of the above file. Its my wire schematic.

Examples and testing:
-This where i keep all the examples and test files i have been using. There is a copy of the 3_1_TkinterGui i keep for referen. Tkinter with classes is the file i am activel editing for functionality..... cant figure out a simple form export at the moment.


Usefull Links:
-Link to Thingivers for Lee Low Primer warning sensor houseing.KPK3iF gets full credit for creating it. I tested it and it works great. You just drill a small throught the primer feeder trough:  https://www.thingiverse.com/thing:4303576

-In case you wonder how i watch the primers with a bore came: https://www.thingiverse.com/thing:3980090, full credit to RHaggmark for creating it.

-If you are wondering how the case feeder connects to my reloading press: https://www.tinkercad.com/things/eshs1PygjrH.

-Case Feeder i use:https://www.thingiverse.com/thing:3607034 use the remixed case dropper.

-Bullet Feeder - Sorry everyone Thingiverse took down the OBF again created by AmmoMike.

God Bless you all that are good at 3D design. I suck at it but my parts are useable.
