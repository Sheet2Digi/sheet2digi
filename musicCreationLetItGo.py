import pysynth

letItGo = (
    ('b5', 8), ('c6', 8), ('e5', 8), ('b5', 4),
    ('c6', -4), ('b5', 8), ('c6', 8), ('e5', 8),
    ('c6', 4), ('b5', -4), ('a5', 8), ('b6', 8),
    ('d5', 8), ('a5', 4), ('b5', -4), ('g5', 2),
    ('f#5', 2)
)

pysynth.make_wav(letItGo, bpm = 100, fn = "letItGo.wav")
