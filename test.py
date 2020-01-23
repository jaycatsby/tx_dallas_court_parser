from dallasparser.parser import TXDallasParser
import sys
import os

TEST_HTML_PATH = os.path.join(os.getcwd(), 'html')
TEST_OUTPUT_PATH = os.path.join(os.getcwd(), 'data')

if __name__=='__main__':
	test = TXDallasParser(TEST_HTML_PATH, TEST_OUTPUT_PATH)
	test.run()
