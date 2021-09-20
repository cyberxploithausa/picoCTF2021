#!/usr/bin/env python3

import base64


a = 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'

b = base64.b64decode(a)
print(b)
