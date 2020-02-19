man(marcus).
man(jaan).

pompay_liver(marcus).
pompay_liver(francesco).


born(marcus,40).
born(jaan,1977).
born(francesco,1989).
person_death_year(marcus,78).

volcanic_eruption_age(78).
maximum_age(150).
year_now(2019).

mortal(X):-
	man(X).

is_dead_by_age(X):-
 born(X,U), year_now(O), N is O - U, N > 150.

 %--------use this rule to check if person is dead----------------------
 %--------for examle man_is_dead(marcus).
 
man_is_dead(X):-
	mortal(X), ((pompay_liver(X), born(X,A), A < 78); person_death_year(X,_); is_dead_by_age(X)), !.