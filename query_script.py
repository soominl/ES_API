#!flask/bin/python

import flask
from elasticsearch import Elasticsearch
import json

# File path for data to index
FILE_PATH = "./harvard_dataverse.json"

# Open JSON file 
with open(FILE_PATH) as json_file:
    json_docs = json.load(json_file)
    
# Flask config
FLASK_HOST = 'localhost'
FLASK_PORT = 5000

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# ES config
ES_HOST = 'localhost'
ES_PORT = 9200
INDEX_NAME = 'sample'

es = Elasticsearch([ES_HOST], port = ES_PORT)

print("Creating '%s' index..." % (INDEX_NAME))
for doc in json_docs:
    es.index(index = INDEX_NAME, body=doc)
     




@app.route('/')
def init():
    return 'Please specify the query string.'

# View sample data 
@app.route('/sample', methods=['GET'])
def index():
    body = {
        "query": {
            "match_all": {}
        }
    }    
    res = es.search(index='sample', size=5, body=body)

    return flask.jsonify(res['hits']['hits'])



# Query by @id 
@app.route('/search/id/', methods=['GET'])
def search():
    url = flask.request.args.get('id', type = str)
    
    body={
        "query": {
            "match" : {
                "@id": url
                }
            }
        }

    
    res = es.search(index="sample", size=1, body=body)

    return flask.jsonify(res['hits']['hits'])
    

# Query by specific field and value 
@app.route('/search/', methods=['GET'])
def search_by_field_val():
    field = flask.request.args.get('field', type = str) 
    value = flask.request.args.get('value', type = str) 
    
    body={
        'query':{
            'match_phrase':{
                field:value
            }
        }
    }
    
    res = es.search(index="sample", size=5, body=body)
    
    return flask.jsonify(res['hits']['hits'])


app.run(host = FLASK_HOST, port = FLASK_PORT)
