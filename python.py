# def subarray(sub):
#     subarray_sums = set()
#     for i in range(len(sub)):
#         for j in range(i + 1, len(sub) + 1):
#             print(sub[i:j])
#             subarray_sums.add(sum(sub[i:j]))
#     return len(subarray_sums)

# subbarray = [1, 2, 3]
# print("davtagdahgu toonuudin niilber:", subarray(subbarray))

# def anagrams(ugnuud):
#     result = {}
#     for ug in ugnuud:
#         key = ''.join(sorted(ug))
#         if key not in result:
#             result[key] = []
#         result[key].append(ug)
#     return result

# ugnuud = ["eat", "tea", "ate", "bat", "tab", "tan", "nat"]
# result = anagrams(ugnuud)

# print( "dictionary" , (result))

# def dundaj_onoo(suragchid):
#     dundaj = {}
#     for ner, onoo in suragchid.items():
#         dundaj[ner] = sum(onoo) / len(onoo)
#     dundaj = dict(sorted(dundaj.items(), key=lambda item: item[1], reverse=True))
#     winner = max(dundaj, key=dundaj.get)
#     print("scholarship", winner, dundaj[winner])
#     return dundaj
# suragchid = {
#     "anu": [85, 90, 92],
#     "bilguun": [78, 80, 74],
#     "saruul": [95, 92, 96]
# }
# result = dundaj_onoo(suragchid)
# print("dundaj onoo:", result,)

# def spiral_matrix(n):
#     matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
#     result = []
#     deed, dood, zuun, baruun = 0, n - 1, 0, n - 1

#     while deed <= dood and zuun <= baruun:
#         for i in range(zuun, baruun + 1):
#             result.append(matrix[deed][i])
#         deed += 1

#         for i in range(deed, dood + 1):
#             result.append(matrix[i][baruun])
#         baruun -= 1

#         if deed <= dood:
           
#             for i in range(baruun, zuun - 1, -1):
#                 result.append(matrix[dood][i])
#             dood -= 1

#         if zuun <= baruun:
           
#             for i in range(dood, deed - 1, -1):
#                 result.append(matrix[i][zuun])
#             zuun += 1

#     return result

# n = 3
# print("Spiral daraalal:", spiral_matrix(n))
# def data():
#     return {
#         "user": {
#             "name": "Naraa",
#             "info": {
#                 "age": 20,
#                 "city": "UB"
#         }
#     }
# }
# print(data()["user"]["name"], data()["user"]["info"]["age"], data()["user"]["info"]["city"])

# def is_valid_sudoku(board):
#     for i in range(9):
#         row = set()
#         col = set()
#         box = set()
#         for j in range(9):
#             if board[i][j] != '.':
#                 if board[i][j] in row:
#                     return False
#                 row.add(board[i][j])
#             if board[j][i] != '.':
#                 if board[j][i] in col:
#                     return False
#                 col.add(board[j][i])
#             box_row = 3 * (i // 3)
#             box_col = 3 * (i % 3)
#             if board[box_row + j // 3][box_col + j % 3] != '.':
#                 if board[box_row + j // 3][box_col + j % 3] in box:
#                     return False
#                 box.add(board[box_row + j // 3][box_col + j % 3])
#         return True
# sudoku_board = [
#     ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
#     ["2", "3", "1", "5", "6", "4", "8", "9", "7"],
#     ["3", "1", "2", "6", "4", "5", "9", "7", "8"],
#     ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
#     ["5", "6", "4", "8", "9", "7", "2", "3", "1"],
#     ["6", "4", "5", "9", "7", "8", "3", "1", "2"],
#     ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
#     ["8", "9", "7", "2", "3", "1", "5", "6", "4"],
#     ["9", "7", "8", "3", "1", "2", "6", "4", "5"]
# ]
# print("zuv sudoku mun?", is_valid_sudoku(sudoku_board))
# def is_neighbor(w1, w2):
#     return sum(a != b for a, b in zip(w1, w2)) == 1

# def bfs(beginword, endword, wordlist):
#     queue = [(beginword, 1)]   # (word, steps)
#     visited = set()

#     while queue:
#         word, steps = queue.pop(0)

#         if word == endword:
#             return steps

#         if word not in visited:
# #             visited.add(word)

# #             for w in wordlist:
# #                 if is_neighbor(word, w) and w not in visited:
# #                     queue.append((w, steps + 1))

# #     return 0
  
# # dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
# # print(bfs("hit", "cog", dictionary))
# def triangle_perimeter(a, b, c):
#     hariu = int( a+ b+ c)
#     return hariu


