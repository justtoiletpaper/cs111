# Note: The Tree implemenation is at the bottom of the file
# Please read the docstrings to learn how to interact with a Tree object.

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = Tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = Tree('roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = Tree(1, [Tree('berry',[Tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    # Write your code here
    if t.label == 'berry':
        return True
    else:
        for branch in t.branches:
            if branch.label == 'berry':
                return True
            elif branch.branches:
                if berry_finder(branch) is True:
                    return True
    return False

def height(t):
    """Return the height of a Tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    # Write your code here
    deepest_depth = 0
    if not t.branches:
        return deepest_depth
    else:
        deepest_depth += 1
    for branch in t.branches:   # Finds the longest branch and adds it to the total
        longest_branch_height = 0
        if branch.branches:
            branch_height = height(branch)  # Recursive call to figure out the length of the branch
            if branch_height > longest_branch_height:
                longest_branch_height = branch_height
        deepest_depth += longest_branch_height
    return deepest_depth



def max_path_sum(t):
    """Return the maximum path sum of the Tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    # Write your code here
    total = t.label
    if not t.branches:
        return total
    else:
        longest_branch_sum = 0
        for branch in t.branches:
            branch_sum = 0
            if branch.branches:
                branch_sum += max_path_sum(branch)  # Calculates longest possible branch length, including parent node
            else:
                branch_sum = branch.label   # If the branch has no branches, return the label of just that node
            if branch_sum > longest_branch_sum:     # Finds the longest branch
                longest_branch_sum = branch_sum
        total += longest_branch_sum
        return total

def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])] ), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    # Highlight the code and press Ctrl-'/' to unccomment the code all at once
    if t.label == x:
        return [x]
    path = [t.label]
    for branch in t.branches:
        # temp_path = []
        if branch.branches:
            temp_path = find_path(branch, x)
        else:
            temp_path = [branch.label]
        if temp_path:       # Checks to make sure temp path isn't empty, so element doesn't throw error
            for element in temp_path:
                if element == x:
                    return path + temp_path


# Optional Question
def has_path(t, word):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular word.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    # Write your code here
    # letter_list = list(word)
    # word_path = [t.label]
    # for branch in t.branches:
    #     letters_left = word[1:]
    #     if has_path(branch, letters_left):
    #         word_path.append(branch.label)
    #
    #
    #
    # if word_path == letter_list:
    #     return True
    # else:
    #     return False


class Tree:

    def __init__(self, label, branches=[]):
        """
        A Tree is constructed by passing a label and an optional *list* of branches.
        The list passed must only contain objects of the Tree class.
        """
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        """
        Returns a boolean, true if this Tree object is a leaf (has no branches), false otherwise.
        """
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{branch_str})'

    def __str__(self):
    
        def indented(self):
            lines = []
            for b in self.branches:
                for line in indented(b):
                    lines.append('  ' + line)
            return [str(self.label)] + lines

        return '\n'.join(indented(self))

