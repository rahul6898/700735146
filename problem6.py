# Problemm to show the number of unique words used in the given sentence

sentence = "I am a teacher and I love to inspire and teach people".split(" ")
set_sentence = set()
for elem in sentence:
    if elem not in set_sentence:
        set_sentence.add(elem)
    elif elem in set_sentence:
        set_sentence.remove(elem)

print(f'number of unique items in set: {len(set_sentence)}')