# def niilber(a, b):
#     hariu = int ( a+b )
#     return hariu
# hariu = niilber( 1 , 2)


# def cube(a):
#     hariu =  (a * a * a)
#     return hariu 
# hariu = cube(5)

# def square_perimeter(a,b):
#     p = (a * 2) + (b * 2)
#     hariu = (a * b) 
#     return hariu , p 

# def hariu(x):
#     y = (3*x)-5
#     r = 4 * (x * x) - (3 * x) + 5
#     return y , r 

# def suulintoo(s):
#     suuliinh = str(s)
#     too =  suuliinh[-1]
#     return int(too) 
# def too(f):
#     aravt =( f % 100) // 10 
#     return aravt 
# def urjver(a):
#     urjver = str(a)
#     ehniitoo = int(urjver[0])
#     hoerdohtoo = int(urjver[1])
#     return ehniitoo * hoerdohtoo
# def niilber(a):
#     if a > 0:
#         niilber = str(a)
#         ehniitoo = int(niilber[0])
#         hoerdohtoo = int(niilber[1])
#         guravdahtoo = int(niilber[2])
#         return ehniitoo + hoerdohtoo + guravdahtoo
# def second(s):
#     hours = s // 3600
#     minut = s // 60
#     seconds = s % 3660
    
#     return f"{ hours, minut, seconds}"
# def second(a, b , c):
#     tsag = a * 3600
#     minut = b * 60
#     second = tsag + minut + c 
#     return second
# def honog(a):
#     odor = a // 24
#     tsag = a % 24
#     return f"{odor,"odor"}{tsag,"tsag"}"
# def honoge(a, b):
#     odor = a * 24
#     tsag = odor + b
#     return tsag
# def jilsar(a):
#     jil = a // 12
#     sar = a % 12
#     return f"{jil, sar}"
# def sar(a, b):
#     jil = a * 12 
#     sar = jil + b
#     return sar
# def ih(a, b):
#     if a > b:
#         return a    
#     else :
#         return b 
# def baga(a, b):
#     if a > b:
#         return b
#     else:
#         return a

# def find_biggest(numbers):
#     biggest = numbers[0]   
#     for num in numbers:
#         if num > biggest:
#             biggest = num
#     return biggest
# def find_smallest(number):
#     smallest = number[0]
#     for num in number:
#         if num < smallest:
#             smallest = num
#     return smallest
# def niilber(a, b, c, d):
#     total = 0
#     for num in [a, b, c, d]:
#         if num > 80:
#             total += num
#     return total

# def urjver(a, b, c, d):
#     total = 1
#     for num in [a, b, c, d]:
#         if num < 5:
#             total *= num
#     return total 
# print(urjver(1, 4, 3, 6))

# def niilber(a, b, c):
#     total = 0 
#     for num in [a ,b, c]:
#         if num // 2:
#             total += num
#             return total 
# print(niilber(10, 3, 5))

# def multiply_odds(a, b, c):
#     result = 1
#     found = False

#     for num in [a, b, c]:
#         if num % 2 == 1:   
#             result *= num
#             found = True

#     return result if found else 0
# def tavintoo(a, b, c,):
#     result=[]
#     for num in a, b, c:
#         if num == 5:
#             result.append(num)
#     return result 
# def huvaagdahtoo(a, b, c, d):
#     result=[]
#     for num in a, b, c, d:
#         if num % 3== 0 :
#             result.append(num)
#     return result 
# print(huvaagdahtoo(3,12,8,9))
# def huvaalt(a, b, c, d):
#     result = 0
#     for num in a, b, c, d:
#         if num % 11 != 0:
#             result += num 
#     return result 


# def dugaar(num):
#     if num > 10:
#         print("yes")
#     else:
#         print("no")
# print(dugaar(11))

# def nomer(num):
#     if num < 5 :
#         print("yes")
#     else:
#         print("no")

# def check_even(a, b, c):
#     for num in [a, b, c]:
#         if num % 2 == 0:   
#             print("yes")
#         else:
#             print("no")


# def print_lol(*nums):
#     if not nums:   
#         for _ in range(3):
#             print("lol")
#     else:
#         print("You entered:", nums)
# print_lol()      

# def nniilber(a):
#     return sum(range(1, a+1))

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# def nomer(num, times):
#     return num * times

# result = nomer(6, 100)
# print(result)

# def toonzereg(n):
#     result = 1
#     for i in range(n):
#         result *= 2
#     return result

# print(toonzereg(5))  
# def zereg(num, times):
#     result = 1
#     for i in range(times):
#         result *= num
#     return result

# print(zereg(3, 4))  

