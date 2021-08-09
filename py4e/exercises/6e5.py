# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    9920.8475";
found = text.find(':')
grab = text[found+1:]
# num = grab.lstrip()
# Python trims white space during float conversion
val = float(grab)
print(grab)
print(val)
# print(type(val))
