import re
import sys


def read_file(path):
    arr = []
    with open(path) as my_file:
        for line in my_file:
            arr.append(line)
    return arr


def is_line_ok(line, home_directory):
    match = re.search("- *([^ \n]+):", line)
    vol = match.group(1)

    is_local_directory = (vol[0] == ".") or (vol[0] != "/")
    is_dir_ok = (home_directory in vol)
    if is_local_directory:
        return True
    if is_dir_ok:
        return True
    #print("Is Local Directory: " + str(is_local_directory))
    #print("Is Ok: " + str(is_dir_ok))
    return False


def main():
    if len(sys.argv) != 3:
        return 3

    file_path = sys.argv[1]     # docker-compose.yml
    home_dir = sys.argv[2]      # /var/www/vhosts/ubpau.sixhands.co

    lines = []
    try:
        lines = read_file(file_path)
    except (Exception):
        return 2

    is_volumes_section = False
    for line in lines:
        line_trimmed = line.strip()
        if "volumes:" in line_trimmed:
            is_volumes_section = True
            continue
        if is_volumes_section and line_trimmed[0] == "-":
            is_ok = is_line_ok(line_trimmed, home_dir)
            if not is_ok:
                return 1
        else:
            is_volumes_section = False

    return 0


if __name__ == "__main__":
    x = main()
    exit(x)



