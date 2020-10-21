# pabi_PythonProgramming_Week5_repetition
# list exercise : manage friends list

menu = 0
friends = ['max', 'july', 'amy', 'chris']
while menu != 9:
    print("------------------------")
    print("1. Show friends list")
    print("2. Add friend")
    print("3. Delete friend")
    print("4. Modify name")
    print("9. Exit")
    menu = int(input("Choose menu"))

    if menu == 1:
        print(friends)

    elif menu == 2:
        name = input("Enter name :")
        friends.append(name)

    elif menu == 3:
        del_name = input("Enter name which you want delete :")
        if del_name in friends:
            friends.pop(del_name)
        else:
            print("Not found %s in list" %del_name)

# pop()은 값을 저장하기 때문에 삭제만 하는 경우에는 메모리가 낭비된다.
# remove()로 삭제한다.
    # friends.remove(del_name)

    elif menu == 4:
        old_name = input("Enter name which you want modify :")
        new_name = input("Enter the new name :")
        if old_name in friends:
            old_name, new_name = new_name, old_name
        else:
            print("Not found %s in list" %name)


# menu 4번이 작동하지 않음
# 매개변수만 변경되고 friends 리스트는 수정이 되지 않았다.

    elif menu == 4:
        old_name = input("Enter name which you want modify :")
        new_name = input("Enter the new name :")
        if old_name in friends:
            index = friends.index(old_name)
            friends[index] = new_name
        else:
            print("Not found %s in list" % name)