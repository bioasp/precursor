%precheck: check if given all pseeds it is possible to produce the targets

% choose a set of seed from the possible seeds
seed(X)  :- ubi(X).
seed(X)  :- pseed(X).

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
%:- available(X), forbidden(X).
#hide.
