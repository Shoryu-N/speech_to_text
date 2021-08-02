import re

class TextProcessor:
  def __init__(self, *, search_words, text):
    self.search_words = search_words
    self.text = text

  def result(self):
    self._print_processed_text_from_words()

  def _print_processed_text_from_words(self):
    for word in self.search_words:
      positions = self._positions(word, self._blank_deleted_text())
      print(f'---------------「{word}」の検索結果---------------')
      self._print_pos_processed_text(positions)

  def _print_pos_processed_text(self, positions):
    for pos in positions:
        self._print_pos(pos)
        self._print_text_from_index(pos)

  def _print_text_from_index(self, pos):
    new_start_ind, new_end_ind = self._new_start_end_index(text=self._blank_deleted_text(), indexes=pos, num=5)
    print('- 前後5文字も含めた文字列')
    print(self._blank_deleted_text()[new_start_ind:new_end_ind])
    print('')      

  def _print_pos(self, pos):
      print('- 出現位置')
      print(pos)
      
  def _new_start_end_index(self, *, text, indexes, num):
    start = indexes[0]
    end = indexes[1]
    new_start_ind =  max(0, start - num)
    new_end_ind = min(len(text), end + num)
  
    return (new_start_ind, new_end_ind)


  def _positions(self, word, text):
    return [m.span() for m in re.finditer(word, text)]

  def _blank_deleted_text(self):
    return self.text.replace(" ", "")