from src.capitalize import capitalize

if capitalize("hello") != "Hello":
    raise Exception("capitalize('hello') should be 'Hello'")

if capitalize("") != "":
    raise Exception("capitalize('') should be ''")

if capitalize(None) != None:
    raise Exception("capitalize(None) should be None")
"""assert capitalize("hello") == "Hello"
assert capitalize("") == ""
assert capitalize(None) == None
print("all tests passed!")"""