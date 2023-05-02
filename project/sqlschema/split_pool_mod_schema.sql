

CREATE TABLE "Database" (
	id TEXT NOT NULL, 
	name TEXT, 
	material_entity_set TEXT, 
	named_thing_set TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DnaSamplePrepComposite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "DnaSamplePrepSimple" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "GeneticSamplePrep" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "Information" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MicDnaExtractionInSoilDnaSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MicDnaExtractionInSubsample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MmsMetagenomeSequencingInProcessedSeqFileName" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MoistureSamplePrep" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "PhSamplePrep" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "Pooling" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "Sequencing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsMetagenomicsPoolingInCompositeSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticArchiveSample1" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticArchiveSample2" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticArchiveSample3" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticArchiveSample4" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticArchiveSample5" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInGeneticSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilCoreCollectionInSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilMoistureInMoistureSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SlsSoilpHInPhSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	neon_sample_class TEXT, 
	neon_sample_tag TEXT, 
	neon_sample_uuid TEXT, 
	has_children TEXT, 
	has_parents TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "SubsampleDnaExtract" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_inputs TEXT, 
	has_outputs TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);
