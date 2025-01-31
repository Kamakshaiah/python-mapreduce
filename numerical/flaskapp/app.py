#!/usr/bin/env python3

from flask import Flask
import pydoop.hdfs as hdfs

app = Flask(__name__)

@app.route('/data')
def data():
	out = hdfs.load('/output/part-00000', mode='r')
	print(out)
	print(type(out)) 
	return(out) 
	
if __name__ == '__main__':
	app.run(debug=True) 
