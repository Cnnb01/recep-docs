# recep-docs

## Load test data

From `prep/Backend`, run:

```bash
python manage.py migrate
python manage.py loaddata seed_data
```

The fixture creates patients, doctors, and appointments with pending, completed,
and cancelled statuses. The configured database must be available before loading
the fixture.
