from copy import deepcopy
from constants import *


class Note:
    """Музыкальная нота с возможностью копирования."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        self.duration = duration

    def clone(self, **params):
        """Создаёт новый экземпляр ноты с теми же параметрами."""
        res = deepcopy(self)
        res.__dict__.update(params)
        # Геннадий что в данном подходе неправильно?
        # for i, j in params.items():
        #     print(i,j)
        # КОММЕНТАРИЙ: то, что здесь вы создаёте атрибут с именем 'i'
        #     res.i = j
        return res

    def __str__(self):
        return (f"Высота: {self.pitch}, Октава: {self.octave}"
                + f", Accidental: {self.accidental}"*(self.accidental is not None)
                + f", Продолжительность: {self.duration}")


class ScoreNote(Note):
    """Изображение музыкальной ноты в партитуре."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 stem_up: bool,
                 beam: bool = False,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.stem_up = stem_up
        self.beam = beam

    def __str__(self):
        return super().__str__() \
               + f", Штиль: " + ("вверх" if self.stem_up else "вниз") \
               + f", Ребро: {self.beam}"


class MIDINote(Note):
    """Кодирование музыкальной ноты в MIDI протоколе."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 velocity: int,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.velocity: int = velocity

    def __str__(self):
        return super().__str__() \
               + f", Атака: {self.velocity}"


note1 = Note(
    pitch=Pitch.B,
    octave=Octave.LINE_3,
    duration=Duration.QUARTER,
    accidental=Accidental.FLAT
)
midi_c1 = MIDINote(
    pitch=Pitch.C,
    octave=Octave.LINE_1,
    velocity=80,
    duration=Duration.HALF
)
score_d3 = ScoreNote(
    pitch=Pitch.D,
    octave=Octave.LINE_3,
    stem_up=True
)

clone_score = score_d3.clone(octave=Octave.GREAT)
clone_midi = midi_c1.clone(pitch=Pitch.D, duration=Duration.WHOLE)

print("Миди_нота:")
print(midi_c1, "\n")
print("Клонированная миди нота с измененными аттрибутами:")
print(clone_midi, "\n")
print("Нота в партитуре: ")
print(score_d3, "\n")
print("Клонированная нота в партитуре с измененными аттрибутами:")
print(clone_midi)


# stdout:
"""
Миди_нота:
Высота:1, Октава:3, Продолжительность: 2, скорость: 80 

Клонированная миди нота с измененными аттрибутами:
Высота:2, Октава:3, Продолжительность: 1, скорость: 80 

Нота в партитуре: 
Высота:2, Октава:5, Продолжительность: 4, stem_up: True, beam: False 

Клонированная нота в партитуре с измененными аттрибутами:
Высота:2, Октава:3, Продолжительность: 1, скорость: 80

"""


# ИТОГ: отлично — 5/5
