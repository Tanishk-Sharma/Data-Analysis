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
	df = pd.read_csv(csv_file, encoding=source_encoding, float_precision='round_trip')

	# The Column to check for null value. Checking the FIRST COLUMN only[for testing].
	COLUMN_TO_CHECK = df.columns[0]
	shape_before = df.shape
	logger.info('Read File "'+ csv_file +'" : Success') 
	
	# to remove rows containing null
	logger.debug('Inspecting column: "'+ COLUMN_TO_CHECK +'" for NULL value') 
	df = df.dropna(subset=[COLUMN_TO_CHECK])
	# to remove columns containing null, uncomment the line below
	# df = df.dropna(axis=1)
	
	shape_after = df.shape
	row_difference = shape_before[0] - shape_after[0]
	col_difference = shape_before[1] - shape_after[1]
	if row_difference or col_difference:
		logger.info('NULL value(s) detected!')
		logger.info('Removed '+ str(row_difference) +' rows, '+ str(col_difference) +' columns')
	else:
		logger.info('File does not have any NULL value(s)')
		
	df.to_csv('(target) Sacramentorealestatetransactions.csv', index=False, encoding=source_encoding)
	
except Exception:
	logger.error('ERROR', exc_info=True)
