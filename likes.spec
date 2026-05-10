transaction addPerson(P: humans) {
  register P;
  insert (P) into person;
}

transaction addFemale(F: humans) {
}

transaction addMale(M: humans) {
  register M;
  insert (M) into male;
}

transaction addCouple(P1: humans, P2: humans) {
}
