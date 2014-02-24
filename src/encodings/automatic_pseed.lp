product(X) :- product(X,R). 
product(X) :- reactant(X,R), reversible(R).

pseed(X):- reactant(X,R), not product(X), can_reach(X).

two_reactions(X) :- reactant(X,R), reactant(X,R2), R!=R2.
two_reactions(X) :- reactant(X,R), product(X,R2), R!=R2.
two_reactions(X) :- product(X,R), product(X,R2), R!=R2.

pseed(X) :- reactant(X,R), not two_reactions(X), reversible(R), can_reach(X).
pseed(X) :- product(X,R), not two_reactions(X), reversible(R), can_reach(X).


can_reach(X) :- target(X).
can_reach(X) :- reactant(X,R), product(P,R), can_reach(P) .
can_reach(X) :- product(X,R), reactant(P,R), reversible(R), can_reach(P) .


#hide.
#show pseed(X).