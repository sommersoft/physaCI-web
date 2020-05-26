# The MIT License (MIT)
#
# Copyright (c) 2020 Michael Schroeder
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import os
import pathlib

import requests

from flask import Flask, render_template, request, url_for, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

with app.test_request_context():
    url_for('static', filename='physaci.css')
    url_for('static', filename='job_results.css')
    url_for('static', filename='oops.css')
    url_for('static', filename='index.css')
    url_for('static', filename='color_pallet.css')
    url_for('static', filename='images/physa_silhouette_two_color.png')
    url_for('static', filename='scripts/result_viewer.js')

@app.errorhandler(HTTPException)
def handle_oopsie(e):
    error_info = {
        'status_code': e.code,
        'name': e.name,
        'description': e.description
    }
    return render_template('oops.html', **error_info), e.code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/job')
def job_result():
    node = request.args.get('node')
    job_id = request.args.get('job-id')

    if node is None or job_id is None:
        abort(400, description='Missing required parameters.')

    job_data = requests.get(
        f'{os.environ["PHYSACI_JOB_RESULT_URL"]}?node={node}&job-id={job_id}'
    )
    if job_data.ok:
        return render_template('physaci_results_page.html', **job_data.json())
    else:
        if 'application/json' in job_data.headers.get('Content-Type', ''):
            error_info = job_data.json()
            description = error_info.get(
                'failure_reason',
                'Error retrieving information.'
            )
            abort(job_data.status_code, description=description)
        else:
            abort(500)
