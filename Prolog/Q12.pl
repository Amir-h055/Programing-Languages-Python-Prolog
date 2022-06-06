start(a).


final(a).
final(e).
final(f).

arc(a,1,b).
arc(b,1,c).
arc(c,0,c).
arc(c,1,c).
arc(a,0,d).
arc(d,0,a).
arc(d,1,e).
arc(b,0,f).
arc(e,1,c).
arc(e,0,f).
arc(f,0,f).
arc(f,1,c).

find_last(X,[],X).
find_last(Q,[H|T],Q2) :- arc(Q,H,Q1),find_last(Q1,T,Q2).

is_accepted(L) :- start(Q),find_last(Q,L,Q1),final(Q1),!.

?-is_accepted([0]).
?-is_accepted([1]).
?-is_accepted([0,1]).
?-is_accepted([1,0]).
