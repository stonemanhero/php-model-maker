from __future__ import print_function
import os.path
import sys


def write_to_file(filename, code):
	output_file = open(filename, 'w')
	output_file.write(code)
	output_file.close()

# check configuration file syntax
def check_syntax(code):
	status = 1

	if len(code) < 2:
		status = 0

	if code[0][0] != "+":
		status = 0

	if status == 0:
		print("\t [ fail ]")
		sys.exit()

# create php code
def create_model(name, attrs):
	filename = "Class" + name + ".php"
	code = ""

	code = code + "<?php\n"
	code = code + "\tclass " + name + "\n"
	code = code + "\t{\n"

	for attr in attrs:
		code = code + "\t\tprivate $" + attr + "\n"

	code = code + "\n\t\t// setters\n"

	for attr in attrs:
		code = code + "\t\tpublic function set_" + attr + "($new_" + attr + ")\n"
		code = code + "\t\t{\n"
		code = code + "\t\t\t$this->" + attr + " = $new_" + attr + ";\n"
		code = code + "\t\t}\n\n"

	code = code + "\t\t// getters\n"

	for attr in attrs:
		code = code + "\t\tpublic function get_" + attr + "()\n"
		code = code + "\t\t{\n"
		code = code + "\t\t\treturn $this->" + attr + ";\n"
		code = code + "\t\t}\n\n"

	code = code + "\t}"

	return filename, code

def main():
	if not os.path.isfile("model.pmm"):
		print("You need to create model.pmm (configuration file).")
		sys.exit()

	# read file
	print("Analysing model file... ", end='')
	with open ("model.pmm", "r") as input_file:
		code=input_file.readlines()
	print("[ ok ]")

	# check syntax
	print("Checking syntax... ", end='')
	check_syntax(code)
	print("[ ok ]")

	# get model name
	print("\nModel name: ", end='')
	model_name = code[0][1:].strip('\n')
	print(model_name)

	# get model attrs
	print("\nModel attrs: ")
	model_attr = []
	for attr in code[1:]:
		model_attr.append(attr.strip('\n'))
		print('\t' + attr.strip('\n'))

	print("\nGenerating code... ", end='')
	filename, code = create_model(model_name, model_attr)
	print("[ ok ]")

	print("Creating Class" + model_name + ".php =>", end='')
	write_to_file(filename, code)
	print(" All done!")

if __name__ == "__main__":
    main()
