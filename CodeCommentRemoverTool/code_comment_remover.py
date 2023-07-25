with open("code_comment_remover.py") as file:

    contents = file.readlines()

open_paren_count = 0

closed_paren_count = 0

decrease_count = 0

for num in range(len(contents)):

    if "#" in contents[num - decrease_count]:

        if contents[num - decrease_count].startswith("#"):

            contents.remove(contents[num - decrease_count])

            decrease_count += 1

        else:

            nline = ""

            for char in contents[num - decrease_count]:

                if char == '(':

                    open_paren_count += 1

                    nline += char

                elif char == ')':

                    closed_paren_count += 1

                    nline += char

                elif char == '#' and open_paren_count == closed_paren_count:

                    break

                else:

                    nline += char

            contents.remove(contents[num - decrease_count])

            contents.insert(num - decrease_count, nline)

file.close()

with open("uncommentedcode.py", "w") as nfile:

    nfile.writelines(contents)