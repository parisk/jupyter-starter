"""
Simple server scripts that spawns the Jupyter notebook server process.
"""

import subprocess


subprocess.call([
    'jupyter', 'notebook', '--no-browser', '--ip=0.0.0.0', '--port=5000',
    '--notebook-dir=../workspace'
])
