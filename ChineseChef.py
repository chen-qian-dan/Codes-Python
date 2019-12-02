


from Chef import Chef

# inside of this ChineaseChef class, I can use all functions in Chef class.
class ChineseChef(Chef):

    # override the class.
    def make_special_dish(self):
        print("The chef makes orange chicken. ")

    def make_fried_rice(self):
        print("The chef makes fried rice. ")