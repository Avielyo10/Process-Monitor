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
        print 'Still Building Up.\n'
        selector()
    else:
        selector()

selector()