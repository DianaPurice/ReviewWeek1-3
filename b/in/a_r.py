# Ask user for eye character
print("Please enter a character for the eye:")
ch = input()
print("Beep's expression is now as follows:")
print('''

    """"""""""""""" 
  "                  "
 "      {}       {}     "
"                      "
"                      "
 "                    "
  "                  "
    """"""""""""""""
          """"""
""""""""""""""""""""""""
 "                    "
  "                  "
   "                "
    "              " '''.format(ch, ch))
