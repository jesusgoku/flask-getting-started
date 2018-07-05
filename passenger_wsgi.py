import sys, os

HOME = os.environ.get('HOME')

VENV = HOME + '/.virtualenvs/flask-getting-started-NtFYFTn8'
PYTHON_BIN = VENV + '/bin/python3'

if sys.executable != PYTHON_BIN:
    os.execl(PYTHON_BIN, PYTHON_BIN, *sys.argv)

sys.path.insert(0, '{v}/lib/python3.5/site-packages'.format(v=VENV))

from app import app as application
