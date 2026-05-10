transaction addFemale ( F: humans ) {
	register F;
	insert (F) into person;
	insert (F) into female;
}


transaction addMale ( M: humans ) {
	register M;
	insert (M) into person;
	insert (M) into male;
}


transaction addCouple ( P1: humans, P2: humans ) {
	register P1;
	register P2;
	insert (P1) into person;
	insert (P2) into person;
	insert (P1, P1) into likes;
	insert (P2, P2) into likes;
	insert (P1, P2) into likes;
}


transaction addPerson ( P: humans ) {
	register P;
	insert (P) into person;
}


transaction addLike ( P1: humans, P2: humans ) {
	register P1;
	register P2;
	insert (P1) into person;
	insert (P2) into person;
	insert (P1, P1) into likes;
	insert (P1, P2) into likes;
}


