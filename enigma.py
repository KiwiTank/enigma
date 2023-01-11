# plug-lead object to map one letter to another
class PlugLead:
    def __init__(self, mapping):
        if mapping[0] != mapping[1]:
            self.map1 = mapping[0]
            self.map2 = mapping[1]
        else:
            raise ValueError("Cannot connect a letter to itself")

    # return the result of passing a character through the lead
    def encode(self, character):
        if character == self.map1:
            return self.map2
        elif character == self.map2:
            return self.map1
        else:
            return character

# plugboard object for containing all the connected plug-lead classes, and passing encoding characters
class Plugboard:
    def __init__(self):
        self.leads = {}

    # add a lead connecting two characters to the plugboard
    def add(self, cable):
        if cable.map1 not in self.leads.keys() or cable.map2 not in self.leads.keys() and len(self.leads.keys()) < 20:
            self.leads[cable.map1] = cable
            self.leads[cable.map2] = cable
        elif len(self.leads.keys()) == 20:
            raise ValueError("There are already 10 leads connected to the plugboard")
        else:
            raise ValueError("Cannot connect a lead to a letter that is already in use")

    # pass a letter through the plugboard and return encoded result
    def encode(self, char):
        if char in self.leads.keys():
            out = self.leads.get(char)
            return out.encode(char)
        else:
            return char

    # returns list of letters not currently connected to a lead
    def list_avail_letters(self):
        unplugged = []
        for letter in list(map(chr, range(ord('A'), ord('Z') + 1))):
            if letter not in self.leads.keys():
                unplugged.append(letter)
            else:
                pass
        print("These letters are currently unplugged: " + str(unplugged))

    # remove a PlugLead object from the plugboard
    def unplug_lead(self, cable):
        v1 = cable.map1
        v2 = cable.map2
        if v1 in self.leads.keys() and v2 in self.leads.keys():
            if self.leads.get(v1) == self.leads.get(v2):
                del self.leads[v1]
                del self.leads[v2]
            else:
                raise ValueError("These letters are not connected to the same lead")
        else:
            raise ValueError("This plug is not connected")

    # remove all leads from the plugboard
    def clear_board(self):
        self.leads = {}


# holds all rotor combinations from which to create rotor objects
class Rotorbox:
    def __init__(self):
        # combinations for all possible rotors held in the rotor box
        self.rotors = {
            'Beta': {'A': 'L', 'B': 'E', 'C': 'Y', 'D': 'J', 'E': 'V', 'F': 'C', 'G': 'N', 'H': 'I', 'I': 'X',
                     'J': 'W', 'K': 'P', 'L': 'B', 'M': 'Q', 'N': 'M', 'O': 'D', 'P': 'R', 'Q': 'T', 'R': 'A',
                     'S': 'K', 'T': 'Z', 'U': 'G', 'V': 'F', 'W': 'U', 'X': 'H', 'Y': 'O', 'Z': 'S'},
            'Gamma': {'A': 'F', 'B': 'S', 'C': 'O', 'D': 'K', 'E': 'A', 'F': 'N', 'G': 'U', 'H': 'E', 'I': 'R',
                      'J': 'H', 'K': 'M', 'L': 'B', 'M': 'T', 'N': 'I', 'O': 'Y', 'P': 'C', 'Q': 'W', 'R': 'L',
                      'S': 'Q', 'T': 'P', 'U': 'Z', 'V': 'X', 'W': 'V', 'X': 'G', 'Y': 'J', 'Z': 'D'},
            'I': {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V',
                  'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U',
                  'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'},
            'II': {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X',
                   'J': 'B', 'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C', 'Q': 'Q', 'R': 'G',
                   'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V', 'Y': 'O', 'Z': 'E'},
            'III': {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H', 'E': 'J', 'F': 'L', 'G': 'C', 'H': 'P', 'I': 'R',
                    'J': 'T', 'K': 'X', 'L': 'V', 'M': 'Z', 'N': 'N', 'O': 'Y', 'P': 'E', 'Q': 'I', 'R': 'W',
                    'S': 'G', 'T': 'A', 'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S', 'Y': 'Q', 'Z': 'O'},
            'IV': {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P', 'F': 'Z', 'G': 'J', 'H': 'A', 'I': 'Y',
                   'J': 'Q', 'K': 'U', 'L': 'I', 'M': 'R', 'N': 'H', 'O': 'X', 'P': 'L', 'Q': 'N', 'R': 'F',
                   'S': 'T', 'T': 'G', 'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M', 'Y': 'W', 'Z': 'B'},
            'V': {'A': 'V', 'B': 'Z', 'C': 'B', 'D': 'R', 'E': 'G', 'F': 'I', 'G': 'T', 'H': 'Y', 'I': 'U',
                  'J': 'P', 'K': 'S', 'L': 'D', 'M': 'N', 'N': 'H', 'O': 'L', 'P': 'X', 'Q': 'A', 'R': 'W',
                  'S': 'M', 'T': 'J', 'U': 'Q', 'V': 'O', 'W': 'F', 'X': 'E', 'Y': 'C', 'Z': 'K'}
        }

        self.available = ['Beta', 'Gamma', 'I', 'II', 'III', 'IV', 'V']

        self.reflectors = {
            'A': {'A': 'E', 'B': 'J', 'C': 'M', 'D': 'Z', 'E': 'A', 'F': 'L', 'G': 'Y', 'H': 'X', 'I': 'V',
                  'J': 'B', 'K': 'W', 'L': 'F', 'M': 'C', 'N': 'R', 'O': 'Q', 'P': 'U', 'Q': 'O', 'R': 'N',
                  'S': 'T', 'T': 'S', 'U': 'P', 'V': 'I', 'W': 'K', 'X': 'H', 'Y': 'G', 'Z': 'D'},
            'B': {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P',
                  'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B',
                  'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'},
            'C': {'A': 'F', 'B': 'V', 'C': 'P', 'D': 'J', 'E': 'I', 'F': 'A', 'G': 'O', 'H': 'Y', 'I': 'E',
                  'J': 'D', 'K': 'R', 'L': 'Z', 'M': 'X', 'N': 'W', 'O': 'G', 'P': 'C', 'Q': 'T', 'R': 'K',
                  'S': 'U', 'T': 'Q', 'U': 'S', 'V': 'B', 'W': 'N', 'X': 'M', 'Y': 'H', 'Z': 'L'}
        }

        self.available_ref = ['A', 'B', 'C']

    # return all the currently used rotors and reflectors to the rotor box
    def return_all_rotors(self):
        self.available = ['Beta', 'Gamma', 'I', 'II', 'III', 'IV', 'V']
        self.available_ref = ['A', 'B', 'C']


