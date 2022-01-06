
import string

punctuation = {' ':'space',
               '.':'period',
               ',':'comma',
               ':':'colon',
               ';':'semicolon',
               '"':'quotedbl',
               '\'':'apostrophe',
               '(':'parenleft',
               ')':'parenright',
               '[':'bracketleft',
               ']':'bracketright',
               '{':'braceleft',
               '}':'braceright',
               '+':'plus',
               '-':'minus',
               '_':'underscore',
               '#':'numbersign',
               '$':'dollar',
               '*':'asterix',
               '~':'asciitilde',
               '/':'slash',
               '\\':'backslash',
               '!':'exclam',
               '?':'question',
               '%':'percent',
               '<':'less',
               '>':'greater',
               '=':'equal',
               }

filename = input("file:   ")
with open(filename) as f:
    content = f.read().split('\n')

script = 'sleep 2\n'
for line in content:
    script += 'xdotool key'
    for char in line:
        if char in string.ascii_letters or char in string.digits:
            script += f' {char}'
        elif char in punctuation:
            script += f' {punctuation[char]}'
    script += '\nxdotool key Return\n'

with open(filename.split('.')[0] + '_converted.sh', 'w+') as f:
    f.write(script)
