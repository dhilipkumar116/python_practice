s = "hello world"
print(type(s))
print(s[1])
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('l'))
print(s.endswith('ld'))
print(s.find('o'))
print(s.find('o',5))
print("Is upper : ",s.isupper())
print("Is lower : ",s.islower())
print("Is AlphaNumeric : ",s.isalnum())
print("Is Alpha : ",s.isalpha())
s="   dhilip   "
print(len(s))
print(s.strip())
print(s.lstrip()) # removing left space
print(s.rstrip()) # removing right space