# class to create the rotor object, which is a child of the Rotorbox class
class Rotor(Rotorbox):
    def __init__(self, label):
        super().__init__()
        # if the requested rotor is in the rotor box then create a new object of this type. else raise a value error
        if label in self.available:
            self.rotor = self.rotors.get(label).copy()
            self.available.remove(label)
        else:
            raise ValueError(f"That rotor is not in the rotor box.\nThe available rotors are {self.available}")
        self.name = label
        self.rotation = 0
        # if else statements to determine the type of rotor and then set its notch location (0-25) if it has one
        if label == 'I':
            self.notch = 16
        elif label == 'II':
            self.notch = 4
        elif label == 'III':
            self.notch = 21
        elif label == 'IV':
            self.notch = 9
        elif label == 'V':
            self.notch = 25
        else:
            self.notch = None

    # return the rotor to the rotor box so that it is available again
    def return_rotor(self, label):
        if label not in self.available:
            self.label.append(label)
        else:
            raise ValueError("That rotor is already in the rotor box")

    # sets the rotation to the defined ring setting for the rotor
    def set_rotation(self, setting):
        self.rotation = setting

    # rotate the rotor one notch up
    def rotate(self):
        if self.rotation < 25:
            self.rotation += 1
        elif self.rotation == 25:
            self.rotation = 0

    # return the current rotation of the rotor
    def current_rotation(self):
        return self.rotation

    # reset rotor rotation to default setting
    def reset_rotor(self):
        self.rotation = 0

    # return the rotor label/type
    def rotor_label(self):
        return self.name

    # return the notch for this rotor
    def get_notch(self):
        return self.notch

    # encode the supplied character from right to left
    def encode_right_to_left(self, character):
        if ord(character) + self.rotation <= ord('Z'):
            return self.rotor.get(chr(ord(character) + self.rotation))
        else:
            return self.rotor.get(chr(ord(character) + self.rotation - 26))

    # encode the supplied character from left to right
    def encode_left_to_right(self, character):
        vals = self.rotor.values()
        return_vals = self.rotor.keys()
        vals_list = list(vals)
        return_vals_list = list(return_vals)
        if ord(character) + self.rotation <= ord('Z'):
            val_index = vals_list.index(chr(ord(character) + self.rotation))
        else:
            val_index = vals_list.index(chr(ord(character) + self.rotation - 26))
        if val_index + self.rotation <= len(vals_list) - 1:
            return_vals_letter = return_vals_list[val_index]
            return return_vals_letter
        else:
            return_vals_letter = return_vals_list[val_index - 26]
            return return_vals_letter

    # list the labels for each rotor
    def list_avail_rotors(self):
        return self.available


