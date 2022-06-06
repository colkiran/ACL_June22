

import logging

logging.basicConfig(level=logging.DEBUG, filename="errorlogs.log", filemode="a",
                    format="%(asctime)s : %(levelname)s : %(message)s : %(filename)s : %(lineno)d")

num = "0"
inv = 1

try:
    inv = 1 / num

except ZeroDivisionError as z:
    logging.critical(z)

except TypeError as t:
    logging.error(t)

except Exception as e:              # base class of all exceptions
    logging.warning(e)

else:
    logging.info(f"Inverse :{inv}")
finally:
    logging.info("Division of the number successfully done.....")