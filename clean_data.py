'''
    Removes lines that begin with a whitespace, believe it messes with reading in csv
    Ran into an issue with some other newline stuff so I only take the first 30000 entries.
'''

line_buffer = []
with open('edited_data.csv', 'r') as fin:
    counter = 0
    running = 1
    bad = 1
    for line in fin.readlines():
        
        if line[0] == '\\':
            bad = 1
            running += 1
        else:
            bad = 0

        if bad == 0 and running != 1:
            counter -= running
            line_buffer = line_buffer[0:(len(line_buffer) - running)]
            running = 1

        line_buffer.append(line)

fout = open('finalData.csv', 'w')
[fout.write(line) for x, line in enumerate(line_buffer) if x < 30000]

