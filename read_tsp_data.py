def from_file(file_path):
    with open(file_path, 'r') as f:
        line = f.readline()
        output = []
        while line:
            line = line.replace('\n', '').split(' ')
            line = [float(x) if '.' in x else x for x in line]  # convert decimals
            line = [int(x) if type(x) is str and x.isdigit() else x for x in line]  # convert integers
            if type(line[0]) is int:
                output.append(
                    {
                        'index': line[0],
                        'x': line[2],
                        'y': line[1],
                    }
                )
            line = f.readline()
    return output
