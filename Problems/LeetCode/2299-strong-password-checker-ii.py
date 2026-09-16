class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        if len([x for x in password if x.islower()]) < 1: return False
        if len([x for x in password if x.isupper()]) < 1: return False
        if len([x for x in password if x.isdigit()]) < 1: return False
        if len([x for x in password if x in "!@#$%^&*()-+"]) < 1: return False
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                return False
        return True

