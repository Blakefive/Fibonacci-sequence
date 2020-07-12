while True:
    def main(i,final,check):
        final.append(final[i-1] + check)
        check = final[i-1] + check
        return final, check
    N = int(input())
    final = [1]
    check = 0
    for i in range(N-1):
        final, check = main(i,final,check)
    print(final)
    print(final[len(final)-1])
    quitcheck = ""
    quitcheck = input("게속하시겠습니다? (Y,y/N,n):")
    if quitcheck == "N" or quitcheck == "n":
        break
