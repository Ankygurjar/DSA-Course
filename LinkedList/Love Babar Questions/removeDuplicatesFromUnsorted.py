


def removeDuplicates(head):
    mySet = set()
    track = head
    mySet.add(track.data)
    while track and track.next:
        if track.next.data in mySet:
            track.next = track.next.next
        else:
            mySet.add(track.next.data)
            track = track.next

    return head




