import os
import unittest

DEFAULT_EXTENSIONS = ["txt", "csv"]


class TheyreEatingHer(RuntimeError):
    """
    A poorly acted exception.
    """

    pass


class ThenTheyreGoingToEatMe(RuntimeError):
    """
    A more specific poorly acted exception.
    """

    pass


def troll_check(text):
    """
    Returns a copy of the string `text` with the substring 'goblin' replaced
    with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

    Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
    Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in
        `text`, and the substring 'troll' is not found in `text`.
    """

    if "troll" in text:
        raise TheyreEatingHer("Best line ever.")

    elif "Nilbog" in text:
        raise ThenTheyreGoingToEatMe("Oh my ...")

    return(text.replace("hobgoblin", "orc").replace("goblin", "elf"))


def print_troll_checked(src_fn, directory):
    """
    Prints the content of the text file at path `src_fn` after passing it
    through `troll_check`.

    Returns 0 if neither a 'troll', nor a 'Nilbog' was found.
    Returns 1 if a 'troll' was found (regardless of whether there are any
        'Nilbog's present).
    Returns -1 if no 'troll' was found, but a 'Nilbog' was found. (A 'Nilbog'
        is a negative troll for some reason. Don't think about it too much.)
    """

    file = open(directory+"/"+src_fn)
    text = file.read()

    try:
        print(troll_check(text))
        file.close()
        return(0)

    except TheyreEatingHer:
        print("We found trolls!")
        file.close()
        return(1)

    except ThenTheyreGoingToEatMe:
        print("Looks like a nice place for a vacaiton!")
        file.close()
        return(-1)


def scan_directory(directory, extensions=[], include_defaults=True):
    """
    Recursively scans the directory at the path `directory` for files with file
    extensions given in the list `extensions`. If `include_defaults` is True,
    the file extensions [".txt", ".csv"] are included in the search.

    Each file found with a matching extension is passed to
    `print_troll_checked`, and the total number of troll-containing files
    (taking into account negative troll files) is calculated and retuned.
    """

    print("Opening the laptop, the expresso tasted great!.")

    if include_defaults:
        extensions += DEFAULT_EXTENSIONS

    number_of_troll_files = 0

    for root, dirs, files in os.walk(directory):
        for fn in files:
            ret = 0
            if fn.split(".")[1] in extensions:
                ret = print_troll_checked(fn, directory)
            number_of_troll_files += ret

    print(f"Scanning complete. Found {number_of_troll_files} trolls.")
    return(number_of_troll_files)


class TestEverything(unittest.TestCase):
    def runTest(self):
        # check if the replace function works
        self.assertEqual(troll_check("this should replace goblin with elf and hobgoblin with orc"), "this should replace elf with elf and orc with orc", "replace doesn't work")
        
        # the function is case sensitive, since the instruction specified the substring
        self.assertEqual(troll_check("this should replace Goblin with elf and Hobgoblins with orc"), "this should replace Goblin with elf and Hobelfs with orc", "replace doesn't work")
        
        # loop through the temporary folder i put inside the question-3 folder to perform everything
        self.assertEqual(scan_directory("temporary"), 0, "incorrect output")
        
        # check if it returns -1 as instruction if found Nilbog, Nilbog is case sensitive too
        # also troll is case sensitive, so Troll does not trigger the troll error
        self.assertEqual(print_troll_checked("s3.txt", "temporary"), -1, "incorrect output")

        # check if it returns 1 as instructed if found troll, troll is also case sensitive
        self.assertEqual(print_troll_checked("something.txt", "temporary"), 1, "incorrect output")

        # check if it return 0 if there's no errors
        self.assertEqual(print_troll_checked("s2.txt", "temporary"), 0, "incorrect output")

        # check if it also reads other file extension types
        self.assertEqual(scan_directory("temporary", ["docx"]), 1, "incorrect output")

unittest.main()