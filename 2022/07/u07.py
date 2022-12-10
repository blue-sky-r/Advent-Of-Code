#!/usr/bin/env python3

__day__  = 7

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Dir:

    def __init__(self):
        self.data = []

    def add_file(self, name, size):
        """ add new file to the current directory - does not check for duplicates """
        entry = { 'name': name, 'type': 'file', 'size': size }
        self.data.append(entry)

    def add_dir(self, name):
        """ add subdir to the current directory - does not check for duplicates """
        entry = { 'name': name, 'type': 'dir', 'data': Dir() }
        self.data.append(entry)

    def get_dirs(self):
        """ get only subdirs from current directory as a list  """
        return [ entry for entry in self.data if entry['type']=='dir' ]

    def get_files(self):
        """ get only files from current dir as a list """
        return [ entry for entry in self.data if entry['type']=='file' ]

    def get_dir_size(self):
        """ calculate dir size """
        size = sum([f['size'] for f in self.get_files()])
        for subdir in self.get_dirs():
            size += subdir['data'].get_dir_size()
        return size

    def print(self, level=1):
        """ print directory structure """
        if not verbose: return
        for entry in self.data:
            print('-' * level, entry['type'], entry['name'], entry.get('size','?'))
            if entry['type'] == 'dir':
                entry['data'].print(level+4)

    def update_dir_size(self):
        """ calculate abd update directory size - usefull for print structure for debug """
        s =  0
        for entry in self.data:
            if entry['type'] == 'dir':
                entry['size'] = entry['data'].calc_dir_size()
            s += entry['size']
        return s

    def get_dir_size_limit(self, r, limit=100000):
        """ get only dirs with size up to the limit - returns list """
        size = sum([f['size'] for f in self.get_files()])
        for subdir in self.get_dirs():
            rr, subdirsize = subdir['data'].get_dir_size_limit(r, limit)
            size += subdirsize
            if subdirsize <= limit:
                r.append(subdirsize)
        return r, size


class FileSystem:

    def __init__(self, sep='/'):
        self.root = Dir()
        self.sep = sep

    def iterate_dirsX(self, fs=None, r=[]):
        """ recursively print fs tree """
        if fs is None: fs = self.root
        for dir in fs.get_dirs():
            #if dir['size'] <= 100000:
            r.append( (dir['name'], dir['size']) )
            rd = self.iterate_dirs(dir['data'])
            #r.extend(rd)
        return r

    def fs_cwd(self, cwd: list):
        """ return fs pointing to cwd """
        fs = self.root
        for dirname in cwd:
            if dirname == '/':
                fs = self.root
                continue
            # find dir entry with dirname
            fs = [ entry['data'] for entry in fs.get_dirs() if entry['name'] == dirname ][0]
        return fs

    def cdX(self, cwd: list, dirname):
        """ cd command in cwd returns new cwd """
        if dirname == self.sep:
            return self.root
        if dirname == '..':
            if len(cwd) >= 1:
                cwd.pop()
            return self.fs_cwd(cwd)
        cwd.append(dirname)
        return self.fs_cwd(cwd)

    def cd_dir(self, cwd: list, dirname):
        """ execute cd command - returns new cwd as a list """
        if dirname == '/':
            return []
        if dirname == '..':
            cwd.pop()
            return cwd
        return cwd + [dirname]

    def add_dir(self, cwd, dirname):
        """ add dir to cwd """
        fs = self.fs_cwd(cwd)
        fs.add_dir(dirname)

    def add_file(self, cwd: list, filename, filesize):
        """ add file to cwd """
        fs = self.fs_cwd(cwd)
        fs.add_file(filename, filesize)
        return cwd

class SpaceOnDevice:

    def __init__(self):
        pass

    def build_filesystem(self, cmdlog):
        """ build filesystem from terminal log """
        fs = FileSystem()
        cwd, prompt, ls_output = [], '$ ', None
        for line in cmdlog:
            if line.startswith(prompt):
                ls_output = False
                prompt_, cmd = line.split(maxsplit=1)
                if cmd.startswith('cd '):
                    cd_, dirname = cmd.split()
                    cwd = fs.cd_dir(cwd, dirname)
                elif cmd.startswith('ls'):
                    ls_output = True
                else:
                    print('ERR: %s - unrecognized line' % line)
            else:
                if ls_output:
                    size_dir, name = line.split()
                    if size_dir == 'dir':
                        fs.add_dir(cwd, name)
                    else:
                        fs.add_file(cwd, name, int(size_dir))
                else:
                    print('ERR: %s - unrecognized line' % line)
        return fs

    def task_a(self, input: list):
        """ task A """
        fs = self.build_filesystem(input)
        if verbose:
            fs.root.print()
            s = fs.root.update_dir_size()
            fs.root.print()
        r, s = fs.root.get_dir_size_limit([], limit=100000)
        return sum(r)

    def task_b(self, input: list):
        """ task B """
        disksize, updatesize = 70000000, 30000000
        fs = self.build_filesystem(input)
        if verbose:
            fs.root.print()
            s = fs.root.update_dir_size()
            fs.root.print()
        freespace = disksize - fs.root.get_dir_size()
        required = updatesize - freespace
        r, s = fs.root.get_dir_size_limit([], limit=updatesize)
        return min([dirsize for dirsize in r if required <= dirsize <= updatesize])


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

# ========
#  Task A
# ========

# test cases
testcase_a(SpaceOnDevice(), testdata,  95437)

# 2031851
testcase_a(SpaceOnDevice(),   None,  2031851)

# ========
#  Task B
# ========

# test cases
testcase_b(SpaceOnDevice(), testdata,  24933642)

# 2568781
testcase_b(SpaceOnDevice(),   None,   2568781)
