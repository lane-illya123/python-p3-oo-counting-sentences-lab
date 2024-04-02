#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value = ""): 
       
     self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, val):
    if isinstance(val, str):
      self._value = val
    else:
      print("The value must be a string.") 

  def is_sentence(check_p):
    if check_p.value.endswith("."):
      return True
    else:
      return False

  def is_question(check_q):
    if check_q.value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(check_e):
    if check_e.value.endswith("!"):
      return True
    else:
      return False

  def count_sentences(check_s):
    check_s.value = check_s.value.replace("?", ".")
    check_s.value = check_s.value.replace("!", ".")
    sentences = check_s.value.split(".")
    sentences = [sentence for sentence in sentences if sentence]  # Remove empty sentences
    return len(sentences)    