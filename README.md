# Scripps_ES

Create index data from Harvard Dataverse and make them searchable by ID or keyword in the field

## Install guide

### Clone the repo

```
$ git clone https://github.com/soominl/Scripps_ES.git
$ cd Scripps_ES
```

### Install dependencies

```
$ pip install -r requirements.txt
```

### Run the script

```
$ FLASK_APP=query_script.py flask run
```

## Querying data

### Using specific dataset identifier (e.g., "https://doi.org/10.11588/data/0HJAJS")

```
localhost:5000/search/id/?id=https://doi.org/10.11588/data/0HJAJS
```

### Using specific field in the JSON object (e.g., datasets with "Earth and Environmental Sciences" in the keywords).

```
localhost:5000/search/?field=keywords&value=Earth and Environmental Sciences
```


