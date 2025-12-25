# def decompress_rle(encoded_string):
#     result = ""
#     count = ""

#     for ch in encoded_string:
#         if ch.isdigit():
#             count += ch
#         else:
#             result += ch * int(count)
#             count = ""

#     return result



# print(decompress_rle("3A2B4C"))       # AAABBCCCC
# print(decompress_rle("1W4B1W"))       # WBBBBW
# print(decompress_rle("10X1Y"))        # XXXXXXXXXXY
# print(decompress_rle("1A1B1C1D1E"))   # ABCDE
# print(decompress_rle("12Z"))          # ZZZZZZZZZZZZ

def decompress_rle(encoded_string):
    result = ""
    count = ""

    for i in encoded_string:
        if '0' <= i <= '9':    
            count += i
        else:
            result += i * int(count)
            count = ""

    return result


print(decompress_rle("3A2B4C"))       # AAABBCCCC
print(decompress_rle("1W4B1W"))       # WBBBBW
print(decompress_rle("10X1Y"))        # XXXXXXXXXXY
print(decompress_rle("1A1B1C1D1E"))   # ABCDE
print(decompress_rle("12Z"))          # ZZZZZZZZZZZZ
