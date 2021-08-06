# tkinter_dndr
A package that provides tkinter (in python) with support for drag/drop and widget resizing of widgets directly on a GUI window


PLEASE READ THIS FILE TO FULLY UNDERSTAND AND USE THIS PACKAGE WITHOUT ISSUES.

----- GENERAL OVERVIEW OF THE PACKAGE (A tkinter Drag/Drop and Resize Package) -----

tkinter_DnDR is short form for tkinter_Drag/Drop, Resize

This package is one that provides drag/drop and widget resizing support to tkinter widget. What this means is that you (as programmer or user) can make your widget move to any position on the GUI window (drag/drop). It additionally means that you can resize your widget directly on the GUI window.

For widget resizing, you can resize your widget in any direction you can think of (even diagonally), whether:

UP (or NORTH) direction
DOWN(or SOUTH) direction
RIGHT (or EAST) direction
LEFT (or WEST) direction
UP-RIGHT (or NORTH-EAST) direction
UP-LEFT (or NORTH-WEST) direction
DOWN-RIGHT (or SOUTH-EAST) direction
DOWN-LEFT (or SOUTH-WEST) direction


----- HOW TO USE THIS PACKAGE -----

First import the tkinter_dndr module.
The tkinter_dndr module contains a class called DragDropResizeWidget. 

1) Create an instance/object of the DragDropResizeWidget class. This class receives your widget as a positional argument.

EXAMPLE: ```instance = DragDropResizeWidget(w)```, where w is the widget you want to give drag/drop or resize support

NOTE: Any instance of the DragDropResizeWidget class, contains three(3) methods:

a) ```instance.make_draggable()``` # Provides only drag/drop support to widget

b) ```instance.make_resizable()``` # Provides only resizing support to widget

c) ```intance.make_draggable_and_resizable()``` # Provides both drag/drop and resizing support to widget
   
2) Call any of the above methods (a,b or c) as you desire

e.g: ```instance.make_draggable()```

3) NOTE: I HAVE INCLUDED A test_dndr.py file. Run/Open this file to see and understand how this package works.


----- NOTE -----

-- To use the ```.make_draggable()``` method, your widget MUST use the PACK or PLACE layout managers (either ```.pack()``` or ```.place()```)

-- To use the ```.make_resizable()``` method, your widget MUST ONLY use the PLACE layout manager

-- To use the ```.make_draggable_and_resizable()``` method, your widget MUST ONLY use the PLACE layout manager

-- If using the ```.make_resizable()``` or ```.make_draggable_and_resizable_method()```, you MUST define x,y,width and height in .place() for your widget

e.g: ```widget.place(x=5, y=10, width=10, height=12)```

-- I will endeavour to make SUBSEQUENT VERSIONS of this package work well with any layout manager (whether ```.grid()```, ```.pack()``` or ```.place()```)


----- A USAGE EXAMPLE OF THIS PACKAGE -----

See the test_dndr.py file in the package directory for a usage example.


----- AUTHOR OUT :) -----

Feel free to reach me on gadawesome@gmail.com if you have anything you like urgently patched or added. 

If your software/project relies on this package fully supporting all layout managers or any other desired support/addition, I am only an email away.

HAPPY TO HELP :-D

IMPROVEMENTS/SUGGESTIONS are welcome :)
