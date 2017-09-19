def new_password(oldpassword, newpassword):

    if len(oldpassword) >= 6 and oldpassword != newpassword:
        return True
    else:
        return False

oldpassword = input("Vul hier je wachtwoord in:")
newpassword = input("Vul hier je nieuwe wachtrwoord in:")
print(new_password(oldpassword, newpassword))