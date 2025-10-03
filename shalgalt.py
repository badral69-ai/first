def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1 
    for ch , count in freq.items():
        print(f"{ch}:{count}", end= ", ")
    print()
word = "programm"
char_frequency(word)

def niilber(matrix):
    sum_main = sum(matrix[i][i] for i in range(len(matrix)))
    print(" diagonal", sum_main)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]

print(niilber(matrix))

   
