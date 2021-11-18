from flask import current_app as app, request, jsonify
from .connector import Connector


@app.route('/')
def index():
    return jsonify()


@app.route('/list_of_companies')
def company_list():
    response = Connector.open_file_list('list_of_companies')
    return jsonify(response)


@app.route('/list_of_persons')
def person_list():
    response = Connector.open_file_list('list_of_persons')
    return jsonify(response)


@app.route('/company')
def company():
    company_pk = request.args.get('pk')

    response = Connector.open_company('company', company_pk)
    return jsonify(response)


@app.route('/person')
def person():
    person_pk = request.args.get('pk')

    response = Connector.open_person('person', person_pk)
    return jsonify(response)

