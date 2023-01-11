from itertools import combinations

# import all engima machine classes and functions from enigma.py
from enigma import *

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
