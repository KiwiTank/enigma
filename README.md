# enigma project
This is a project I did for my MSc in AI to create a working emulator of the German Enigma coding machine from WWII. Once the machine is created, it then needs to successfully decode some text, including text encoded using missing or altered plug and rotor settings for which the system can determine the missing settings and apply them to the decription.

## code
This project consists of two python files. Enigma.py contains all the classes and functions for the machine itself, which can take plug and rotor settings and return decryted text that was encryted using those settings. 
The second file, decryption.py runs a number of functions to determine missing or altered rotor and plug settings and then decrypt the given text. 

### enigma.py
This file contains classes that mimic the function of the various components of the German enigma machine. The basic idea is that the machine could be used to encrypt a message, letter by letter, using a specific setting. In order to read that message the receiving party also needed to have an enigma machine set to the exact same settings, and by inputing each letter of the encrypted message the original plain text message could be found. 
The three main components in the encryption process involved a number of rotors, each of which was wired to convert a recieved letter into another fixed letter. All rotors lined up to create a chain of letter changes, leading to a massively large number of potential combinations. This was furthered by the reflector, sited at the end of the rotor chain, which changed the letter again and passed it back through the string of rotors. To complicate things further, the rotors would rotate at set points or by their relationship to an adjacent rotor, changing the letter combinations that the rotor passed through. Lastly, the plugboard contained a number of potential connections between any two letters which again altered the passed letter at both the beginning and end of the encyrption process. This ultimately leads to a staggering 158 quintillion possible combinations! 
For more information on how this machine worked, click [here](https://en.wikipedia.org/wiki/Enigma_machine). 

To emulate this complext process, each of these features was coded as a class, with the features and function of that class contained within each object. For example, the rotor object contains the ability to define its historical wiring settings from a set dictionary, set its intitial rotation setting, and encode letters based on that setting, while also altering its own and its neighbours rotation based on the location of the notches found on specific rotors. 
Each of these objects are passed into the machine class, whichin which the encrytion and decrytion take place by combining the plugboard and plug settings, rotors, and initial settings. 

Examples are included at the end of the script (commented out) which will set up a specific setting and then decrypt the example message.

### decryption.py
The prime function in this script is *decode*, into which can be passed all the known settings alongside the encrypted message, and it will run a number of checks to determine missing or altered settings or objects before returning the decrypted message. For example, code 2 (commented out at the end) was missing the three initial letter settings for each of the three rotors. The function will run through all possible rotor combinations to determine which ones return a message which corresponds to a given clue.
The five code examples at the end become more complicated, with the last containing a hypothetically altered rotor which contains unknown wiring. The code uses brute force to determine the new rotor dictionary.

# lesson learned
This was a very enjoyable project that fits well with my strong interest in history. The object oriented programming methodology lends itself really well to this type of system. While translating some of the very complex operations of the real machine, particularly the number of edge cases and exceptions that exist within it, I was able to successfully decrypt all the messages and recieved a Disctinction grade as a result. 
