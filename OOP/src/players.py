class Player:
    def __init__(self) -> None:
        self.name: str = ""
        self.reset()

    def reset(self):
        self.score = 0
        self.current_bet = True
        self.opp_last_bet = True
        self.total_bets = 0

    def make_bet(self):
        return self.current_bet

    def update_score(self, opp_bet):
        self.total_bets += 1
        if opp_bet is True and self.current_bet is True:
            self.score += 2
        elif self.current_bet is False and opp_bet is True:
            self.score += 3
        elif self.current_bet is True and opp_bet is False:
            self.score -= 1
        self.opp_last_bet = opp_bet


class Cheater(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheater"

    def make_bet(self):
        self.current_bet = False
        return self.current_bet


class Cooperator(Player):
    def __init__(self) -> None:
        super().__init__()
        self.current_bet = True
        self.name = "Cooperator"

    def make_bet(self):
        return self.current_bet


class Copycat(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Copycat"

    def make_bet(self):
        self.current_bet = self.opp_last_bet
        return self.current_bet


class Grudger(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Grudger"

    def make_bet(self):
        if self.opp_last_bet is False:
            self.current_bet = False
        return self.current_bet


class Detective(Player):
    def __init__(self) -> None:
        super().__init__()
        self.initial_bets = [True, False, True, True]
        self.mode = True
        self.name = "Detective"

    def reset(self):
        self.mode = True
        return super().reset()

    def make_bet(self):
        if self.total_bets < 4:
            self.current_bet = self.initial_bets[self.total_bets]
            if self.opp_last_bet is False:
                self.mode = False
        else:
            if self.mode is True:
                self.current_bet = False
            else:
                self.current_bet = self.opp_last_bet
        return self.current_bet


class Me(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Me"
        self.cnt = 0

    def reset(self):
        self.cnt = 0
        return super().reset()

    def make_bet(self):
        if self.cnt < 2:
            self.cnt += 1
            self.current_bet = True
        else:
            self.cnt = 0
            self.current_bet = self.opp_last_bet
        return self.current_bet
