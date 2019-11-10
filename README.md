# PyArcadePaint

**Development State:**
Finished, may receive future updates.

## Info
PyArcadePaint is a python application that allows a user to draw something using a simple GUI, then convert it into python code with the single click of a button. This code will then be manually copied and pasted into an Arcade template in a .py file, which when run will draw the drawing the user drew in the GUI. It's simple, fast, and time-saving!

## File Structure
PyArcadePaint.py is the main program but runs at a very slow frame rate.<br/>
PyArcadePaintVBOVersion.py has less features and hapes to draw, but draws at a much faster frame rate due to it's use of Vertex Buffer Objects.

## Dependencies
[arcade python library](http://arcade.academy/) <br/>
[pymsgbox python library](https://pymsgbox.readthedocs.io/en/latest/basics.html) <br/>

## How To Use
1. Run the program.<br/>
2. Choose a shape to draw on the toolbar on the left side of the screen. <br/>
3. Choose a color to draw with on the toolbar on the left side of the screen. <br/>
4. Click somewhere on the drawing canvas, and hold the mouse until a second coordinate, then release the mouse button. A shape should appear on the screen. Repeat doing this for more shapes of various to appear on the screen. <br/>
5. When done drawing, click the export button at the top left corner of the screen. A popup message should appear confirming this, click ok. <br/>
6. Open your file explorer, navigate to this project's directory, and run Exported_Code.py. <br/>
8. Your drawing should appear. <br/>
