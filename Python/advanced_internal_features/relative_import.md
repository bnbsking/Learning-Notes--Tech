# Introduction
+ Definition
	+ Package: a folder contains `__init__.py`
	+ Module: `xxx.py` in a package


# File structure example
+ assume `a.py` want to use sth in `b.py`
```bash
a/
	__init__.py  # content: from b import hello; from .a import hi
	a.py         # content: from . import hello; hi=hello+1

b/
	__init__.py  # content: from .b import hello
	b.py         # content: hello=2

main.py          # content: from a import hi; print(hi)  # 3
```

+ for relative import, both `__init__.py` and module cannot be executed directly! so `main.py` is needed.

+ if one wants to execute module:
```bash
python -m a.a  # folder use `.` instead of `/`, and no more `.py` extension!
```
