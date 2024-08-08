from flask import Blueprint
from flask import Blueprint, jsonify, request, jsonify, send_file
import os
import json
import numpy as np
import utils.logging_utils as logging_utils

logger = logging_utils.setup_logger('jira_searcher')
import time
from datetime import datetime, timedelta
import service.jira_service as jira_service

jira_searcher_pb = Blueprint("jira_searcher", __name__)



@jira_searcher_pb.route('/search_jira', methods=['GET'])
def search_jira():
    user_input = request.args.get('query')

    query_type = request.args.get('query_type')
    logger.info("query type" + query_type + " query:" + user_input)
    if query_type == 'Jira-ID':
        summary, descprition = jira_service.find_summary_and_description(user_input)
        user_input = summary + " "+ descprition

    results = jira_service.find_top_similar_jira(user_input)

    return jsonify({'similarJiras':results})
