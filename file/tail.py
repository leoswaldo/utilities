#!/usr/local/bin/python3.5

## function: tail
#  Description: tail function works as the linux utility for tailing
#      the last n lines of a given file, this script works for very big
#      files also, since it moves the cursor into the file to the end, and
#      starts scanning the last data, it read chomps as big as the buffer_size
#      variable, or the rest size of the file if it is smaller
def tail(filepath, lines=10):
    buffer_size=1048
    with open(filepath, 'rb+') as f:
        # go to the end of the file to see the size of it
        f.seek(0, 2)
        file_size = f.tell()
        total_bytes_read = lines_founded= 0
        ##lines_content = ''
        # itereate through the file due to the lines found and the file_size
        while(lines_founded < lines and \
            total_bytes_read < file_size):
            bytes_to_read = 0
            # we make sure the next block of data to read is not bigger than
            # the rest of the file
            if(f.tell() >= buffer_size):
                bytes_to_read = buffer_size
            else:
                bytes_to_read = f.tell()
            # we move the cursor to the point were we should read the 
            # following chomp of data
            f.seek(-(bytes_to_read + total_bytes_read), 2)
            block_content = f.read(bytes_to_read)
            # its read as bytes, we convert it and count the number of lines
            block_content = block_content.decode('utf-8')
            lines_founded += block_content.count('\n')
            # lines commented with '##' are for secondary solution
            ##lines_content = '%s%s' % (block_content, lines_content)
            total_bytes_read += bytes_to_read
            
        # its time to move the cursor to the point where we read the ammount 
        # of lines we were asked, or exceded and read the file from there to
        # the end, remember readlines methon breaks with '\n' from cursor point
        f.seek(-total_bytes_read, 2)
        last_lines = f.readlines()
        ##last_lines = lines_content.split('\n')
        
        # from now we make sure we only print the requested number or the 
        # max lines in case the file does not have that many
        total_last_lines = len(last_lines)
        if(total_last_lines >= lines):
            lines_to_tail = lines          
        else:
            lines_to_tail = total_last_lines
        
        for i in range(lines_to_tail):
            line = last_lines[i + (total_last_lines - lines_to_tail\
                )].decode('utf-8')
            line = line.replace('\n', '')
            ##line = last_lines[i + (total_last_lines - lines_to_tail)]
            print(line)


if(__name__ == '__main__'):
    tail('file_example', 7)
