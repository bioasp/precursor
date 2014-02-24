% TODO:
% add rules for reversible reactions to minimality check

% choose a set of seed from the possible seeds
seed(X) :- ubi(X).
{ seed(X) } :- pseed(X), not ubi(X).

% a reaction is applied if all reactants are available
areaction(R) :- available(M) : reactant(M,R), reaction(R).
areaction(R) :- available(M) : product(M,R), reaction(R), reversible(R).
% otherwise its inactive
ireaction(R) :- reaction(R), not areaction(R).


% a metabolite is available if it is given as a seed or if it is the product of an applied reaction
available(X) :- seed(X).
available(X) :- product(X,R), areaction(R).
available(X) :- reactant(X,R), areaction(R), reversible(R).


reach(X) :- seed(X).
reach(X) :- product(X,R), reactant(Y,R), reach(Y).
reach(X) :- reactant(X,R), product(Y,R), reach(Y), reversible(R).

% a metabolite might be available or not
{ available(X) } :- reach(X). 


% atleast one reaction must be producing X
% if all are inactive it is not a solution 
is_produced(X) :- areaction(R), product(X,R).
is_produced(X) :- reactant(X,R), areaction(R), reversible(R).
:- not is_produced(X), available(X), not seed(X).
%:- ireaction(R) : product(X,R), available(X), not seed(X).
 

% there must be a path from a seed to the available metabolite
founded(X) :- seed(X).
founded(X) :- product(X,R), reactant(Y,R), areaction(R), founded(Y).
founded(X) :- reactant(X,R), product(Y,R), areaction(R), founded(Y), reversible(R).

:- available(X), not founded(X).

% every target must be available
:- target(X), not available(X).

new_seed(X):- seed(X), not ubi(X).


% check subset-minimality 

 % which metabolites depend on a pseed 
 dep(S,S) :- pseed(S).
 dep(X,S) :- product(X,R), depreaction(R,S).

 % a reaction depends on a pseed if one reactant depend on the pseed
 depreaction(R,S) :-  dep(M,S), reactant(M,R), reaction(R).

 % a metabolite can be available without a seed if it can be product of a reaction that does not depend on the seed
 indep(M,S) :- dep(M,S2), product(M,R), indepreaction(R,S).

 % a reaction is independent of a seed if all reactants depend on something else
 indepreaction(R,S) :-  S!=T: dep(M,T) : reactant(M,R), areaction(R), seed(S).

:-  indep(T,S) : target(T), seed(S).



#hide.
#show new_seed/1.
%#show indep(M,S).
%#show dep(M,S).
%#show indepreaction(R,S).