def all_unique(s):
    for c in s:
        if s.count(c) > 1:
            return False
    return True


def find_packet(s):
    chars_until_detected = -1
    for i in range(len(chars)-3):
        code = chars[i:i+4]
        if all_unique(code):
            chars_until_detected = i+4
            break
    return chars_until_detected


def find_message(s):
    chars_until_detected = -1
    for i in range(len(chars)-13):
        code = chars[i:i+14]
        if all_unique(code):
            chars_until_detected = i+14
            break
    return chars_until_detected


if __name__ == '__main__':

    with open('6_input.txt') as f:
        chars = f.read()

    indx_first_packet = find_packet(chars)
    indx_first_message = find_message(chars)

    print(indx_first_packet)
    print(indx_first_message)
