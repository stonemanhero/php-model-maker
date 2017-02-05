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

def create_model(name, attrs):
	model_filename = "Class" + name + ".php" 
	output_file = open(model_filename, 'w')

	output_file.write("<?php\n")
	output_file.write("\tclass " + name + "\n")
	output_file.write("\t{\n")

	for attr in attrs:
		output_file.write("\t\tprivate $" + attr + "\n")

	output_file.write("\n\t\t// setters\n")

	for attr in attrs:
		output_file.write("\t\tpublic function set_" + attr + "($new_" + attr + ")\n")
		output_file.write("\t\t{\n")
		output_file.write("\t\t\t$this->" + attr + " = $new_" + attr + ";\n")
		output_file.write("\t\t}\n\n")

	output_file.write("\t\t// getters\n")

	for attr in attrs:
		output_file.write("\t\tpublic function get_" + attr + "()\n")
		output_file.write("\t\t{\n")
		output_file.write("\t\t\treturn $this->" + attr + ";\n")
		output_file.write("\t\t}\n\n")

	output_file.write("\t}")

	print "All done!"

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

	create_model(model_name, model_attr)

if __name__ == "__main__":
    main()
