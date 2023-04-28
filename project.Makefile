## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example run-linkml-validation

check-jsonschema-example: project/jsonschema/split_pool_mod_schema.schema.json \
	  src/data/examples/invalid/DatabaseCollection-undefined-slot.yaml
	# showing ignore failures here
	# this should be templated
	- $(RUN) check-jsonschema \
	  --schemafile $^

run-linkml-validation: src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml \
src/data/examples/invalid/DatabaseCollection-undefined-slot.yaml
	# PersonCollection is assumed as the target-class because it has been defined as the tree_root in the schema
	- $(RUN) linkml-validate \
	  --schema $^


src/data/dh_vs_linkml_json/DatabaseCollection_linkml_raw.yaml: src/data/dh_vs_linkml_json/Database_dh.json
	$(RUN) dh-json2linkml \
		--input-file $< \
		--output-file $@ \
		--output-format yaml \
		--key entries


src/data/dh_vs_linkml_json/DatabaseCollection_linkml_normalized.yaml: src/data/dh_vs_linkml_json/DatabaseCollection_linkml_raw.yaml
	$(RUN) linkml-normalize \
		--schema src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml \
		--output $@ \
		--no-expand-all $<

src/data/dh_vs_linkml_json/entries.json: src/data/dh_vs_linkml_json/DatabaseCollection_linkml_normalized.yaml
	$(RUN) linkml-json2dh \
		--input-file $< \
		--input-format yaml \
		--output-dir $(dir $@)

project/reports/slot_usage_esp_validation.tsv:
	linkml2sheets \
		--schema src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml \
		--output $@ \
		src/local_schemasheets/templates/slot_usage_esp_validation.tsv
