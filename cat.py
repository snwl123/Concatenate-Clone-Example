def cat(source, dest):
    for line in source.read():
        dest.write(line)