#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

class Jira(object):

	def run(self):
		
		name = raw_input('Input user name you want to seach:').lower()
		if len(name) < 1 :
			print "name can't be null"
			exit()
		elif not re.match('[a-zA-Z]+\.[a-zA-Z]+', name):
			print "name should follow the rule: firstname.lastname"
			exit()

		
		url = "https://jira.xxxxx.com/rest/api/latest/search"
		param = {'jql':'assignee in ("{0}@xxxxx.com")'.format(name)}
		headers = {'Authorization': 'Basic base64(username:password)', 'Content-Type': 'application/json'}

		r = requests.get(url, params=param, headers=headers)
		result = r.json()
		ticket_number = result['total']

		if ticket_number == 0:
			print "Sorry, Not Found User {0} !".format(name)
		else:
			print "User {0} has {1} ticket{2} .".format(name, ticket_number, 's' if ticket_number>1 else '') 
		

if __name__ == '__main__':
	f = Jira()
	f.run()
