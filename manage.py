import os
import subprocess
from flask.ext.script import Manager
from boilerflask import *
manager = Manager(app)


@manager.command
def server():
	extra_dirs = ['boilerflask/templates']
	extra_files = extra_dirs[:]
	for extra_dir in extra_dirs:
	    for dirname, dirs, files in os.walk(extra_dir):
	        for filename in files:
	            filename = path.join(dirname, filename)
	            if path.isfile(filename):
	                extra_files.append(filename)

	app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=int(os.environ.get('PORT', 5000)))

@manager.command
def deploy():
	call = lambda x: subprocess.check_output([x], shell=True).strip()
	original_branch = call("git rev-parse --abbrev-ref HEAD")
	call("git checkout -b deploy-throwaway")
	call("grunt production")
	call("git add ./assets.json -f") #force add since it is intentionally ignored in .gitignore
	call("git commit -m \"Add assets.json for deploy\"")
	call("git push git@heroku.com:boilerflask-test.git deploy-throwaway:master -f")
	call("git checkout %s" % original_branch)
	call("git branch -D deploy-throwaway")

if __name__ == "__main__":
    manager.run()