# create the reflector object, which is a child of the rotorbox class
class Reflector(Rotorbox):
    def __init__(self, label):
        super().__init__()
        # connect the object to a copy of the correct dictionary, and remove the reflector from the rotorbox
        if label in self.available_ref:
            self.reflector = self.reflectors.get(label).copy()
            self.available_ref.remove(label)
        else:
            raise ValueError(
                f"That reflector is not in the rotor box.\nThe available reflectors are {self.available_ref}")
        self.name_ref = label

    # return the reflector label/type
    def rotor_label(self):
        return self.name_ref

    # encode the supplied character from right to left
    def encode(self, character):
        return self.reflector.get(character)

    # list the available reflectors
    def list_avail_reflectors(self):
        return self.available_ref


# function to offset letters for use in multiple rotor encoding in Machine class, dependent on relative rotor rotations
def letter_offset(character, offset, add=False, sub=False):
    if add:
        if ord('Z') >= ord(character) + offset >= ord('A'):
            return chr(ord(character) + offset)
        elif ord(character) + offset < ord('A'):
            return chr(ord(character) + offset + 26)
        else:
            return chr(ord(character) + offset - 26)
    elif sub:
        if ord('Z') >= ord(character) - offset >= ord('A'):
            return chr(ord(character) - offset)
        elif ord(character) - offset < ord('A'):
            return chr(ord(character) - offset + 26)
        else:
            return chr(ord(character) - offset - 26)
    else:
        raise ValueError('one of the arguments \'add\' or \'sub\' must be set to True')


