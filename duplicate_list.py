
def function():
i=0
a=[]
while i<len(string_list):
    if string_list[i] not in a:
        a.append(string_list[i])
    i=i+1
print(a)
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
function()
