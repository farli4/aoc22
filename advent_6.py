def all_unique(s):
    for c in s:
        if s.count(c) > 1:
            return False
    return True


def find_stuff(s, length):
    chars_until_detected = -1
    for i in range(len(s)-length + 1):
        code = chars[i:i+length]
        if all_unique(code):
            chars_until_detected = i+length
            break
    return chars_until_detected


if __name__ == '__main__':

    with open('6_input.txt') as f:
        chars = f.read()

    indx_first_packet = find_stuff(chars, 4)
    indx_first_message = find_stuff(chars, 14)

    print(indx_first_packet)
    print(indx_first_message)
