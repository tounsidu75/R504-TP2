def affiche(n):
    output = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            output += "FrisBee "
        elif i % 3 == 0:
            output += "Fizz "
        elif i % 5 == 0:
            output += "Buzz "
        else:
            output += str(i) + " "
    return output.strip()  # Pour enlever l'espace final

if __name__ == "__main__":
    n = 15  # on peut changer cette valeur pour tester d'autres nombres
    print(affiche(n))
