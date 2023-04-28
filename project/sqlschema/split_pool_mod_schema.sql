

CREATE TABLE "Database" (
	information_set TEXT, 
	material_entity_set TEXT, 
	named_thing_set TEXT, 
	process_set TEXT, 
	PRIMARY KEY (information_set, material_entity_set, named_thing_set, process_set)
);

CREATE TABLE "Information" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
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

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Process_has_inputs" (
	backref_id TEXT, 
	has_inputs TEXT, 
	PRIMARY KEY (backref_id, has_inputs), 
	FOREIGN KEY(backref_id) REFERENCES "Process" (id)
);

CREATE TABLE "Process_has_outputs" (
	backref_id TEXT, 
	has_outputs TEXT, 
	PRIMARY KEY (backref_id, has_outputs), 
	FOREIGN KEY(backref_id) REFERENCES "Process" (id)
);
