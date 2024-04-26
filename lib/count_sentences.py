#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        if type(value) is str:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        value_last = [letter for letter in self.value][-1]
        if value_last == ".":
            return True
        else:
            return False
        
    def is_question(self):
        value_last = [letter for letter in self.value][-1]
        if value_last == "?":
            return True
        else:
            return False
    def is_exclamation(self):
        value_last = [letter for letter in self.value][-1]
        if value_last == "!":
            return True
        else:
            return False
        
    def count_sentences(self):
        #self.value.replace("!",".").replace("?", ".").split(". ")
        if self.value != "": 
            return len(self.value.replace("!",".").replace("?", ".").split(". "))
        else:
            return 0
        
    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) is str:
            self._value = value
        else:
            print("The value must be a string.")  

    value = property(get_value, set_value)