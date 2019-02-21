import logging,os,time

class Logger(object):
	def __init__(self,logger):
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
		log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
		log_name = log_path + rq +'.log'
		fh = logging.FileHandler(log_name)
		fh.setLevel(logging.INFO)

		ch = logging.StreamHandler()
		ch.setLevel(logging.INFO)

		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	def getlog(self):
		return self.logger
