%

vertex('A1').
vertex('A2').
vertex('A3').
vertex('A4').

hasDescription('A1', 'Event 1').
hasDescription('A2', 'Event 2').
hasDescription('A3', 'Event 3').
hasDescription('A3', 'Event 4').

hasActor('A1', 'Actor 1').
hasActor('A2', 'Actor 2').
hasActor('A3', 'Actor 3').
hasActor('A4', 'Actor 4').

hasOccurrenceVertex('A1', 4).
hasOccurrenceVertex('A2', 11).
hasOccurrenceVertex('A3', 2).
hasOccurrenceVertex('A4', 2).

edge('A1', 'A2', 5). %il terzo parametro costituisce le occorrenze dell’arco
edge('A2', 'A3', 1).
edge('A3', 'A1', 1).

edge(node(Name1, _, _, _), node(Name2, _, _, _), EdgeOcc)
  :- edge(Name1, Name2, EdgeOcc).
edge(node(Name1, _, _, _), node(Name2, _, _, _), EdgeOcc)
  :- edge(Name2, Name1, EdgeOcc).

node(Name, Event, Actor, Occ) :-  vertex(Name),
                                  hasDescription(Name, Event),
                                  hasActor(Name, Actor),
                                  hasOccurrenceVertex(Name, Occ).