# create the machine object, where all the other objects are brought together and used to encode strings
class Machine:
    # below are all the initial settings (*_rotor = rotors, ref = reflector, four = optional fourth rotor, *_ring is
    # the ring setting for each rotor)
    def __init__(self, left, middle, right, reflector, plugboard, fourth=None):
        self.r_rotor = right
        self.m_rotor = middle
        self.l_rotor = left
        self.ref = reflector
        self.four = fourth
        self.r_ring = 0
        self.m_ring = 0
        self.l_ring = 0
        self.four_ring = 0
        self.plugboard = plugboard

    # set initial rotor positions, with the option of a fourth rotor. Additional statements added to allow for the
    # ring settings to be called first
    def initial_position(self, left, middle, right, fourth=None):
        if self.r_rotor.current_rotation() == 0:
            self.r_rotor.set_rotation(ord(right) - 65)
        else:
            if ord(right) - 65 - self.r_rotor.current_rotation() < 0:
                if (ord(right) - 65 - self.r_rotor.current_rotation() + 26) < 26:
                    self.r_rotor.set_rotation(ord(right) - 65 - self.r_rotor.current_rotation() + 26)
                else:
                    self.r_rotor.set_rotation(0)
            else:
                self.r_rotor.set_rotation(ord(right) - 65 - self.r_rotor.current_rotation())

        if self.m_rotor.current_rotation() == 0:
            self.m_rotor.set_rotation(ord(middle) - 65)
        else:
            if ord(middle) - 65 - self.m_rotor.current_rotation() < 0:
                if (ord(middle) - 65 - m_rotor.current_rotation() + 26) < 26:
                    self.m_rotor.set_rotation(ord(middle) - 65 - m_rotor.current_rotation() + 26)
                else:
                    self.m_rotor.set_rotation(0)
            else:
                self.m_rotor.set_rotation(ord(middle) - 65 - m_rotor.current_rotation())

        if self.l_rotor.current_rotation() == 0:
            self.l_rotor.set_rotation(ord(left) - 65)
        else:
            if ord(left) - 65 - self.l_rotor.current_rotation() < 0:
                if (ord(left) - 65 - self.l_rotor.current_rotation() + 26) < 26:
                    self.l_rotor.set_rotation(ord(left) - 65 - self.l_rotor.current_rotation() + 26)
                else:
                    self.l_rotor.set_rotation(0)
            else:
                self.l_rotor.set_rotation(ord(left) - 65 - self.l_rotor.current_rotation())

        if fourth is not None:
            if self.four.current_rotation() == 0:
                self.four.set_rotation(ord(fourth) - 65)
            else:
                if ord(fourth) - 65 - self.four.current_rotation() < 0:
                    if (ord(fourth) - 65 - self.four.current_rotation() + 26) < 26:
                        self.four.set_rotation(ord(fourth) - 65 - self.four.current_rotation() + 26)
                    else:
                        self.four.set_rotation(0)
                else:
                    self.four.set_rotation(ord(fourth) - 65 - self.four.current_rotation())

    # set initial ring settings. If else statements allow for either ring settings or initial positions to be called
    # first. Option to set ring settings for a fourth rotor
    def ring_settings(self, left, middle, right, fourth=None):
        self.r_ring = right - 1
        self.m_ring = middle - 1
        if self.r_rotor.current_rotation() == 0 and right == 1:
            pass
        elif self.r_rotor.current_rotation() == 0 and right != 1:
            self.r_rotor.set_rotation(26 - (right - 1))
        else:
            if self.r_rotor.current_rotation() - (right - 1) >= 0:
                self.r_rotor.set_rotation(self.r_rotor.current_rotation() - (right - 1))
            else:
                self.r_rotor.set_rotation(self.r_rotor.current_rotation() - (right - 1) + 26)

        if self.m_rotor.current_rotation() == 0 and middle == 1:
            pass
        elif self.m_rotor.current_rotation() == 0 and middle != 1:
            self.m_rotor.set_rotation(26 - (middle - 1))
        else:
            if self.m_rotor.current_rotation() - (middle - 1) >= 0:
                self.m_rotor.set_rotation(self.m_rotor.current_rotation() - (middle - 1))
            else:
                self.m_rotor.set_rotation(self.m_rotor.current_rotation() - (middle - 1) + 26)

        if self.l_rotor.current_rotation() == 0 and left == 1:
            pass
        elif self.l_rotor.current_rotation() == 0 and left != 1:
            self.l_rotor.set_rotation(26 - (left - 1))
        else:
            if self.l_rotor.current_rotation() - (left - 1) >= 0:
                self.l_rotor.set_rotation(self.l_rotor.current_rotation() - (left - 1))
            else:
                self.l_rotor.set_rotation(self.l_rotor.current_rotation() - (left - 1) + 26)

        if fourth is not None:
            if self.four.current_rotation() == 0 and fourth == 1:
                pass
            elif self.four.current_rotation() == 0 and fourth != 1:
                self.four.set_rotation(26 - (fourth - 1))
            else:
                if self.four.current_rotation() - (fourth - 1) >= 0:
                    self.four.set_rotation(self.four.current_rotation() - (fourth - 1))
                else:
                    self.four.set_rotation(self.four.current_rotation() - (fourth - 1) + 26)

    # returns the current rotor positions for all rotors currently in the machine
    def rotor_positions(self, four=False):
        if four:
            print(self.four.current_rotation(), self.l_rotor.current_rotation(), self.m_rotor.current_rotation(),
                  self.r_rotor.current_rotation())
        else:
            print(self.l_rotor.current_rotation(), self.m_rotor.current_rotation(), self.r_rotor.current_rotation())

    # pass the string through all installed leads, rotors, and reflectors. Rotation of rotors occurs first,
    # depending on notch location relative to rotor type
    def encode(self, string):
        out = ''
        # middle rotation is tracked to ensure that it is not rotated twice on any one character
        middle_rotation = False
        for character in string:
            self.r_rotor.rotate()
            # if before r_rotor rotation the rotor was on its notch, then rotate m_rotor. Ring setting is added back
            # to the current rotation to remove it from turnover calculations
            if self.r_rotor.get_notch() is not None:
                if self.r_rotor.get_notch() == 25:
                    if self.r_rotor.current_rotation() + self.r_ring > 25:
                        if (self.r_rotor.current_rotation() + self.r_ring - 25) == 1:
                            self.m_rotor.rotate()
                            middle_rotation = True
                    else:
                        if (self.r_rotor.current_rotation() + self.r_ring) == 1:
                            self.m_rotor.rotate()
                            middle_rotation = True
                else:
                    if self.r_rotor.current_rotation() + self.r_ring > 25:
                        if (self.r_rotor.current_rotation() + self.r_ring - 26) == (self.r_rotor.get_notch() + 1):
                            self.m_rotor.rotate()
                            middle_rotation = True
                    else:
                        if (self.r_rotor.current_rotation() + self.r_ring) == (self.r_rotor.get_notch() + 1):
                            self.m_rotor.rotate()
                            middle_rotation = True
            # rotate middle rotor if it is sitting on its notch and has not just been rotated
            if self.m_rotor.get_notch() is not None and middle_rotation is False:
                if (self.m_rotor.current_rotation() + self.m_ring) > 25:
                    if (self.m_rotor.current_rotation() + self.m_ring) == (self.m_rotor.get_notch()):
                        self.m_rotor.rotate()
                        middle_rotation = True
                else:
                    if (self.m_rotor.current_rotation() + self.m_ring) == (self.m_rotor.get_notch()):
                        self.m_rotor.rotate()
                        middle_rotation = True
            # if before m_rotor rotation the rotor was on its notch, then rotate l_rotor, otherwise rotate left rotor
            # if the middle rotor was on its notch before rotation
            if self.m_rotor.get_notch() is not None and middle_rotation is True:
                if (self.m_rotor.current_rotation() + self.m_ring) > 25:
                    if (self.m_rotor.current_rotation() + self.m_ring - 25) == (self.m_rotor.get_notch() + 1):
                        self.l_rotor.rotate()
                else:
                    if (self.m_rotor.current_rotation() + self.m_ring) == (self.m_rotor.get_notch() + 1):
                        self.l_rotor.rotate()
            if self.m_rotor.get_notch() is not None and middle_rotation is False:
                if (self.m_rotor.current_rotation() + self.m_ring) > 25:
                    if (self.m_rotor.current_rotation() + self.m_ring - 25) == (self.m_rotor.get_notch()):
                        self.l_rotor.rotate()
                else:
                    if (self.m_rotor.current_rotation() + self.m_ring) == (self.m_rotor.get_notch()):
                        self.l_rotor.rotate()
            middle_rotation = False
            # pass the character through the plugboard and the first three rotors
            pass1 = self.plugboard.encode(character)
            pass2 = letter_offset(self.r_rotor.encode_right_to_left(pass1), self.r_rotor.current_rotation(), sub=True)
            pass3 = letter_offset(self.m_rotor.encode_right_to_left(pass2), self.m_rotor.current_rotation(), sub=True)
            pass4 = letter_offset(self.l_rotor.encode_right_to_left(pass3), self.l_rotor.current_rotation(), sub=True)
            # if a fourth rotor is connected, decode through the fourth rotor to the reflector and back again
            if self.four is not None:
                pass5 = letter_offset(self.four.encode_right_to_left(pass4), self.four.current_rotation(), sub=True)
                pass6 = self.ref.encode(pass5)
                pass7 = letter_offset(self.four.encode_left_to_right(pass6), self.four.current_rotation(), sub=True)
                pass8 = letter_offset(self.l_rotor.encode_left_to_right(pass7), self.l_rotor.current_rotation(),
                                      sub=True)
                pass9 = letter_offset(self.m_rotor.encode_left_to_right(pass8), self.m_rotor.current_rotation(),
                                      sub=True)
                pass10 = letter_offset(self.r_rotor.encode_left_to_right(pass9), self.r_rotor.current_rotation(),
                                       sub=True)
                out = out[:] + self.plugboard.encode(pass10)
            # if there is no fourth rotor, then pass to the reflector and back through the three rotors in reverse
            # and to the plugboard
            else:
                pass5 = self.ref.encode(pass4)
                pass6 = letter_offset(self.l_rotor.encode_left_to_right(pass5), self.l_rotor.current_rotation(),
                                      sub=True)
                pass7 = letter_offset(self.m_rotor.encode_left_to_right(pass6), self.m_rotor.current_rotation(),
                                      sub=True)
                pass8 = letter_offset(self.r_rotor.encode_left_to_right(pass7), self.r_rotor.current_rotation(),
                                      sub=True)
                out = out[:] + self.plugboard.encode(pass8)
        return out

# uncomment below to run the example settings and enigma decrytion
if __name__ == "__main__":    
    #rotor = Rotor('I')
    #rotorII = Rotor('II')
    #rotorIII = Rotor('III')
    #rotorIV = Rotor('IV')
    #rotorV = Rotor('V')
    #rotorGamma = Rotor('Gamma')
    #rotorBeta = Rotor('Beta')
    #refA = Reflector('A')
    #refB = Reflector('B')
    #refC = Reflector('C')

    #plug.clear_board()
    #plug.add(PlugLead("PC"))
    #plug.add(PlugLead("XZ"))
    #plug.add(PlugLead("FM"))
    #plug.add(PlugLead("QA"))
    #plug.add(PlugLead("ST"))
    #plug.add(PlugLead("NB"))
    #plug.add(PlugLead("HY"))
    #plug.add(PlugLead("OR"))
    #plug.add(PlugLead("EV"))
    #plug.add(PlugLead("IU"))

    #cipher = Machine(rotorV, rotorBeta, rotor, refA, plug, fourth=rotorIV)
    #cipher.initial_position('Z', 'G', 'P', fourth='E')
    #cipher.ring_settings(24, 3, 5, fourth=18)

    #print('Example 2 decryption = ' + str(cipher.encode('BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI')))
