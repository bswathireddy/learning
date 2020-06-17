while True:
    inputText=input('input:').lower()
    if inputText=='start':
        print("car has started...ready to go!")
    elif inputText=='stop':
        print("car has stopped")
    elif inputText.lower()=='quit':
        break
    else:
        print("I didn't understand")
