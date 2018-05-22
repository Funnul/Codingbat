def xyz_there(str):
    for i in range(len(str)-1):
        if str[i:i+3] == "xyz":
            if str[i-1] != ".":
                return True
    return False
