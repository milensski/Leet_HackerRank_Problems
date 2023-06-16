if __name__ == '__main__':
    sequence = []
    commands = []
    N = int(input())

    for _ in range(N):
        commands.append(input())

    for command in commands:

        command = command.split()
        action = command[0]

        if action == 'insert':
            index = int(command[1])
            e = int(command[2])
            sequence.insert(index, e)

        elif action == 'print':
            print(sequence)

        elif action == 'remove':
            e = int(command[1])
            sequence.remove(e)

        elif action == 'append':
            e = int(command[1])
            sequence.append(e)

        elif action == 'sort':
            sequence.sort()

        elif action == 'pop':
            sequence.pop()

        elif action == 'reverse':
            sequence = sequence[::-1]
