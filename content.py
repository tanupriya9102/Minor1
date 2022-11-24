def test_content():
    content=[]
    n=int(input("enter no of elements:"))
    while(len(content)!=n):
        i=input("enter value:")
        content.append(i)
    print(content)

c=test_content()
