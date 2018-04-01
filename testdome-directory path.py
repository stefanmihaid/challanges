# Write a function that provides change directory (cd) function for an abstract file system.
#
# Notes:
#
# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.
# For example:
#
# path = Path('/a/b/c/d')
# path.cd('../x')
# print(path.current_path)
# should display '/a/b/c/x'.


class Path:
    def __init__(self, path):
        self.current_path = path

    def sep(self, command):
        result = []
        if command[0] == "/":
            command = command[1:]
        while len(command)>0:
            start = 0
            end = command.find("/")
            if end < 0:
                end = len(command)
            result.append(command[start:end])
            start = end
            command = command[start+1:]
        return result

    def get_path(self, current, command):
        if len(command) == 1:
            current = command
        for l in command:
            if l == "..":
                current = current[:-1]
                command = command[1:]
        current += command
        return current

    def separate(self, director):
        solution = []
        for l in director:
            solution.append("/")
            solution.append(l)
        return solution

    def cd(self, new_path):
        new = ""
        current = self.sep(self.current_path)
        command = self.sep(new_path)
        changed = self.get_path(current, command)
        for l in self.separate(changed):
            new +=l
        self.current_path = new



path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
