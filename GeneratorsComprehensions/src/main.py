def fix_wiring(cables: list, sockets: list, plugs: list):
    yield [
        f"{'plug' if 'plug' in plug else 'weld'} " +
        f"{cable} {'into' if 'plug' in plug else 'to'} " +
        f"{socket} {'using '+ plug if 'plug' in plug else 'without plug'}"
        for plug, socket, cable in zip(
            [item for item in plugs if isinstance(
                item, str) and "plug" in item] + ['weld'] * len(cables),
            [item for item in sockets if isinstance(
                item, str) and "socket" in item],
            [item for item in cables if isinstance(
                item, str) and "cable" in item]
        )
    ]

plugs = ['plug1', 'plug2', 'plug3']
sockets = ['socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable1', 'cable2', 'cable3', 'cable4']

    
    
iterator = test()
iterator.next 