from src.ML_Project.logger import logging
import sys
from src.ML_Project.exception import CustomException
if __name__=="__main__":
    logging.info("The execution has started")
    try:
        a=1/0
    except Exception as e:
        logging.info("Customer Exception : ")
        raise CustomException(e,sys)
