class Quote():
  def __init__(self, person, words):
    self.person = person
    self.words = words

  def who(self):
    return self.person

  def says(self):
    return self.words + '.'

class QuestionQuote(Quote):
  def says(self):
    return self.words + '?'

class ExclamationQuote(Quote):
  def says(self):
    return self.words + '!'