# def dun(a):
#     if a > 3:
#         print ("tentssen")
#     else:
#         print ("unasan")
# print(dun(2))

# def hariu(a):
#     if a == 2:
#         print("muu")
#     elif a == 3:
#         print("dund")
#     elif a == 4:
#         print("sain")
#     elif a == 5:
#         print("onts")
#     else:
#         print("")

# def dun(a):
#     if a > 100 or a < 0:   
#         print("Invalid number")
#     elif a > 89:
#         print("A")
#     elif a > 79:
#         print("B")
#     elif a > 69:
#         print("C")
#     elif a > 59:
#         print("D")
#     else:
#         print("F")

# def garag(a):
#     if a == 1:
#         print("davaa")
#     elif a == 2 :
#         print("myagmar")
#     elif a == 3:
#         print("lhagva")
#     elif a == 4:
#         print("purev")
#     elif a == 5:
#         print("baasan")
#     elif a == 6:
#         print("hagassain")
#     elif a == 7:
#         print("butensain")
#     else :
#         print()
# def season(a):
#     if a in [12, 1, 2]:
#         return "Winter"
#     elif a in [3, 4, 5]:
#         return "Spring"
#     elif a in [6, 7, 8]:
#         return "Summer"
#     elif a in [9, 10, 11]:
#         return "Autumn"
#     else:
#         return "Invalid month"
# def gurvaljin(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         print("bolohgui")
#     else:
#         print("bolno")
# def hurd(a):
#     for i in range(1,11):
#         print(f"{a} * {i}={a*i}")

# def zereg(too, urjver):
#     for i in range(1, urjver+1 ):
#         print(f"{too} ^ {i} = {too ** i}")
# print(zereg(3,5))
# def hariult(a, b, c):
#     print(f"{a * b - c}")



9.23
# def palindrome(word):
#     word = word.lower()
#     return word == word[::-1]
# print(palindrome("madam"))  

# s 

# def buhtoo():
#     k = list(map(int, input("oruul :").split(" ")))
#     target = 6      
#     for i in range(len(k)):
#         for j in range(len(k)):
#             if k[i] + k[j] == target:
#                 print(f"{k[i]} + {k[j]} = {target}")
# buhtoo()

# def str_dotorh_dawtagdsan_useg():
#     a = str(input("string oruul :"))
#     b = []
#     for i in range(len(a)):
#         count = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#               count += 1
#             if count > 1 and a[i] not in b:
#                b.append(a[i])
#             return (b)
#     print(str_dotorh_dawtagdsan_useg())

# def davhardsantoo(arr):
#         davhardsan = []
#         for num in arr:
#             if arr.count(num) > 1 and num not in davhardsan :
#                 davhardsan.append(num)
#         return davhardsan 
# numbers = [1,2,3,2,4,5,1]
# print(davhardsantoo(numbers))
 
# def ugnuud(ug):
#     ug = ug.lower()
#     left, right = 0, len(ug) - 1 

#     while left < right:           
#         if ug[left] != ug[right]:   
#             print("not palindrome")
#             return
#         left += 1
#         right -= 1

#     print("palindrome")
# (ugnuud("madam"))

# def max_subarray_sum(arr):
#     current_sum = arr[0]
#     max_sum = arr[0]

#     for i in range(1, len(arr)):
#         current_sum = max(arr[i], current_sum + arr[i])  
#         max_sum = max(max_sum, current_sum)  

#     return max_sum

# def ugnuud(word1, word2):
#     return sorted(word1.lower()) == sorted(word2.lower())

# print(ugnuud("Listen", "silenT")) 

# def niilber(matrix):
#     sum_main = sum(matrix[i][i] for i in range(len(matrix)))
#     print(" diagonal", sum_main)
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]

# ]

# (niilber(matrix))

# def anhnii(n):
#     primes = []  
#     is_prime = [True] * (n + 1) 
#     is_prime[0] = is_prime[1] = False 

#     for num in range(2, n + 1):
#         if is_prime[num]:
#             primes.append(num)  
#             for multiple in range(num * 2, n + 1, num):
#                 is_prime[multiple] = False

#     return primes
# print(anhnii(20))

# def print_max_min(numbers):
#     print("Maximum number:", max(numbers))
#     print("Minimum number:", min(numbers))

# nums = [5, 3, 9, 1, 7]
# print_max_min(nums)

# def char_frequency(s):
#     freq = {}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1 
#     for ch , count in freq.items():
#         print(f"{ch}:{count}", end= ", ")
#     print()
# word = "programm"
# char_frequency(word)

# def niilber(matrix):
#     max_sum = sum(matrix[0])
#     max_row = matrix[0]
    
