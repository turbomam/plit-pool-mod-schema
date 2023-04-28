

CREATE TABLE "Database" (
	named_thing_set TEXT, 
	PRIMARY KEY (named_thing_set)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
