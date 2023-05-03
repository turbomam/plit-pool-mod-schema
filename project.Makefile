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

# how to make this easy to open in desktop or withing HG web browser, with Mermaid rendering?
examples/output/Database-neon-example.html: src/data/examples/valid/Database-neon-example.yaml
	$(RUN) linkml-render \
	--schema src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml \
	--config renderer-include-mermaid-conf.yaml \
	--output-format html \
	--output $@ $<

examples/output/neon-merged.json:
	robot merge \
		--input project/owl/split_pool_mod_schema.owl.ttl \
		--input examples/output/Database-neon-example.ttl \
		--output $@

examples/output/neon-merged.ttl:
	robot merge \
		--input project/owl/split_pool_mod_schema.owl.ttl \
		--input examples/output/Database-neon-example.ttl \
		--output $@

examples/output/neon-merged.png: examples/output/neon-merged.json
	$(RUN) og2dot $< \
		--outfile $@ \
		-s test-ogv-style.json \
		--to png $<


xxx: examples/output/neon-merged.ttl
#	$(RUN) runoak \
#		--verbose \
#		--input $< labels .all
#	$(RUN) runoak \
#		--verbose \
#		--input $< leafs
#	$(RUN) runoak \
#		--verbose \
#		--input $< roots
#	$(RUN) runoak \
#		--verbose \
#		--input $< relationships 'NamedThing'
#	$(RUN) runoak \
#		--verbose \
#		--input $< siblings 'Information'
#	$(RUN) runoak \
#		--verbose \
#		--input $< tree 'Information'
	$(RUN) runoak \
		--input $< viz -p t,p,i 'empty/invalid bioproject claimed by neon'

# # # #

neon_samples:
	$(RUN) neon-dl-sample-by-tag-or-tags by-tag \
		--sample-tag "YELL_052-M-20200709-COMP" \
		--get-relatives \
		--dest-dir $@ \
		--api-token eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJNQU1AbGJsLmdvdiIsInNjb3BlIjoicmF0ZTpwdWJsaWMiLCJpc3MiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnLyIsImV4cCI6MTg0MDYzMTY3MywiaWF0IjoxNjgyOTUxNjczLCJlbWFpbCI6Ik1BTUBsYmwuZ292In0.H0P7ke_WL7syECGAA4khEddZ8f6sR__vA3TFherLVt8I1omtYNjspqwWZh42ZkoCbCmRTIr4b4OG8uqPhICv8g

#instantiate-samples:
#	$(RUN) instantiate-samples instantiate \
#		--destination-file neon-notes/Database.yaml \
#		--materialize-generic-processes \
#		--neon-yaml-dir neon_samples \
#		--schema-file src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml

neon-notes/one_compound_soil_metagenome.yaml: src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml neon_samples
	$(RUN) python src/split_pool_mod_schema/datamodel/inst_samps.py instantiate \
		--destination-file $@ \
		--no-materialize-generic-processes \
		--neon-yaml-dir $(word 2, $^) \
		--schema-file $<

neon-notes/one_compound_soil_metagenome.ttl: src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml \
neon-notes/one_compound_soil_metagenome.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--schema $^


neon-notes/one_compound_soil_metagenome_with_ontology.ttl: neon-notes/one_compound_soil_metagenome.ttl \
project/owl/split_pool_mod_schema.owl.ttl
	robot merge \
		--input $(word 1, $^) \
		--input $(word 2, $^) \
		--output $@