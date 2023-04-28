

CREATE TABLE "Database" (
	id TEXT NOT NULL, 
	name TEXT, 
	named_thing_set TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Information" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_input) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(has_output) REFERENCES "NamedThing" (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
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
