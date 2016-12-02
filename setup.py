from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'Shorthand asserts for those who love predictable code but dont have time for writing every assert in the world.',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/PyRequire',
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1',
  keywords = ['assert', 'shorthand', 'contract', 'require'], # arbitrary keywords
  classifiers = [],
)
