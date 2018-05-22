

def not_string(str):
    if "not" in str[:3]:
        return str
    else:
        return "not " + str

# str[:3] for first 3 letters
