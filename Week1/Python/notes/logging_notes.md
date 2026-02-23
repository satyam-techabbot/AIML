# Logging in Python

Logging in Python lets you record important information about your program’s execution. You use the built-in logging module to capture logs, which provide insights into application flow, errors, and usage patterns.

## Starting With Python’s Logging Module
The logging module in Python’s standard library is a ready-to-use, powerful module that’s designed to meet the needs of beginners as well as enterprise teams.

```
import logging
logging.warning("Remain calm!")
```

### Log level
```
Log Level	    Function	        Description

DEBUG	        logging.debug()	    detailed information that’s valuable. Numeric Value: 10

INFO	        logging.info()	    general info about what’s going on with program. Numeric Value: 20

WARNING	        logging.warning()	Indicates that there’s something you should look into. Numeric Value: 30

ERROR	        logging.error()	    Alerts you to an unexpected problem in program.  Numeric Value: 40

CRITICAL	    logging.critical()	serious error has occurred & may have crashed app.  Numeric Value: 50

NOTSET	        logging.NOTSET	    No level set; delegates to parent or logs all if root.  Numeric Value: 0
```

Example:
```
logging.debug("This is a debug message")

logging.info("This is an info message")

logging.warning("This is a warning message")

logging.error("This is an error message")

logging.critical("This is a critical message")
```

Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels.

## Adjusting the Log Level
To set up your basic logging configuration and adjust the log level, the logging module comes with a basicConfig() function.

```
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged.")
```

## Formatting the Output
By default, logs contain the log level, the logger’s name, and the log message.

```
import logging
logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
logging.warning("Hello, Warning!")
```

You can choose one of these three styles of your format string by specifying the style parameter. The options for style are "%", "$", or "{". When you provide a style argument, then your format string must match the targeted style. Otherwise, you’ll receive a ValueError.

```
import logging
logging.basicConfig(
    level=50,
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:%M",
)
logging.error("Something went wrong!")
logging.critical("Something went critical!")
```

## Logging to a File
To save your logs in a file, you can set up your logger’s basicConfig() with the filename argument.

You must provide a filepath. It’s also good practice to set an encoding and the mode the file should be opened in.

```
import logging

logging.basicConfig (
    filename="app.log", 
    encoding="utf-8", 
    filemode="a", 
    format="{asctime} - {levelname} - {message}", 
    style="{", 
    datefmt="%Y-%m-%d %H:%M", 
    level=0
)

logging.warning("This is a debug log full_path")
```

## Capturing Stack Traces
using 'exc_info=True' as arg in log function or by logging.exception(arg)

```
import logging
logging.basicConfig(
    filename="error.log", 
    encoding="utf-8", 
    filemode="a", 
    format="{asctime} - {levelname} - {message}", 
    style="{", 
    datefmt="%Y-%m-%d %H:%M", 
    level=0
)

try:
    a = 1/0
except ZeroDivisionError as e:
    logging.error(e, exc_info=True)
```
OR
```
import logging
try:
    a = 1/0
except ZeroDivisionError as z:
    logging.exception(z)
```

## Creating a Custom Logger

The default logger named root, which is used by the logging module whenever functions like logging.debug(), logging.warning(), and so on are called.

The downside of working with the root logger directly is that the configuration can be cumbersome as you’re relying on a single basicConfig(). For bigger projects, you’ll need more flexibility for your logging needs.

### Instantiating Your Logger
You can instantiate a Logger class by calling the logging.getLogger() function and providing a name for your logger.

```
import logging
logger = logging.getLogger(__name__)
logging.warning(f"logger {logger}")
```

### Using Handlers
Handlers come into the picture when you want to configure your own loggers. Handlers send your logs to the output destination you define like console(standard output stream) using StreamHandler class or file using FileHandler class.

```
import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler() # creating console handler
file_handler = logging.FileHandler("log_file.log", mode="a", encoding="utf-8") # creating file handler

logger.addHandler(console_handler) # adding handler to logger
logger.addHandler(file_handler)

logger.handlers # fetching added handlers

logger.warning("Watch Out") # calling logs
```

> RotatingFileHandler: creates a new log file once a file size limit is reached

> TimedRotatingFileHandler: you can create a new log file for defined intervals.

### Adding Formatters to Your Handlers
With a formatter, you can control the output format by specifying a string format as you did before with the format argument of logging.basicConfig().

```
import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log_file.log", mode="a", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%d/%m/%Y %H:%M:%S",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.warning("Watch Out")
```

### Setting the Log Levels of Custom Loggers
This is useful when you want to set multiple handlers for the same logger but want different severity levels for each.

The default log level of your custom logger is 0, which stands for NOTSET.

```
logger.getEffectiveLevel() # gives 30

logger.setLevel(logging.DEBUG) 
# logger.setLevel(10)
# logger.setLevel("DEBUG")
```

### Filtering Logs
There are three approaches to creating filters for logging. You can create a:
- Subclass of logging.Filter() and overwrite the .filter() method
- Class that contains a .filter() method
- Callable that resembles a .filter() method

For the subclass and class, .filter() must accept a log record and return a Boolean.

The callable can be a basic function with one parameter for the log record that your handler passes in. The return value must be a Boolean. Most convinient way.

```
# using callable
import logging

def get_only_debug(record):
    return record.levelname == "ERROR"

logger1 = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
console_handler.addFilter(get_only_debug)

logger1.addHandler(console_handler)

logger1.error("This is error")
logger1.critical("This is CRITICAL")
logger1.debug("This is debug")
logger1.info("This is info")
```

```
# using class
class NoParsingFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith('parsing')

logger.addFilter(NoParsingFilter())
```






