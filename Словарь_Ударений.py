from itertools import permutations
from random import sample


def hash_key(value):
    return int(''.join(str(ord(c)) for c in value if latin(c)))


def latin(c):
    return ord(c) in range(1040, 1104) or ord(c) == 1025 or ord(c) == 1105


correct_words_list = []
correct_words_set = set()
correct_words_hashes = []

with open('Ударения.txt', mode='r', encoding="utf-8") as f:
    for word in f:
        correct_words_list.append(''.join(word.split()))
        correct_words_set.add(''.join(word.split()))
        correct_words_hashes.append(str(hash_key(word)))
true_list = [True] * len(correct_words_list)
correct_words = {k: v for k, v in zip(correct_words_hashes, zip(correct_words_list, true_list))}

vowels_const = set("АЕЁИОУЫЭЮЯаеёиоуыэюя")
all_words_list = []
all_words_set = set()
all_words_hashes = set()

for word in correct_words.values():
    word = list(word[0])
    count = 0
    for letter in word:
        if letter in vowels_const:
            count += 1
    commands = '2' + '1' * (count - 1)
    for permutation in permutations(commands):
        count = 0
        for i in range(len(word)):
            if word[i] in vowels_const:
                if permutation[count] == '1':
                    word[i] = word[i].lower()
                if permutation[count] == '2':
                    word[i] = word[i].upper()
                count += 1
        all_words_list.append(''.join(word))
        all_words_hashes.add(hash_key(''.join(word)))
        all_words_set.add(''.join(word))

all_words_hashes = sorted(all_words_hashes)
incorrect_words_set = all_words_set - correct_words_set
incorrect_words_hashes = [hash_key(word) for word in sorted(incorrect_words_set)]
false_list = [False] * len(incorrect_words_set)
incorrect_words = {k: v for k, v in zip(incorrect_words_hashes, zip(sorted(incorrect_words_set), false_list))}
all_words = {k: v for k, v in zip(sorted(all_words_hashes), sorted(
    sorted(zip(correct_words_list, true_list)) + sorted(zip(list(incorrect_words_set), false_list))))}


class ApplicationData:
    """Данные по приложению, нужные для генерации заданий и ответов"""

    def __init__(self):
        self.all_words_hashes = all_words_hashes
        self.all_words = all_words
        self.correct_words = correct_words
        self.incorrect_words = incorrect_words

    @staticmethod
    def task_and_response():
        while True:
            task_hashes = sample(all_words_hashes, 5)
            keys = set()
            task = []
            answers = []
            counter = 0
            for word_hash_key in task_hashes:
                word_info = all_words[word_hash_key]
                if word_info[1]:
                    answers.append(word_info[0] + '\n')
                    counter += 1
                else:
                    answers.append("")
                task.append(word_info[0])
                keys.add(word_info[0].lower())
            if (0 < counter < 5) and len(keys) == 5:
                break
        return dict(zip(task, answers))


'''x = application_data.task_and_response(application_data)
print(f'Task №1: {", ".join(i[0] for i in x)}')
print('Answer:')
for i in x:
    if i[1] != "":
        print(i[1][:-1])'''

'''
print(all_words)
print(len(all_words))
print(correct_words)
print(len(correct_words))
print(incorrect_words)
print(len(incorrect_words))
for i,j in x:
    print(i, j.split())'''

'''Вывод
print(all_words)
print(len(all_words))
print(correct_words)
print(len(correct_words))
print(incorrect_words)
print(len(incorrect_words))'''

'''
from random import *
for i in range(1,20):
    problem = sample(list(all_words_set), 5)
    count = 0
    keys = set()
    for word in problem:
        if word in correct_words_set:
            count += 1
        keys.add(words.lower())
    if count > 0 and len(keys)==5:
        with open(f'D:/Рабочий стол/Задания №2/Problems/Problem №{i}.txt', 'w+', encoding='utf-8') as p:
            for word in problem:
                p.writelines(word+'\n')
        with open(f'D:/Рабочий стол/Задания №2/Answers/Answer №{i}.txt', 'w+', encoding='utf-8') as a:
            for word in problem:
                if word in correct_words:
                    a.writelines(str(correct_words[word])+'\n')
                if word in incorrect_words:
                    a.writelines(str(incorrect_words[word])+'\n')
print(base)'''
