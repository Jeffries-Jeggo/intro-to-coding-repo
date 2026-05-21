def get_yes_or_no():
    answer = input('Type "yes" or "no": ')
    while answer != "yes" and answer != "no":
        print("Invalid. Try again.")
        answer = input('Type "yes" or "no": ')
    return answer
