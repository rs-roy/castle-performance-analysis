import logging 

logging.basicConfig(filename="execution_time.log", format='%(asctime)s %(levelname)s - %(message)s', datefmt= '%Y/%m/%d %I:%M:%S %p', filemode='a')                    
                    
logger=logging.getLogger() 
logger.setLevel(logging.INFO)