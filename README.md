# Gary's Email Generator
## By Nate Browne

### Introduction
Hello! If you're reading this and you're not the author (Nate Browne), then you
somehow got voluntold (or you volunteered) to help Gary send out those
verification emails that make sure everyone is signed up to do what they wanted
to be doing. This program will do just that for you, but it requires a few
things to have been done. I'll outline them file by file so that you know
exactly what needs to be done so that you can just let this program do the
tedious task.

You can run this program by typing `./main.py`. This program contains a debug
mode; to use it, start up the program and add on either `--debug` or `-d`. You
should run it with debug mode before sending the email to Gary to make sure that
everything is good to go. You can end the program at any time by pressing either
`CTRL+C` or `CTRL+D`.

### Setup
Make sure you have `python3` installed. To check if you have it, on Linux/macOS
just type `which python3` into your terminal and it should give you a path to
the executable if it exists (or it will say "python3 not found". If you don't
have python3, figure out how to install it for your system.).
Open up `main.py` and make sure that the shebang at the top of the file matches
the path to your system's installation of `python3`.

Next up, the email stuff. This program will send an email as you to Gary (or
some other recipient that you can specify) so you'll need to get that squared
away. Here's what to do:

1. UCSD uses Gmail to handle their `@ucsd.edu` emails, so you'll need to allow
your UCSD email account to send stuff. Go to [this link](https://stackabuse.com/how-to-send-emails-with-gmail-using-python/),
scroll down to the section "Authenticating with Gmail", and follow those steps.
If you want to run this program and send emails from a different email server,
you'll need to edit the file `mailer.py` to allow you to do so. More on this
later. As an aside, if you use Outlook, you don't (as of the time of writing
this) need to do any authentication. You can just use your email and password as
normal.

If you use Windows, find a Linux/macOS system cause I have no idea how to run
this program on Windows. Sorry dude ¯\\_(ツ)_/¯

*Side note: If anyone using this knows how to run it on Windows, be sure to hit
me up. I'm pretty sure all you need to do is have a working version of Python
and set up the path correctly (or use python3 explicitly) but I'm not sure.*

### The Files

#### The .tsv File
Firstly, Gary should have given you access to a spreadsheet containing the staff
organization for the quarter. If you don't have this, ask him for access.

Once you have access, download it as a `.tsv` file (not a `.csv`). The reason
for this is that the file more than likely has commas *in* the data (for
example, the name of the tutors is probably "surname, first name"), so using
commas to separate the data is pretty useless.

Once you've done that, move that `.tsv` file into this directory where all of
these files are. You can call it whatever you want. Now, open up that file and
delete the lines that have the counts. Those are the last few lines below the
last tutor's name. After that, delete all the lines under the (probably two)
header lines until the first line below those is the first tutor.

#### adder.py
This is a module that contains a bunch of functions that append a new section of
the email to the currently built email. These sections are the parts that
mention how many hours you have, which Piazzas you're going to be in, what
you're grading, etc.

The thing to note here is that you may have to add/remove sections based on
__the courses that Gary is teaching this quarter__. If he's doing 12, 15L, and
110, then the only thing you'd have to do is verify that the spreadsheet (and
consequently, your `.tsv` file) have blank spaces where there is no entry
(instead of like a 'N' or a 0 or something). The script is written assuming that
that is the case, so you'd either have to remove those values from the `.tsv`
or just update each function in this file (I'd personally pick the latter; it'd
be faster). If he's doing other classes, you'll have to edit some of the stuff
in here as well as in `strings.py` (more on that later).

Ultimately, you *probably won't touch this file very much*.

#### extractor.py
This module pulls out the relevant information from a row in the `.tsv` file and
populates a dictionary with it.

You'll probably have to edit this function based on the column numbers, not the
names. What I mean by that is that you'll have to open your file (or open the
spreadsheet cause it'll be easier to read) and re-number the indices of the row
so that they match up with the corresponding label in the dictionary. As an
example, you'd have to make sure that the name of the tutor actually is in
column 3 so that this line `data['name'] = row[3]` still works out. If the name
actually is in column 5 now, you'd just have to change the 3 to a 5 and you're
good. Make sure you do that for every single field so that things line up as
expected, and re-name some of the keys in the dictionary if it makes sense to
(e.g. if Gary isn't teaching 110, you don't need the 110 stuff. Maybe that is
replaced with a different course (like 8A) or maybe it's just gone; either way,
you'd just comment out those lines and you're good.)

#### mailer.py
*You shouldn't need to touch this file*. If something goes wrong here, double
check to see you've authenticated with Gmail properly (refer to the above link).
If you wanted to use a different email client than Gmail, you'll need to open
this file and change the string that says 'smtp.gmail.com' to be the SMTP
protocol for your particular mail server. The file has a dict of the common
ones; if yours is there, then just change the corresponding dictionary key.
Otherwise, add yours in.

#### strings.py
*You shouldn't need to touch this file*. This file contains all of the strings
used throughout the entire program. Some of them you'll never need to touch,
others you may need to change depending on which classes are being taught.

#### creator.py
*You shouldn't need to touch this file*. This file just creates the huge email
string for the tutor and returns it.

#### verifier.py
*You shouldn't need to touch this file*. All it does is validate that the email
you put in is a valid one. If desired, you can modify the set of known domains
(you'll see it) so that it recognizes more of them, but it's probably not
necessary. Besides, I'm pretty sure I've put the major ones you'll be sending an
email to from this script.

#### main.py
*You shouldn't need to touch this file*. This is the file that actually does
stuff (you'll notice that it's the only executable file as well). It's pretty
nicely documented, so if you want to get a good idea of how it works just read
through the docstrings and comments. The program also gives an option to output
to a file instead of sending an email if you'd prefer to do that instead (or if
Gary asks for a file instead of an email).

### Contact
If at any point you don't understand what you're seeing here, email me at
npcompletenate@protonmail.com and I'll do my best to remember what this thing does and
how to use it (lol). If I'm still at UCSD when you're reading this, you probably
have a better way of contacting me other than my email address (so use that instead
please!)


