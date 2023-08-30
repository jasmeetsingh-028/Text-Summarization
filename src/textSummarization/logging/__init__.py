#custom logg can be used for every project
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  #time stamp, type of logg (information logging)  #root dir of file being excecuted #message you want to add
log_dir = "logs"  #log directory
log_filepath = os.path.join(log_dir,"running_logs.log") #inside dir running_logs.log
os.makedirs(log_dir, exist_ok=True)

#logic for log

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  # log inside file
        logging.StreamHandler(sys.stdout)   #log info inside terminal
    ]
)

logger = logging.getLogger("textSummarizationLogger")

