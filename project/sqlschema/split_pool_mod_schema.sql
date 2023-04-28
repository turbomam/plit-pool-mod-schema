

CREATE TABLE "Database" (
	named_thing_set TEXT, 
	material_entity_set TEXT, 
	PRIMARY KEY (named_thing_set, material_entity_set)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
