#!/usr/bin/env python3

class MyString:
  
  def __init__(self,value="value"):
    self.value = value
  
  def get_value(self):
    return self._value
  
  def set_value(self,value):
    self._value = value
    if (isinstance(value,str)):
      return value
    print("The value must be a string.")

  def is_sentence(self):
    return self.value[len(self.value)-1] == "."
  
  def is_question(self):
    return self.value[len(self.value)-1] == "?"
  
  def is_exclamation(self):
    return self.value[len(self.value)-1] == "!"
  
  def count_sentences(self):
    split_sentences = self.value.split(" ")
    count  = 0
    for sentense in split_sentences:
      if sentense.endswith(".") or sentense.endswith("!") or sentense.endswith("?"):
        count+=1
    return count
    
  value = property(get_value,set_value)

name = MyString()
print(name.count_sentences())