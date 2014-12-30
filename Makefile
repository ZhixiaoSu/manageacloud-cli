clean:
	rm -rf venv
	find . -name '*.pyc ' -delete

prepare:clean
	set -ex
	virtualenv venv -p /usr/bin/python2.7
	venv/bin/pip install -r requirements.txt
	#venv/bin/pip install .

