if __name__ == '__main__':
    n = int(input())
    student_marks = {}                                #initialising a dictionary to be Empty
    for _ in range(n):
        name, *score_to_be_entered = input().split()       ##means that beside every name I want to input scores of the student
        scores = list(map(float, score_to_be_entered))      #every score String I entered, I simply want that score to be converted in to float
        student_marks[name] = scores                         #means that beside every name I want to display scores of the student
    query_name = input()                                    #user can choose any student from above/key and input its name
    query_score=student_marks[query_name]                         # so that its score will be displayed

    print("{0:.2f}".format(sum(query_score)/(len(query_score))))                       #average with two decimal value
