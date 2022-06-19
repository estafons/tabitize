from models import Octave, Pitch, Accidental
from typing import List, Sequence
from copy import deepcopy

class Note():
    """ Abstract class representing a note Object"""
    # pitch: Pitch
    # octave: Octave
    # accidental: Accidental

    def __init__(self, pitch : Pitch, octave : Octave, accidental : Accidental):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental

    @property
    def pitch(self):
        return self.__pitch.value

    @property
    def octave(self):
        return self.__octave.value
    
    @property
    def accidental(self):
        return self.__accidental.value

    @pitch.setter
    def pitch(self, pitch: Pitch):
        self.__pitch = pitch
    
    @octave.setter
    def octave(self, octave: Octave):
        self.__octave = octave
    
    @accidental.setter
    def accidental(self, accidental: Accidental):
        self.__accidental = accidental
    
    @property
    def val(self) -> str:
        return self.__val
    
    @val.setter
    def val(self, val) -> None:
        self.__val = val

class Tab():
    """a tablature class"""

    @property
    def tab(self) -> List:
        return self.__tab

    @tab.setter
    def tab(self, tab: List[Note]) -> None:
        print("this is tab.setter")
        self.__tab = deepcopy(tab)

class TabFromListList(Tab):
    """subclass working as an interface to read notes from list of lists"""

    def __init__(self, ListList : Sequence[Sequence[str]]) -> object: 
        self.tab = [Note(Pitch(x[0]), Octave(x[1]), Accidental(x[2])) for x in ListList]
    


x = Note(Pitch('C'), Octave('one'), Accidental('perfect'))
print((x.pitch))

t = TabFromListList([('C', 'one', 'perfect'),[Pitch('D'), Octave('two'), Accidental('perfect')]])
t = TabFromListList([(Pitch('C'), Octave('one'), Accidental('perfect')),(Pitch('D'), Octave('two'), Accidental('perfect'))])

print(t)
# t = Tab()
# t.tab = [x, x]
for n in t.tab:
    print(n.pitch)
