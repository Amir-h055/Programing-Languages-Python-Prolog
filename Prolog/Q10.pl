

every-other([], []).
every-other([X], [X]).
every-other([X, _ | T], [X | Y]) :- every-other(T, Y).