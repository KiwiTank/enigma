from itertools import combinations

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
        return unplugged

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


class Rotor(Rotorbox):
    def __init__(self, label):
        super().__init__()
        # if the requested rotor is in the rotor box then create a new object of this type
        if label in self.available:
            self.rotor = self.rotors.get(label).copy()
            self.available.remove(label)
        else:
            raise ValueError(f"That rotor is not in the rotor box.\nThe available rotors are {self.available}")
        self.name = label
        self.rotation = 0
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
        print(self.available)


class Reflector(Rotorbox):
    def __init__(self, label):
        super().__init__()
        if label in self.available_ref:
            self.reflector = self.reflectors.get(label).copy()
            self.available_ref.remove(label)
        else:
            raise ValueError(
                f"That reflector is not in the rotor box.\nThe available reflectors are {self.available_ref}")
        self.name_ref = label

    # return the reflector label/type
    def rotor_label(self):
        print(self.name_ref)

    # encode the supplied character from right to left
    def encode(self, character):
        return self.reflector.get(character)

    # list the available reflectors
    def list_avail_reflectors(self):
        print(self.available_ref)

    def access_dict(self):
        return self.reflector.copy()

    def set_source_dict(self, temp_dict):
        self.reflector = temp_dict


# function to offset letters for use in multiple rotor encoding, dependent on relative rotor rotations
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


class Machine:
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

    # returns the current rotor positions
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

# function to swap strings between two lists based on location within the list
def swap(input_list, index1, index2, index3):
    input_list[index1][index3], input_list[index2][index3] = input_list[index2][index3], input_list[index1][index3]

    return input_list

