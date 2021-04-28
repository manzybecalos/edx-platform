#!/usr/bin/python
# Testing encoding on second line does not cause violation
message = "<script>alert('XSS');</script>"
x = f"<string>{message}</strong>"
