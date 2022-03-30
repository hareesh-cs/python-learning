import os

host = input("Enter the host name: ")
print("Average ping time:", end=" ")
res = os.system("ping -c 15 " + host + "  | tail -1| awk '{print $4}' | cut -d '/' -f 2")
# res=os.system("ping -c 5 "+ host)
