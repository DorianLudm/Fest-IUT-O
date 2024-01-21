import tarfile
with tarfile.open('myFolder.tar', 'w') as tar:
    tar.add('myFolder/')