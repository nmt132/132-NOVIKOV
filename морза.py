a = "abwgdevijklmnoprstufhcqx"
abc = list(a)
print(abc)
b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
abcm=b.split()
print(abcm)
abcm=b.split()
text=input("Введите текст на английском: ")
indm=""
for i in range (len(text)):
    ind = abc.index(text[i])
    indm=indm + abcm[ind] 
print(f"{indm}")

