import logging
import logging.handlers

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s : %(message)s',
    filename='/home/rapa/test.log'
    )

#디폴트는 터미널에 띄워주고 , 파일적으면 파일에 로그남김

'''
logging.debug("hohoho")
logging.info("hi")

logging.warning("너 지금 납치된 거야")
logging.error("Error msg")
logging.critical("심각한 오류")
'''



savelog = logging.getLogger()
savelog.setLevel(logging.DEBUG)
formatting = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

fileHandler = logging.FileHandler('/home/rapa/test.log')
fileHandler = set.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
savelog.addHandler(fileHandler)


printlog = logging.getLogger()
printlog.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatting)
savelog.addHandler(fileHandler)


savelog.debug("hohoho")
savelog.info("hi")
savelog.warning("너 지금 납치된 거야")
savelog.error("Error msg")
savelog.critical("심각한 오류")









'''
import logging
import logging.handlers
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    LOGFILE, maxBytes=(1048576*5), backupCount=7
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
'''