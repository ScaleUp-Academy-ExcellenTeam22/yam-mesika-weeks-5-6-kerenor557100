#submitted by Keren Or Hadad 208025205


# part 5.3
def lahshenanit():
    result = ""
    try:
        with open("logo.jpg", "rb") as file:
            byte = file.read(1)
            while byte:
                byte_hex = int(byte.hex(), 16)
                if byte_hex in range(97, 123):
                    result += chr(byte_hex)
                elif byte_hex == 33:
                    result += chr(byte_hex)
                    if len(result) >= 6:
                        print(result)
                        result = ""
                else:
                    result = ""
                byte = file.read(1)
    except IOError:
        print('error')


lahshenanit()
"""
output:
python!
isawesome!
welldone!
goodjob!
"""