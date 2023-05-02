## Database-heterogeneous
### Input
```yaml
id: example:db1
information_set:
- description: this is the first Information
  id: example:Info001
  name: first Information
- description: this is the second Information
  id: example:It002
  name: second Information
material_entity_set:
- description: this is the first MaterialEntity
  id: example:Me001
  name: first MaterialEntity
- description: this is the second MaterialEntity
  id: example:Me002
  name: second MaterialEntity
name: example database
process_set:
- description: this is the first Process
  id: example:Proc001
  name: first Process
- description: this is the second Process
  id: example:Proc002
  name: second Process

```
## Database-neon-example
### Input
```yaml
id: example:db1
information_set:
- id: BIOPROJECT:PRJNA406974
  name: empty/invalid bioproject claimed by neon
material_entity_set:
- description: intended for sequencing and metagenomic analysis
  id: NEON_SAMP_VIEW:YELL_046-M-4.5-0.5-20191002-GEN-DNA2
  name: extracted dna from neon soil sample
name: example database
process_set:
- has_input: NEON_SAMP_VIEW:YELL_046-M-4.5-0.5-20191002-GEN-DNA2
  has_output: BIOPROJECT:PRJNA406974
  id: example:SampleNeonSoilMetagenomeSequencing
  name: Sequencing of soil from Yellowstone

```
## DatabaseCollection-no-id
### Input
```yaml
age_in_years: 33
name: foo bar
primary_email: foo.bar@example.com

```
## DatabaseCollection-dupe-ids
### Input
```yaml
entries:
- id: example:Database001
  name: foo bar
- id: example:Database001
  name: foo bar
  undefined: undefined

```
## DatabaseCollection-bad-id-pattern
### Input
```yaml
entries:
- id: example_Person001
  name: foo bar
- id: example_Person002
  name: foo bar

```
## DatabaseCollection-undefined-slot
### Input
```yaml
entries:
- id: example:Database001
  name: foo bar
- id: example:Database002
  name: foo bar
  undefined: undefined

```
