lucas(0, 2) :- !.
lucas(1, 1) :- !.
lucas(N, R) :-
    N > 1,
    N_Pre is N - 1,
    N_PrePre is N - 2,
    lucas(N_Pre, LHS),
    lucas(N_PrePre, RHS),
    R is LHS + RHS.

% Generate List
seq(M, Result) :-
    numlist(0, M, List),
    maplist(lucas, List, Result).
