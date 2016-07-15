# We are going to parse economic data from the web into a dictionary and save it as a javascript array.

# Set up
start = "var data = {"
end = "};"

###########
# Process #
###########
def parse_to_break(s):
	i = 0	
	while i < len(s) and s[i] != "\t" and s[i] != "\n":
		i += 1
	return s[0:i], s[i + 1:]

def parse_to_js(file):
	file_as_string = file.read()
	toReturn = ""
	curr = ""
	rest = file_as_string
	state = curr, rest
	i = 0
	while state[1] != "":
		state = parse_to_break(state[1])
		curr = state[0]
		if (i % 2 == 0):
			toReturn += '"' + curr + '"' + ": "
		else:
			toReturn += '"' + curr + '", '
		i += 1
	return start + toReturn + end

#Running stuff

file_to_read = open("data.txt", "r")
file_to_write = parse_to_js(file_to_read)
write_location = open("data.js", "w")
write_location.write(file_to_write)