# function to find missing settings based on what is supplied to the function,
# and then return the original and corrected settings along with the decrypted result
def decode(l_rotor, m_rotor, r_rotor, ref, l_ring, m_ring, r_ring, l_init, m_init, r_init, code, crib, *leads):
    plugboard = Plugboard()
    if l_rotor is not None:
        left = Rotor(l_rotor)
    if m_rotor is not None:
        middle = Rotor(m_rotor)
    if r_rotor is not None:
        right = Rotor(r_rotor)
    if ref is not None and len(ref) == 1:
        reflector = Reflector(ref)
    if l_ring is not None:
        left_ring = l_ring
    if m_ring is not None:
        middle_ring = m_ring
    if r_ring is not None:
        right_ring = r_ring
    if l_init is not None:
        left_pos = l_init
    if m_init is not None:
        middle_pos = m_init
    if r_init is not None:
        right_pos = r_init
    # add leads to the plugboard if a pair contains only letters
    for i in range(0, len(leads)):
        if leads[i].isalpha():
            plugboard.add(PlugLead(leads[i]))

    # setting variables and lists used in the checks below
    refs = ['A', 'B', 'C']
    rotors = ['2', '4', 'B', 'G']
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    ring_pos = list(range(2, 9, 2)) + list(range(20, 27, 2))
    decrypts = []
    social_media = ['TWITTER', 'FACEBOOK', 'INSTAGRAM', 'TIKTOK', 'YOUTUBE', 'WHATSAPP', 'SNAPCHAT', 'REDDIT',
                    'PINTEREST', 'LINKEDIN']
    out = []
    code4 = []

    # Check for potential alterations to the reflector wires, if the passed reflector argument is a string longer than 1
    if ref is not None:
        if len(ref) > 1:
            for item in refs:
                if item == 'A':
                    print(f'Checking possible alterations to reflector {item}. Please wait...')
                elif item == 'B':
                    print(f'Now checking possible alterations to reflector {item}. Still waiting...')
                else:
                    print(
                        f'Finding possible alterations to reflector {item}. Nearly there...')
                reflect = Reflector(item)
                temp_reflect = Reflector(item)
                pairs_items = reflect.access_dict().items()
                check_items = temp_reflect.access_dict().items()
                pairs_list = []
                exclusion_list = []
                for key, val in pairs_items:
                    pairs_list.append([key, val])
                check_list = []
                for key, val in check_items:
                    check_list.append([key, val])
                # create a list of all possible letter pair combinations to loop through
                for pairs in combinations(check_list, 2):
                    if pairs[0][0] != pairs[1][1]:
                        # create list of pairs in the outermost loop so exclude from inner loops to speed up process
                        if pairs[0] not in exclusion_list:
                            exclusion_list.append(pairs[0])
                        location_0 = check_list.index(pairs[0])
                        location_1 = check_list.index(pairs[1])
                        location_0_opp = check_list.index([pairs[0][1], pairs[0][0]])
                        location_1_opp = check_list.index([pairs[1][1], pairs[1][0]])
                        location_check = [location_0, location_1, location_0_opp, location_1_opp]
                        # loop to swap pairs of letters using indexing against the unaltered checklist
                        for i in range(0, 2):
                            swap(pairs_list, location_0, location_1, i)
                            if i == 0:
                                swap(pairs_list, location_0_opp, location_1_opp, i + 1)
                            else:
                                swap(pairs_list, location_0_opp, location_1_opp, i - 1)
                            # create a second list of pair combinations for the nested loop, but ensure that pairs
                            # already covered by the first loop are not repeated
                            for pairs_2 in combinations(check_list, 2):
                                if pairs_2[0][0] != pairs_2[1][1]:
                                    if check_list.index(pairs_2[0]) not in location_check and check_list.index(
                                            pairs_2[1]) not in location_check and check_list.index(
                                        [pairs_2[0][1], pairs_2[0][0]]) not in location_check and check_list.index(
                                        [pairs_2[1][1], pairs_2[1][0]]) not in location_check and (pairs_2[0]
                                        not in exclusion_list and pairs_2[1] not in exclusion_list):
                                        for j in range(0, 2):
                                            location_2 = check_list.index(pairs_2[0])
                                            location_3 = check_list.index(pairs_2[1])
                                            location_2_opp = check_list.index([pairs_2[0][1], pairs_2[0][0]])
                                            location_3_opp = check_list.index([pairs_2[1][1], pairs_2[1][0]])
                                            swap(pairs_list, location_2, location_3, j)
                                            if j == 0:
                                                swap(pairs_list, location_2_opp, location_3_opp, j + 1)
                                            else:
                                                swap(pairs_list, location_2_opp, location_3_opp, j - 1)
                                            left.reset_rotor()
                                            middle.reset_rotor()
                                            right.reset_rotor()
                                            #creates a temporary dictionary for the reflector object on the next line
                                            temp_dict = {ins[0]: ins[1] for ins in pairs_list}
                                            reflect.set_source_dict(temp_dict)
                                            # decipher the code using this altered reflector and store the result
                                            cipher = Machine(left, middle, right, reflect, plugboard)
                                            cipher.initial_position(left_pos, middle_pos, right_pos)
                                            cipher.ring_settings(left_ring, middle_ring, right_ring)
                                            decrypts.append((cipher.encode(code), f'Original reflector = {item},'
                                                                                  f' original wire connections {pairs[0], pairs[1], pairs_2[0], pairs_2[1]} were changed to {pairs_list[location_0], pairs_list[location_1], pairs_list[location_2], pairs_list[location_3]}'))
                                            swap(pairs_list, location_2, location_3, j)
                                            if j == 0:
                                                swap(pairs_list, location_2_opp, location_3_opp, j + 1)
                                            else:
                                                swap(pairs_list, location_2_opp, location_3_opp, j - 1)
                                    else:
                                        pass
                                else:
                                    pass
                            swap(pairs_list, location_0, location_1, i)
                            if i == 0:
                                swap(pairs_list, location_0_opp, location_1_opp, i + 1)
                            else:
                                swap(pairs_list, location_0_opp, location_1_opp, i - 1)
                            location_check = []
                    else:
                        pass

    # check if any of the plugboard leads contain non-letter strings, and if so only connect those with letter pairs
    if not all(pair.isalpha() for pair in leads):
        correct_plug = []
        for i in range(0, len(leads)):
            if not leads[i].isalpha():
                correct_plug.append(leads[i][0])
            else:
                pass
        plug_combos = []
        # create a list of all letters not connected to iterate through
        for plug in correct_plug:
            for letter in plugboard.list_avail_letters():
                if plug != letter:
                    plug_combos.append(plug + letter)
        pair_leads = []
        # loop to create all possible letter combinations for the missing lead end
        for x in plug_combos:
            for y in plug_combos:
                if x != y and x[0] != y[0] and x[1] != y[1] and x[0] != y[1] and x[1] != y[0]:
                    pair_leads.append((x, y))
        for x in pair_leads:
            for y in pair_leads:
                if x[0] == y[1] and x[1] == y[0]:
                    pair_leads.remove(y)
        print('Running through possible lead connections. Please wait...')
        for combo in pair_leads:
            plugboard.add(PlugLead(combo[0]))
            plugboard.add(PlugLead(combo[1]))
            cipher = Machine(left, middle, right, reflector, plugboard)
            left.reset_rotor()
            middle.reset_rotor()
            right.reset_rotor()
            cipher.initial_position(left_pos, middle_pos, right_pos)
            cipher.ring_settings(left_ring, middle_ring, right_ring)
            decrypts.append((cipher.encode(code), 'Correct leads = ' + str(combo)))
            plugboard.unplug_lead(PlugLead(combo[0]))
            plugboard.unplug_lead(PlugLead(combo[1]))

    # if the reflector is unknown, cipher all possible reflector combinations and find the result containing the crib
    # as well as the correct setting
    if ref is None and l_rotor is not None:
        print('Running through possible reflector options. Please wait...')
        for missing in refs:
            cipher = Machine(left, middle, right, Reflector(missing), plugboard)
            left.reset_rotor()
            middle.reset_rotor()
            right.reset_rotor()
            cipher.initial_position(left_pos, middle_pos, right_pos)
            cipher.ring_settings(left_ring, middle_ring, right_ring)
            decrypts.append((cipher.encode(code), 'Correct reflector = ' + str(missing)))

    # if the initial setting are missing, creates a list of letter combinations and runs through each of them
    if l_init is None or m_init is None or r_init is None:
        combos = list(list(x + y + z) for x in letters for y in letters for z in letters)
        print('Running through possible initial positions. Please wait...')
        for combs in combos:
            cipher = Machine(left, middle, right, reflector, plugboard)
            left.reset_rotor()
            middle.reset_rotor()
            right.reset_rotor()
            cipher.initial_position(combs[0], combs[1], combs[2])
            cipher.ring_settings(left_ring, middle_ring, right_ring)
            decrypts.append((cipher.encode(code), 'Correct initial positions = ' + str(combs)))

    # if the rotors and their ring settings are missing, a list of possible rotor combinations (without those not
    # expected in result) is created and then looped through
    if (l_rotor is None or m_rotor is None or r_rotor is None) and (l_ring is None or m_ring is None or r_ring
                                                                    is None) and ref is None:
        rotor_combos = list(list(x + y + z) for x in rotors for y in rotors for z in rotors)
        rotor_names = {'II': '2', 'IV': '4', 'Beta': 'B', 'Gamma': 'G'}
        for key in rotor_names:
            value = rotor_names[key]
            for i in range(len(rotor_combos)):
                for j in range(0, 3):
                    if rotor_combos[i][j] == value:
                        rotor_combos[i][j] = key
                    else:
                        pass
        # list of ring combinations from ring_pos variable created, removing all odd numbers.
        rings = list((x, y, z) for x in ring_pos for y in ring_pos for z in ring_pos)
        print('Running through possible rotor, reflector, and ring combinations. Please wait...')
        # loops through all possible rotor and ring setting options and decrypts for each
        for rot in rotor_combos:
            for ring in rings:
                for missing in refs:
                    cipher = Machine(Rotor(rot[0]), Rotor(rot[1]), Rotor(rot[2]), Reflector(missing), plugboard)
                    cipher.initial_position(left_pos, middle_pos, right_pos)
                    cipher.ring_settings(ring[0], ring[1], ring[2])
                    decrypts.append((cipher.encode(code), 'Correct initial positions = ' + 'Rotors are ' + str(rot) +
                                     ', Ring settings are ' + str(ring) + ', Reflector is ' + str(missing)))

    # checks the crib for each of the five codes against all output decrypts and returns the correct result and
    # the correct settings.
    print('Checking crib(s) against decrypted results...')
    for option in decrypts:
        if crib == 'SOCIALMEDIA':
            for social in social_media:
                if option[0].find(social) != -1:
                    out.append(option)
                else:
                    pass
        elif option[0].find(crib) != -1:
            out.append(option)
        else:
            pass
    for possible in out:
        if possible[0].find('NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES') != -1:
            code4.append(possible)
        else:
            pass

    if not code4:
        return out[0]
    else:
        return code4


