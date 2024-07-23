from dateutil import parser

print(parser.parse('2024-07-13T12:57:12'))

print(parser.parse('30/12/2024'))

print(parser.parse('12/30/2024'))

print(parser.parse('03/08/2024', dayfirst = True))

print(parser.parse('08/03/2024'))

s = 'Today is July the 13, 2024 at Ind UTC'

print(parser.parse('July 13, 2024 '))

try:
    print(parser.parse(s, fuzzy_with_tokens = True))
except Exception as e:
    print(e)


