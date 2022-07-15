def county(lst):
    word_amount = []
    distinct = len(set(lst))
    for word in lst:
        if lst.count(word) == 1:
            word_amount.append(1)
        else:
            word_amount.append(lst.count(word))
            lst.remove(word)


    return distinct, word_amount

words = []
n_number = int(input("enter number of words:"))
for x in range(n_number):
    word = input("enter words:")
    words.append(word)



print(county(words))