if __name__ == "__main__":
     #print('Code 1 = ' + str(decode('Beta', 'Gamma', 'V', None, 4, 2, 14, 'M', 'J', 'M',
     #'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ', 'SECRETS', 'KI', 'XN', 'FL')))

     #print('Code 2 = ' + str(decode('Beta', 'I', 'III', 'B', 23, 2, 10, None, None, None,
     #'CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH', 'UNIVERSITY', 'VH', 'PT',
     #'ZG', 'BJ', 'EY', 'FS')))

    #print('Code 3 = ' + str(decode(None, None, None, None, None, None, None, 'E', 'M', 'Y',
    #                               'ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY',
    #                               'THOUSANDS', 'FH', 'TS', 'BE', 'UQ', 'KD', 'AL')))

    #print('Code 4 = ' + str(decode('V', 'III', 'IV', 'A', 24, 12, 10, 'S', 'W', 'U',
    # 'SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW', 'TUTOR',
    # 'WP', 'RJ', 'VF', 'HN', 'CG', 'BS', 'A?', 'I?')))

    #print('Code 5 = ' + str(decode('V', 'II', 'IV', 'NONSTANDARD', 6, 18, 7, 'A', 'J', 'L',
    #'HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX', 'SOCIALMEDIA', 'UG', 'IE', 'PO',
    #'NX', 'WT')))
