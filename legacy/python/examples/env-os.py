#!/usr/bin/env python3

import os

print('Home:', os.environ['HOME'])
print('My:', os.environ.get('MY'))
print('Foo:', os.environ.get('FOO', 'default_value'))
