student(sam).
student(amir).
student(james).
studentID(sam, 123).
studentID(amir, 456).
studentID(james, 789).
course(comp201).
course(comp202).
course(comp203).
course(math201).
taking(sam, comp201).
taking(sam, comp203).
taking(amir, comp201).
taking(amir, math201).
taking(james,comp202).
taking(james,math201).

?-findall(X, taking(sam, X), Classes).
?-aggregate_all(count, student(X), Count).
?-findall(X, course(X), Lst), list_to_set(Lst, UniqueCourses).
?-(findall(X, course(X), Lst), list_to_set(Lst, UniqueCourses)),sort(UniqueCourses, Sorted).
?-[A,B|C] = Sorted.




?-findall(X, taking(sam, X), Classes),
aggregate_all(count, student(X), NumberofStudents),
findall(X, course(X), Lst), list_to_set(Lst, UniqueCourses),
(findall(X, course(X), Lst), list_to_set(Lst, UniqueCourses)),sort(UniqueCourses, Sorted), [A,B|C] = Sorted.
