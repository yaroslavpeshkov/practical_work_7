volume_n = int(input())
volumes = []
for i in range(1, int(volume_n**(1/3))+1):
    volumes.append(str(i**3))
print(' '.join(volumes))
