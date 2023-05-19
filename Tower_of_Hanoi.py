def tower_of_hanoi(disks,source,auxiliary,target):
    if (disks == 1):
        print('move disks 1 from rod {} to rod {}.'.format(source,target))
        return
    tower_of_hanoi(disks - 1,source,target,auxiliary)
    print('move disks {} from rod {} to rod {}.'.format(disks,source,target))
    tower_of_hanoi(disks - 1,auxiliary,source,target)
disks = int(input('Enter the number of disks :'))
tower_of_hanoi(disks,'1','2','3')
