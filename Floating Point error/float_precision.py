import sys
import pandas as pd
import logging
from datetime import datetime

# date_suffix helps make a unique log file for everyday
date_suffix = datetime.today().strftime('%d%m%Y')

# Configuring the logging object
LOG_FILENAME = 'NULL_remove.out.' + date_suffix + '.log'
LOG_FORMAT = "%(levelname)8s | %(asctime)25s  | %(message)s"
LOG_LEVEL = logging.DEBUG
logging.basicConfig(filename=LOG_FILENAME,
					level=LOG_LEVEL,
					format=LOG_FORMAT)
logger = logging.getLogger()

try:
	logger.info('## PROGRAM START ## ') 
	csv_file = sys.argv[1]
	logger.debug('Arguments: ' + str(sys.argv))
	with open(csv_file) as file_check:
		source_encoding = file_check.encoding 
	# the df_simple_read DataFrame reads the csv file with default parameters.
  df_simple_read = pd.read_csv(csv_file)
  
  # The df_precise DataFrame reads the csv file with float_precision='round_trip'
  df_precise = pd.read_csv(csv_file, float_precision='round_trip')

	logger.info('Read File "'+ csv_file +'" : Success') 
		
  # Saving the DataFrame to a different csv file
	df_simple_read.to_csv('(df_simple_read) Sacramentorealestatetransactions.csv', index=False)
	df_precise.to_csv('(df_precise) Sacramentorealestatetransactions.csv', index=False)
  
except Exception:
	logger.error('ERROR', exc_info=True)
