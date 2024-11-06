# Introduction
+ installation
```bash
pip install logging
```

+ usage
```python
logger = logging.getLogger("main") # Initialize a logger
handler = logging.FileHandler(loggerPath) # Initialize a handler 
consoleHandler = logging.StreamHandler()

log_format = logging.Formatter(fmt, datefmt) # log information. 
logging.setLevel(level)  # level: logging.DEBUG < INFO < WARNING < ERROR
logger.addHandler(handler)  # sync
logger.addHandler(consoleHandler)  # sync
```

+ concepts

| object | class | role | description |
| - | - | - | - |
| logger | <class 'logging.Logger'> | brain | records log in the brain |
| file handler | <class 'logging.FileHandler'> | hand | write from brain to diary |
| stream handler | <class 'logging.StreamHandler'> | hand | output to screen |