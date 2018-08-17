import urllib.request

url = input("Enter azlyrics URL: ")

head = "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"
end = "</div>"

content = urllib.request.urlopen(url).read()
s = content.decode("utf-8")

s = s[s.find(head):]
s = s[:s.find(end)]
s = s[s.find("\n"):]
s = s.split("<br>")

for i in range(0, len(s)):
    s[i] = s[i].strip("\n")
    
for i in s:
    print(i)

