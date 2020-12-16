class Document:
  def __init__(self, name):
    self.name = name

  @property
  def show(self):
    raise NotImplementedError("ABSTRACT METHOD: SUBCLASS MUST IMPLEMENT")


class Pdf(Document):
  @property
  def show(self):
    return "show pdf contents"


class Word(Document):
  @property
  def show(self):
    return "show word contents"


docs = [
  Pdf('doc1: pdf'),
  Word('doc2: word'),
  Pdf('doc3: pdf'),
  Word('doc4: word')
]

for doc in docs:
  print(f"doc name: {doc.name} - show: {doc.show}")