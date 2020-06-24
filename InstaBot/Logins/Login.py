loginFile = open("Atom\InstagramBot\InstagramBot\InstaBot\Logins\Login.txt", "r")

def LoginUM():
    return loginFile.readline()
    
def LoginPW():
    return loginFile.readline()
