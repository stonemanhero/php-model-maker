import os.path
import sys

# check configuration file syntax
def check_syntax(code):
	status = 1

	if len(code) < 2:
		status = 0

	if code[0][0] != "+":
		status = 0

	if status == 0:
		print("Syntax error in configuration file.")
		sys.exit()

def main():
	if not os.path.isfile("model.pmm"):
		print("You need to create model.pmm (configuration file).")
		sys.exit()

	with open ("model.pmm", "r") as input_file:
		code=input_file.readlines()

	check_syntax(code)

	# get model name
	model_name = code[0][1:].strip('\n')
	print(model_name)

	# get model attrs
	model_attr = []
	for attr in code[1:]:
		model_attr.append(attr.strip('\n'))

if __name__ == "__main__":
    main()
