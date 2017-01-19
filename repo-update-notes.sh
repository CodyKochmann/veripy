# these are notes on how to update the repo on pypi

echo 'dont actually run this file'
exit

# make sure you update your README and setup.cfg
# to the current date.

# update the remote repo
git add .
git commit -m "yourmessage"
git push origin master

# tag the current repo
git tag 0.1 -m "changes to this version"
git push --tags origin master

# send the repo to the test server
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

# send the repo to the main server
python setup.py register -r pypi
python setup.py sdist upload -r pypi
