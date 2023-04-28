## Database-heterogeneous
### Input
```yaml
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
process_set:
- description: this is the first Process
  id: example:Proc001
  name: first Process
- description: this is the second Process
  id: example:Proc002
  name: second Process

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
## DatabaseCollection-no-id
### Input
```yaml
age_in_years: 33
name: foo bar
primary_email: foo.bar@example.com

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
