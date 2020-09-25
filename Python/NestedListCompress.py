if __name__ == '__main__':
    score_sheet=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        score_sheet.append([name,score])

    second_highest=sorted(list(set([marks for name,marks in score_sheet])))[1]

    print('\n'.join([a for a,b in sorted(score_sheet) if b == second_highest]))

        
