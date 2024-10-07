if __name__ == '__main__':
    n = int(input("Number of students : "))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks)
    query_name = input("Name of student : ")
    total_mark = 0
    for s_name,s_marks in student_marks.items():
        if query_name == s_name:
            for new_mark in s_marks:
                total_mark += new_mark
                average_mark = total_mark / len(s_marks)
            print(f"Average mark of {s_name} is {"%.2f" % average_mark}")
    