def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    # Write your code here
    # Iterative:
    # lst = []
    # while link is not Link.empty:
    #     lst.append(link.first)
    #     link = link.rest
    # return lst
    # Recursive:
    converted_list = []

    def convert_link_helper(lst, linked):
        if linked is Link.empty:
            return lst
        else:
            print(linked.first)
            lst.append(linked.first)
            return convert_link_helper(lst, linked.rest)
    return convert_link_helper(converted_list, link)


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    # Write your code here
    current = n
    prev_link = Link.empty
    while current > 0:
        attr = current % 10
        current = current // 10
        link = Link(attr, prev_link)
        prev_link = link
    return link

def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    # Write your code here
    lst = convert_link(link)
    if len(lst) <= 2:
        return
    # else:
    #     i = 1
    #     current_link = link
    #     while i <= len(lst):
    #
    #         skipped_link = current_link.rest
    #         next_link = skipped_link.rest
    #         new_link = Link(current_link.first, next_link)
    #         i += 2
    #         current_link = new_link
    #     link = current_link
    else:
        i = 1
        iterated_link = link.rest
        current_link = link
        while i < len(lst) - 1:
            current_link.rest = iterated_link.rest
            iterated_link = iterated_link.rest
            iterated_link = iterated_link.rest  # Skipping the even indexed Link
            print(repr(iterated_link))
            current_link = current_link.rest    # Brings the current scope to the most recently moved up odd link
            print(repr(current_link))
            i += 2
        if len(lst) % 2 == 0:
            current_link.rest = Link.empty




def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    if link is Link.empty:  # If the List is List.empty, the function ends. Otherwise an empty list throws an error
        return

    if isinstance(link.first, int):
        link.first = fn(link.first)
    elif isinstance(link.first, Link):
        deep_map_mut(fn, link.first)

    if link.rest is Link.empty:
        pass
    elif isinstance(link.rest, Link):
        deep_map_mut(fn, link.rest)









class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
