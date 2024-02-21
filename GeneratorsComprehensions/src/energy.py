import unittest

# Base structure
# temp_list = [item1 + item2 for item1,item2 in zip(items1, items2)]


def fix_wiring(cables: list, sockets: list, plugs: list):
    return [
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


class TestFixWiringFunction(unittest.TestCase):
    def test_1(self):
        plugs = ['plug1', 'plug2', 'plug3']
        sockets = ['socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable1', 'cable2', 'cable3', 'cable4']

        result = [
            "plug cable1 into socket1 using plug1",
            "plug cable2 into socket2 using plug2",
            "plug cable3 into socket3 using plug3",
            "weld cable4 to socket4 without plug"
        ]
        cnt = 0
        for c in fix_wiring(cables, sockets, plugs):
            self.assertEqual(c, result[cnt])
            cnt += 1

    def test_2(self):
        plugs = ['plugZ', None, 'plugY', 'plugX']
        sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable2', 'cable1', False]

        result = [
            "plug cable2 into socket1 using plugZ",
            "plug cable1 into socket2 using plugY"
        ]
        cnt = 0
        for c in fix_wiring(cables, sockets, plugs):
            self.assertEqual(c, result[cnt])
            cnt += 1


if __name__ == "__main__":
    unittest.main()
