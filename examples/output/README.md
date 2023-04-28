## Database-minimal
### Input
```yaml
named_thing_set:
- description: this is the first named thing
  id: example:Nt001
  name: first named thing
- description: this is the second named thing
  id: example:Nt002
  name: second named thing

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
