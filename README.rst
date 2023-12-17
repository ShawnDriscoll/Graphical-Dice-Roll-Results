**Graphical Dice Roll Results for Python 3.11**
===============================================

**Graphical Dice Roll Results** is a Python 3.11 program for rolling various dice using PyQt5 and Matplotlib.

.. figure:: images/graphical_dice_roll_app.png

.. figure:: images/graphical_dice_roll_audit.png


Some Things Required
--------------------

* **Windows 11**

  This code will still run on Windows 10.

* **Python 3.11**

  This code was written using Python 3.11.6.

* **PyQt5 5.15.9**

  PyQt5 is the framework used for displaying the Window GUI and buttons, etc.
   
* **numpy 1.26.0**

  For building arrays.

* **matplotlib 3.8.0**

  For graphics plotting.

* **pyttsx3 2.90**

  For the MS Zira and MS David voices (it will try to detect other SAPI voices installed).


Don't Have Python?
------------------

The .EXE version can be run in Windows 11 or 10.


.. |ss| raw:: html

    <strike>

.. |se| raw:: html

    </strike>

Things To-Do
------------

| Add more dice roll types.
| Instruction manual.
| Cheat codes.
|ss|

| Switch over to Python 3.11 for faster calculations.
| Voice manual input roll results.
| Switch to using pydice 3.8 for die rolls.
| Secret roll types added.
| Add Advantage and Disadvantage roll types.
| Make it talk.
| Graph manually entered dice rolls as well.
| Start on a To-Do.

|se|

**Known History**

* v0.6.0b

  Success dice (**S6** and **S10**) have been added.

* v0.5.8b

  Increased accuracy to 500,000 iterations.
  Reports the mean average of rolls if applicable.

* v0.5.7b

  Increased accuracy to 100,000 iterations.

* v0.5.6b

  Updated for Windows 11. Will still run on Windows 10.

* v0.5.5b

  Fixed crash caused when the amount of high or low number of dice to keep was missing.

* v0.5.4b

  FATE dice were using the wrong random() for some reason. Fixed.

* v0.5.3b

  Will now use the Microsoft Desktop SAPI voices you have installed. Not just Zira and David.

* v0.5.2b

  Fixed str being added to int errors when rolling dice at ``CMD`` prompt.

* v0.5.1b

  Added **Sicherman** dice rolls.
  Better logging for dice starting with a **0** instead of a **1**.

* v0.5.0b

  Updated for Python 3.11. Runs much faster.

* v0.4.6b

  Error-trapping for invalid dice modifiers now.
  The new **D1** roll generates values **0 - 1**.
  The **D2** roll now generates values **1 - 2**.

* v0.4.5b

  Roll accuracy for result chart is adjustable.
  pydice module updated.

* v0.4.4b

  Fixed infinite loop. (Haven't seen one of those in decades.)

* v0.4.3b

  Uses updated pydice module.

* v0.4.2b

  Removed roll samples when manual rolls were invalid.
  
* v0.4.1b

  Increased error-trapping of any out-of-bound rolls during brute force percentage calculations.
  Roll results from manual inputs are now voiced as well.
  Number of dice and dice modifier ranges have been increased.

* v0.4.0b

  Now uses pydice 3.8 for its die rolling.
  Added error-trapping when performing **MINMAXAVG** rolls at the CMD prompt.
  Displays a sample of ten random rolls.

* v0.3.2b

  Fixed die roll range when adding a -DM to a roll.

* v0.3.1b

  Added secret rolls types based on the 4dF roll.

* v0.3.0b

  Added **Advantage** and **Disadvantage** roll types.
  
  .. image:: images/video.png
    :target: https://www.youtube.com/watch?v=89AzLRwAToU

* v0.2.0b

  It talks now.

* v0.1.0b

  Initial release.
  Graphing works with manual rolls also.


Contact
-------
Questions? Please contact shawndriscoll@hotmail.com
