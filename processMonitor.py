def selector():
    print('\t\t####### Process Monitor #######')
    print 'Please Select Mode: '
    print '[1] Monitor Mode'
    print '[2] Regular Mode'
    pmMode = raw_input()
    if pmMode == '1':
        import monitor
        monitor
    elif pmMode =='2':
        import regularMode
        regularMode
    else:
        selector()

selector()