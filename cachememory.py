history = {}

cache = ""

def active(count):
    global cache
    if count-1 > 2 and history[count-1] == history[count-2]:
        cache = "0001"
    else:
        pass
    
    
if __name__ == "__main__":
    count = 0
    while 1:
        print("1. 크롬 2. 롤 3. 메이플 4. 유튜브 9. 확인")
        choose = int(input())
        if choose == 1:
            history[count] = "0001"
            count += 1
        elif choose == 2:
            history[count] = "0010"
            count += 1
        elif choose == 3:
            history[count] = "0011"
            count += 1
        elif choose == 4:
            history[count] = "0100"
            count += 1
        elif choose == 9:
            print("\n",history,"\n",cache)
        active(count)
        
        
            
            
