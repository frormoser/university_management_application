def listCourses(courses):
    print("Courses: ")
    counter = 1
    for cur in courses:
        data = "{0}. Código: {1} | Nombre: {2} ({3} Créditos)"
        print(data.format(counter, cur[0], cur[1], cur[2]))
        counter = counter+1
    print(" ")
