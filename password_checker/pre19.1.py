# We're going to invoke a function ("create_password_checker"),
# and the return value from that function will itself be a function.

from string import ascii_uppercase as uppercase, ascii_lowercase as lowercase, punctuation, digits

def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def password_checker(pw):
        """
        Returns a boolean (indicating if the password passed the test) and
        a dict showing the difference between min and actual numbers.
        :param pw:
        :return:
        """
        pwset = set(pw)

        calculations = {'uppercase': len(set(uppercase) & pwset) - min_uppercase,
                        'lowercase': len(set(lowercase) & pwset) - min_lowercase,
                        'punctuation': len(set(punctuation) & pwset) - min_punctuation,
                        'digits': len(set(digits) & pwset) - min_digits,
                        }
        return all(x >= 0
                   for x in calculations.values()), calculations

    return password_checker

pc1 = create_password_checker(2,3,1,4)
print(pc1('Ab!1'))
print(pc1('ABcde!1234'))