#     for row in matrix:
#         current_sum = sum(row)
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_row = row
#     return max_row
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(niilber(matrix))

# def binary(n):
#     if n == 0:
#         return "0"
#     result = ""
#     while n > 0:
#         result = str(n % 2) + result
#         n = n // 2
#     return result

# num = int(input("nomer oruul: "))
# print("Binary:", binary(num))
9.24
# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)
# for i in range(1, 21):
#     fizzbuzz(i)

# def longest_word(text):
#     words = text.split()
#     longest = max(words, key=len)
#     return longest, len(longest)

# s = "hamgiin urt ug"
# word, length = longest_word(s)
# print("urt ug ni", word)
# print("usgin too", length)

# def niilber(nums):
#     total = 0
#     for n in nums:
#         if nums.count(n) == 1: 
#             total += n
#     return total
# numbers = [1, 2, 2, 3, 4, 4]
# print("niilber", niilber(numbers))

# suragchid = {
#     "anu": [85],
#     "bilguun": [78],
#     "saruul": [95]
# }

# print("ih duntei suragch", max(suragchid))
# def nomerud(list1, list2):
#     return set(list1) & set(list2) 
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# print(nomerud(a, b))
# scores = {'Bat': 85, 'Bold': 92, 'Suren': 78, 'Naraa': 92}

# for name, score in scores.items():
#     if score > 90:
#         print(name)
# def while_loop():
#     n = int(input("too :"))
#     total = 0   
#     count = 0   
#     i = 1 
#     while total <= n:
#         total += i
#         count += 1
#         i += 1   
#     print(f"too : {count}, niilber: {total}")
# while_loop()
# def letter_count(word):
#     count_dict = {} 
#     for ch in word:
#         if ch in count_dict:
#             count_dict[ch] += 1   
#         else:
#             count_dict[ch] = 1  
#     return count_dict

# result = letter_count("hello")
# print(result)
# for letter, count in result.items():
#     print(letter, "→", count)

# def find_number():
#     data = {
#         "bat": 99112233,
#         "bold": 88110022,
#         "suren": 77112233,
#         "naraa": 99119911
#     }
#     name = input("Нэр оруулна уу: ").lower()  # lower() гэж функц болгож бичих шаардлагатай
#     # data доторх бүх түлхүүрийг жижиг үсэгтэй болгож харьцуулж байна
#     normalized_data = {k.lower(): v for k, v in data.items()}
    
#     if name in normalized_data:
#         print(f"{name}-ийн дугаар: {normalized_data[name]}")
#     else:
#         print("Буруу нэр")

9.25
# find_number()
# matrix = [
#     [1 , 2], 
#     [3 , 4],
#     [5 , 6]
# ]
# solih = list(map(list, zip(*matrix)))
# print(solih)
# 
21.
# text = "hello world"
# print(text.title())
# 
# text = "hello nigga"
# words= text.split()
# capitalized= [ a.capitalize() for a in words]
# result = " ".join(capitalized)
# print(result)
22
# def hassn(numbers):
#     return [n for n in numbers if n >= 0]
# nums = [3, -1, 4, -2, 7]
# result = hassn(nums)
# print(result)

23# def factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     too = str(factorial)
#     count = 0
#     for ch in reversed(too):
#         if ch == '0':
#             count += 1
#         else:
#             break
#     print(f"too ni {n} bol factorial {factorial}")
#     print(f"suulin 0 iin toonuud{count}")
# num = int(input("nomer oruul "))
# factorial(num)

24# arr = [1, 2, 3, 4, 5]
# reversed_arr = []
# for i in range(len(arr)-1, -1, -1):
#     reversed_arr.append(arr[i])

# print("Reversed array:", reversed_arr)

25# def palindrome(s):
#     s = "".join(s.lower().split())
#     left, right = 0, len(s) - 1 

#     while left < right:           
#         if s[left] != s[right]:   
#             return False
#         left += 1
#         right -= 1
#     return True
# sum = palindrome("A man a plan a canal Panama")
# print(sum)
26# def nomer(arr):
#     max= arr[0]
#     min = arr[0]
#     for i in arr:
#         if i > max:
#             max = i 
#         if i < min :
#             min = i 
#     return max - min 
# print(nomer([1, 2 , 3, 20]))
27# def too(s):
#     s = str(s)
#     s = " ".join(s).split()
#     arr = [int(x) for x in s]
#     print(arr)
#     sum = 0
#     for i in arr:
#        sum += i
#     return sum
# print(too(1233))
28# def too(n: int):
#     if n == 0:
#         return null

