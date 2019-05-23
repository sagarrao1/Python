with open('log.txt', 'r') as rf:
    with open('Write.txt', 'w') as wf:
        chunk_size=40
        rf_contents= rf.read(chunk_size)
        while len(rf_contents) > 0:
            wf.write(rf_contents)
            rf_contents = rf.read(chunk_size)

        # for line in rf:
        #     wf.write(line)