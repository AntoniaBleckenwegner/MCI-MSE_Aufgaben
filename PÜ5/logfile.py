import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

logger = logging.getLogger()

logger = logging.getLogger()

logger.info("INFOOOOOOO")
#Testing our Logger