#     arr = []
#     while n % 2 == 0:
#         arr.append(2)
#         n //= 2
#     print(n)

29#     gurvaarshaana = 3
#     while gurvaarshaana * gurvaarshaana <= n:
#         while n % gurvaarshaana == 0:
#             arr.append(gurvaarshaana)
#             n //= gurvaarshaana
#         gurvaarshaana += 2

#     if n > 1:
#         arr.append(n)

#     return arr

# print(too(36))
#30
# def too(arr):
#     seen = set()
#     out = []
#     for x in arr:
#         if x not in seen:
#             seen.add(x)
#             out.append(x)
#     return out

# print(too([10,20,10,30,40,10]))

# #31
# def too2(psda):
#     lalar = []
#     for gici in psda:
#         if gici.isalpha():
#             lalar.append(gici)
#     clean_psda = "".join(lalar)

#     if len(set(clean_psda)) <= 1:
#         return None

#     def psda_key_first(i):
#         return (clean_psda.count(clean_psda[i]), -i)

#     lalar_i1 = max(range(len(clean_psda)), key=psda_key_first)
#     gici = clean_psda[lalar_i1]

#     lalar = clean_psda.replace(gici, "")
#     if not lalar:
#         return None

#     def psdaKey(i):
#         return (lalar.count(lalar[i]), -i)

#     gici_i2 = max(range(len(lalar)), key=psdaKey)
#     return lalar[gici_i2]
# too2("12344")
# #32
# def too3(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
    
# print(too3(100))
# #33
# def too4(arr):
#     return [x for x in arr if too3(x)]
    
# print(too4([10, 2, 3, 4, 7, 11]))
# #34
# def too5(n):
#     s = str(n)
#     return s == "0" or (n >= 0 and all(a == b for a, b in zip(s, reversed(s))))
    
# print(too5(121))
# #36
# def too6(s):
#     ans = ""
#     for i in range(len(s)):
#         for l, r in [(i, i), (i, i+1)]:
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l -= 1; r += 1
#             if r - l - 1 > len(ans):
#                 ans = s[l+1:r]
#     return ans
    
# print(too6("babad"))
# #37
# def too7(a):
#     n = len(a)
#     if n < 2:
#         return None

#     x0, x1 = a[0], a[1]
#     if x0 >= x1:
#         max1, max2 = x0, x1  
#         min1, min2 = x1, x0  
#     else:
#         max1, max2 = x1, x0
#         min1, min2 = x0, x1

#     for x in a[2:]:
#         if x >= max1:
#             max2, max1 = max1, x
#         elif x > max2:
#             max2 = x
#         if x <= min1:
#             min2, min1 = min1, x
#         elif x < min2:
#             min2 = x

#     left  = min1 * min2   
#     right = max1 * max2   
#     return (min1, min2, left) if left > right else (max2, max1, right)

# print(too7([3, 5,-10,-6, 2]))

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1 
#     while left <= right:
#         mid =(left + right)//2 
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1 
#         else :
#             right = mid -1 
#     return -1 
# nums = [1,3,5,6,7,8,14]
# print(binary_search(nums, 9))
# def print_number(n):
#     if n == 0: 
#         return
#     print_number(n-1)
#     print(n)
# print_number(5)

# def factorial(n):
#     if n ==0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# def niilber(n):
#     if n == 0 :
#         return 0 
#     return n + niilber(n-1)
# print(niilber(5))

# def fibo(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else :
#         return fibo(n-1) + fibo(n-2)
# for i in range(6):
#     print(fibo(i), end= "")

# def reverse_string(s):
#     return s[::-1] 
# print(reverse_string("hello")) 
# class Student:
#     def __init__(self, ner, onoo):
#         self.name = ner
#         self.score = onoo
    
#     def shalgalt(self):
#         if self.score >= 60:
#             return f"{self.name} passed (Score: {self.score})"
#         else:
#             return f"{self.name} failed (Score: {self.score})"

# students = [
#     Student("B", 75),
#     Student("w", 45),
#     Student("S", 90),
#     Student("a", 59),
#     Student("T", 60)
# ]

# for s in students:
#     print(s.shalgalt())



# class Teacher:
#     def __init__(self, name):
#         self.name = name

#     def teach(self):
#         print (f"Teacher {self.name} is teaching")

# bagsh = Teacher("nigga")
# bagsh.teach()
# class Shape:
#     def area(self):
#         pass 


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
       
#         return 3.14 * (self.radius ** 2)


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Square(Rectangle): 
#     def __init__(self, side):
#         super().__init__(side, side)
# sq = Square(7)
# print("Square area:", sq.area())