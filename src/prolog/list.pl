% last element in list

last_member(X, [X]).
last_member(X, [_|TAIL]) :- last_member(X, TAIL).

% number of elements in the list

list_length(0, []).
list_length(N, [_|TAIL]) :- list_length(N1, TAIL), N is N1 + 1.

% check if element is member of list

member(X, [X|_]).
member(X, [_|TAIL]) :- member(X, TAIL).

% append one list to another, forming a third

append([], L, L).
append([X1|L1], L2, [X1|L3]) :- append(L1, L2, L3).

% insert element into list at last index

insert_last(APPEND, LIST, RESULT) :- append(LIST, [APPEND], RESULT).
