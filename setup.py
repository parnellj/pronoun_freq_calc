try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Pronoun Frequency Calculator',
	'version': '0.1',
	'url': 'https://github.com/parnellj/pronoun_freq_calc',
	'download_url': 'https://github.com/parnellj/pronoun_freq_calc',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Analyzes the frequency of pronouns in State of the Union addresses over time (NLTK exercise).',
	'long_description': 'Analyzes the frequency of pronouns in State of the Union addresses over time (NLTK exercise).',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['pronoun_freq_calc'],
	'scripts': []
}
	
setup(**config)
