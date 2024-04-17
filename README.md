# C21
[![es](https://img.shields.io/badge/Cambiar_Lenguaje_a-Espa%C3%B1ol-%2369EAA1?style=flat
)](https://github.com/ktehllama/C21/blob/main/README.es.md)

## Casinos Hate This One Simple Trick!
In all seriousness, C21 is a _Blackjack Card Counting Calculator_ with an integrated
GUI made using the [Tkinter](https://docs.python.org/3/library/tkinter.html) library. It has 4 integrated card counting methods (that are mentioned in more 
detail later in this beautiful read-me), a full-color terminal interface and many more features
for all your online card counting needs, or to just ~~steal~~ borrow some code, don't we all.

- Fast & Compact
- Some Understanding of Blackjack Required
- 🔥 Beat the Casino 🔥

<details>
  <summary>Images (Click Me):</summary>
<br>
<img src="https://github.com/ktehllama/C21/blob/main/C21-imgs/c21-startup.PNG" alt="c21-startup" />
<br>
<img src="https://github.com/ktehllama/C21/blob/main/C21-imgs/c21-demo.PNG" alt="c21-demo" />
</details>

## Before we start...
Before you can use this tool effectively, it's important you have a concrete understanding of
the following:
- How to play Blackjack
- How the card counting methods that are used in C21 work
- How to use basic strategy charts

Learning how to play Blackjack is probably the simplest of all, you can watch [this amazing video by
Blackjack Apprenticeship](https://www.youtube.com/watch?v=PljDuynF-j0) on learning Blackjack quickly and easily. You would also need to memorize different key words
that are commonly used when talking about Blackjack, such as running count, true count, deck penetration, and more.
All you need to do is memorize how the card counting methods work to learn how to use them. The ones used
in C21 are:
- [HiLo](https://wizardofodds.com/games/blackjack/card-counting/high-low/)
- [Omega II](https://www.casinoguardian.co.uk/blackjack/omega-ii-blackjack-system/)
- [KO](https://www.bonusinsider.com/blackjack/the-knock-out-card-counting-system/)
- [Ace Five Count](https://wizardofodds.com/games/blackjack/ace-five-count/)

You can click the links to learn more about the methods or you can go to the `bjstrats.yaml` file in the
project, where under the name of the method there is a `description` tag that has all the info
nice and condensed for reading, though I would still recommend visting the websites linked above.

Finally, basic strategy charts teaches you exactly when to: hit or stand, double down, split pairs or
surrender. These are extremely useful to have and I recommend [this one](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/), also by Blackjack Apprenticeship.

## Exe Installation
This section is for if you want to use the EXE version of C21 where you don't need to install Python, just
instlal the program file, the settings file and the methods file.

Install the folder as a Zip and Unzip it. Before doing anything, there are two important files: 
- `c21_settings.json` 
- `e_bjstrats.yaml`

### c21_settings
This is a settings file where you tell the program how many decks of cards you're using, this is
essential since everything would break if this file were not here. The default amount of decks is `6`; but if you
are playing with more or less decks, all you have to do is open the JSON file, and edit the number next to the
`decks_amount` value. The __maximum amount__ of decks you can play with is `8`, and the __minimum__ is `1`.
```json
{"decks_amount":6}
```

### e_bjstrats
This is the methods file that contains all the logic of how to count cards and tells the program what language its in, this should not be deleted 
under any circumstances (unless you want to test something or whatever you want to do). 
On default installation the language is in __English__. If you want to change it to __Spanish__ which is the only
supported language as of now, you can delete everything in the file, and replace it with this:

[Spanish Version For e_bjstrats.yaml](https://github.com/ktehllama/C21/blob/main/C21-imgs/C21-Version-Espa%C3%B1ol)

> Pro Tip:
Don't change anything in here if you're not sure what it does.
Also if you accidentally delete the `e_bjstrats.yaml` file, just make another file
with the same name add copy the same content it had before in it to the new file,
make sure to make the file in the same folder.

### Possible Errors
You might get an error from your Windows defender that this is a suspicious file, and this is normal.
Every EXE file downloaded from github is flagged as dangerous, but I promise this is not one of those.
If you don't trust me, then you can install Python normally, install the normal C21 files 
and run the code natively where you can see it.

After you downloaded everything and changed the settings as you'd like, you now have an EXE file
that can directly run C21, just remember to keep all the files together in the same folder.

## Installation
C21 requires a [Python](https://www.python.org/) version 3.10 or above. Once you've installed Python and set it up,
install C21 as a Zip file and run the main file: `akr_main.py`

> __Important note__:
Later on, I will add an EXE file where the calculator can be run directly without the need
to install Python.

The only pip installation needed is `pyyaml` and `termcolor`, the helper files are all there
and the rest of the modules are already build into Python.
```
pip install pyyaml
pip install termcolor
```

__IMPORTANT__: Before you run the program though, you need to change the `method_file` variable in
`method_parse.py`, located at the top of the script after the imports, to the _file path_ of your `bjstrats.yaml` file.
This is where all the methods are stored, and is essential for C21. If no yaml file is found, the terminal
will throw an error, or not run at all. You also have to change the `DECKS` constant near the top of
`akr_main.py` to the number of decks you are playing with, it's set to `6` by default.

## How to use C21
When you run the main file, a calculator GUI will pop up on the screen and the terminal will supply you with
info about the current methods that are running and the status overall of the program.
This window is resizable and I highly recommend you resize it to your liking, just don't make it too small.

There are 4 different parts to this calculator:
- The ___methods matrix___, located top left with four sections
- The ___information sidebar___, located to the right of the methods matrix
- The ___history bar___, located under the methods matrix
- And the ___card keypad___, located under the history bar

### Methods matrix
This section is divided into four, one quadrant for each method.

__TOP ROW:__ HiLo, Omega II
__BOTTOM ROW:__ KO, ACEFC (For the remainder of this readme, Ace Five Count will be shortened to this)

Top row methods are all balanced systems meaning they have true counts, the bottom row ones only have running counts. 
The color of the boxes will change from red to blue to green depending on the true count and running count. 
These colors represent the betting recommendations, or in other words how much you should bet on the next round. 
Recommendations are also shown in text under the _RC_ and _TC_ (Running count, True count).

__SPECTRUM:__ 🟥 Red: Bet the minimum -> 🟦 Blue: Neutral bet -> 🟩 Green: Increase bet

This is the most important section out of all of them as it tells you how to scale your bets accordingly, pay
close attention and memorize all the method's interactions with one another.

### Information Sidebar
To the right of the methods matrix is the information sidebar. It tells you your last played card (PC),
the decimal amount of decks left (DL) and the number of all the cards left in the deck (AC).

### History Bar
Below the methods matrix is the history bar. It shows you the last _10_ cards you have played, with
the leftmost index being the most recent, and the rightmost one being the latest.
(All _Jacks, Queens and Kings_ are counted as _Tens_)

```
Most Recent >---------------> Oldest
History: 5, 6, A, 9, 10, 2, A, 2, 10
```

> __Pro Tip:__
You can change the limit of the cards it shows from 10 to another number by going
to the `append_limit` function and changing the `limit` parameter default value
to another number. Try to not make it too big as all the cards won't be able to fit
in the GUI.
 
### Card Keypad
The oh-so-beautiful card keypad allows you to input your cards so you can actually use the calculator (wow!).
In a 5x2 configuration, all you need to do is press the button corresponding to the card(s) you want to
insert into the calculator. __As a reminder__, all Jacks; Queens and Kings are counted as Tens, so the button for 10
includes the letters J Q K so you don't wonder where they went or if I forgot to include them.

### Debugging the Terminal
Nice job, now you know how to use the GUI and what all the sections mean. But you might have noticed
when you start up C21 and every time you press a card button, you get some info in the terminal, this is
all for debug purposes and to show whats going on.
There are 5 different tags you can get along with a message in the terminal:
- Success
- Notice
- Info
- Warning
- Error

Each one has thier own color and are self-explanatory, the only ones to really explain are _notice_ and _info_.
Info is used for when the program returns data sets such as the dictonarys needed for storing the
counts and recommendations. Notice on the other hand is used for showing what functions are being called
and a rudimentary version of the information sidebar.
There is also a rudimentary version of the recommendation system printed out in the terminal. There, the four
method names are printed out and tells you to increase or lower your bets.
```
HILO: - OMEGAII: - KO: - ACEFC:
(Inc = Increase Bet, Neu = Neutral Bet, Neg = Bet Minimum)
```

When you run the program, the first thing it will tell you is if it's running on Windows or another OS, this
is used for activating the color in the terminal so you can see all the beautiful colored tags. It also tells
you if the yaml file for the methods has been loaded successfully and the methods it will use.

### Resetting
If you want to reset the calculator and it's values completly you will have to close the program and run
it again. I have not implemented a reset button as you can run the risk of losing your progress on accident.
Feedback would be appreciated if you would like the inclusion of a reset button.

## A Word About Deck Penetration In Online Casinos
Online casinos usually have low deck penetration, which just means they put in a special card somewhere in the
shoe (all the decks) so they know when to reshuffle. This means you might get very bad cards in the beginning
and it's about to get very good, but the dealer reshuffles before you can get to those high value cards. This
means while counting online, you have to be very patient or just look for a good table with high penetration.

## And finally...
I hope you found this project somewhat interesting, and that you've learned something from it. C21 took
around 2 weeks to complete with delays but turned out pretty good if I do say so myself. I got inspired
to make something like this thanks to the [1988 movie "Rainman"](https://en.wikipedia.org/wiki/Rain_Man), great movie, highly recommend watching it. 

Now I leave you with this information in this README, and the knowledge that you can now beat any online casino
if you use this tool correctly. Best of luck! :)

> __IMPORTANT__: I, `ktehllama`, am not responsible at all for any monetary loss on your part or any other legal issues that may arise
by using an assisted program to count cards, this is for educational purposes only, use at your own volition and risk.

## License
CC0 1.0 Universal
