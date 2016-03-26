def sed(seq, rep_seq, read_file, write_file):
    #replaces a string 'seq' with 'rep_seq' in 'read_file' and writes to 'write_file'
    file1 = open(read_file)
    file2 = open(write_file, 'w')
    for line in file1:
        if seq in line:
            file2.write(line.replace(seq, rep_seq))
            continue
        file2.write(line)
    file1.close(), file2.close()

#sed('the sidewalk', 'my sandwich', "Where the Sidewalk Ends.txt", 'Where my sandwich ends.txt')