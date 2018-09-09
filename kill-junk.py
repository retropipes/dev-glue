# Imports
import os
import re
import os.path
import argparse

# Filename patterns to be considered junk
junk_names = list()
junk_names.append(re.compile(r'^\._.+'))
junk_names.append(re.compile(r'^\.DS_Store$'))
junk_names.append(re.compile(r'^\.AppleDouble$'))
junk_names.append(re.compile(r'^\.LSOverride$'))
junk_names.append(re.compile(r'^(eh)?[Tt]humbs(_vista)?\.db$'))
junk_names.append(re.compile(r'^[Dd]esktop\.ini$'))

# Argument parser
parser = argparse.ArgumentParser(description='Remove OS-generated junk files.')
parser.add_argument('--top', default=os.getcwd())

# Main function
def main(top):
	for root, dirs, files in os.walk(top):
		for file in files:
			for junk in junk_names:
				if junk.match(file):
					os.remove(os.path.join(root, file))

# Kickstarter
if __name__ == '__main__':
	args = parser_parse_args()
	main(args.top)