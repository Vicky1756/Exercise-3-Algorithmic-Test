roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
         (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class int_roman_converter:
    def converter(self, num):
        alphabet = " "

        while num > 0:

            for i, r in roman:
                while num >= i:
                    alphabet += r
                    num -= i
        return alphabet


print(int_roman_converter(). converter(120))
