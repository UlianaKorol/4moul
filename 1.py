
#O(N*M)- помедленнее алгоритм
def strcounter(s): 
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1

        print(sym, count)

strcounter('abcadccdb')

#функция set даёт нам  не писать букву столько раз сколько она записана
#в списке. Она позволяет написать букву в выводе один раз, но числом указать сколько раз она была написана в списке

#O(N**2)-самый плохой алгоритм
def strcounter(s): 
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1

        print(sym, count)

strcounter('abcadccdb')

#O(N) - самый эффективный алгоритм
def strcounter(s):
    syms_counter = {}
    for sym in set(s):
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter('abcadccdb')

print (21)
print (21)