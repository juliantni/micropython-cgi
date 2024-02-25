import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup


setup(name='micropython-uasyncio',
      version='0.6.1',
      description='uasyncio module for MicroPython',
      long_description='Lightweight asyncio-like library built around native Python coroutines, not around un-Python devices like callback mess.',
      url='https://github.com/micropython/micropython/issues/405',
      author='Paul Sokolovsky',
      author_email='micro-python@googlegroups.com',
      maintainer='MicroPython Developers',
      maintainer_email='micro-python@googlegroups.com',
      license='MIT',
      py_modules=['uasyncio'],
      install_requires=['micropython-heapq', 'micropython-errno', 'micropython-select', 'micropython-logging'])
