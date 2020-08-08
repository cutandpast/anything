history = {}

cache = ""

chrome = "0001"
lol = "0010"
maple = "0011"
youtube = "0100"

def active(count):
    global cache
    global history
    if count > 1 and history[count] == history[count-1]:
        cache = history[count]
    try:
        if count > 10:
            count2 = count-10
            del history[count2]
    except KeyError:
        pass

def cachehit(a):
    if cache == a:
        print("cachehit!")
    elif count < 3:
        print("non history")
    else:
        print("cachemiss!")

if __name__ == "__main__":
    count = 0
    while 1:
        print("1. 크롬 2. 롤 3. 메이플 4. 유튜브 9. 확인")
        choose = int(input())
        if choose == 1:
            count += 1
            history[count] = "0001"
            cachehit(chrome)
        elif choose == 2:
            count += 1
            history[count] = "0010"
            cachehit(lol)
        elif choose == 3:
            count += 1
            history[count] = "0011"
            cachehit(maple)
        elif choose == 4:
            count += 1
            history[count] = "0100"
            cachehit(youtube)
        elif choose == 9:
            print("\n",history,"\n",cache)
        active(count)
        
        
            
            
