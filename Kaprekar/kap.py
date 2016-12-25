# from random import randint

DIGITS = 4

def is_repdigit(n):
    while n > n%10:
        if (n%10) * 11 != n%100:
            return False
        n //= 10
    return True

def _insert_at(n, insert):
    place = 1
    while place < n and insert > (n % (place*10)) // place:
        place *= 10
    return place

def _insert_digit(desc, to_insert):
    place = _insert_at(desc, to_insert)
    return (desc*10) - (9 * (desc%place)) + (to_insert*place)

def to_descending(raw_digits):
    desc = 0
    while raw_digits > 0:
    # for i in range(total_digits):
        to_insert = raw_digits % 10
        raw_digits //= 10
        desc = _insert_digit(desc, to_insert)
    return desc

def reverse_digits(forward_digits):
    reverse = 0
    while forward_digits > 0:
        reverse = reverse * 10 + (forward_digits%10)
        forward_digits //= 10
    return reverse

def subtraction(desc, asc):
    print "  %s" % (desc)
    print "- %s" % (asc)
    print "_________"
    diff = desc - asc
    print "  %s\n" % (diff)
    return diff

def main():
    d = 4
    n = 495
    # print "insert 6 at %s's place" % (insert_at(n, 6))
    # print "6 inserted into %s: %s" % (n, insert_digit(n,6))
    # print "%s in descending order: %s" % (n, to_descending(n))

    # print is_repdigit(8888)

    while not ((d==3 and n==495) or (d==4 and n==6174)):
    # while n != 6174 and n != 495:
    # for i in range(5):
        desc = to_descending(n)
        if desc < 10**(d-1):
            desc *= 10
        asc = reverse_digits(desc)
        n = subtraction(desc, asc)

    # print "%s:\n\tdescending: %s\n\tascending: %s" % (n, desc, asc)




if __name__ == '__main__':
    main()
