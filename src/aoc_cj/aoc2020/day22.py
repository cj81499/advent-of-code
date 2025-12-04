import collections

import more_itertools as mi


class Deck:
    def __init__(self, n, cards):
        self.n = n
        self.cards = collections.deque(cards)

    @staticmethod
    def parse(deck_str):
        player_n, *cards = deck_str.splitlines()
        n = int(player_n.strip("Player ").strip(":"))
        cards = (int(x) for x in cards)
        return Deck(n, cards)

    def __repr__(self):
        return f"Player {self.n}'s deck: {', '.join(str(x) for x in self.cards)}"

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.popleft()

    def put_on_bottom(self, *cards):
        self.cards.extend(cards)

    def score(self):
        return sum((i + 1) * n for i, n in enumerate(reversed(self.cards)))

    def copy(self):
        return Deck(self.n, self.cards)

    def subdeck(self, n):
        return Deck(self.n, [*self.cards][:n])


class CombatGame:
    def __init__(self, decks):
        assert len(decks) == 2
        self.decks = [d.copy() for d in decks]

    @classmethod
    def parse(cls, game_str):
        decks = [Deck.parse(d) for d in game_str.split("\n\n")]
        return cls(decks)

    def __repr__(self):
        return f"{type(self)}({self.decks})"

    def winner_score(self):
        return self.winning_deck().score()

    def winning_deck(self):
        assert self._is_done()
        for d in self.decks:
            if len(d) != 0:
                return d

    def play(self):
        while not self._is_done():
            self._round()

    def _is_done(self):
        return any(len(d) == 0 for d in self.decks)

    def _round(self):
        draw_deck_pairs = [(d.draw(), d) for d in self.decks]
        _winning_draw, winning_deck = max(draw_deck_pairs)
        to_put_on_bottom = sorted((n for n, _deck in draw_deck_pairs), reverse=True)
        winning_deck.put_on_bottom(*to_put_on_bottom)


class RecursiveCombatGame(CombatGame):
    game_n = 1

    def __init__(self, decks):
        super().__init__(decks)
        self.seen = set()
        self.loop = False
        self._game_n = RecursiveCombatGame.game_n
        RecursiveCombatGame.game_n += 1
        self._round_n = 1

    def play(self):
        super().play()

    def _round(self):
        r = repr(self)
        if r in self.seen:
            self.loop = True
            return
        self.seen.add(r)
        draw_deck_pairs = [(d.draw(), d) for d in self.decks]

        can_recurse = all(n <= len(deck) for n, deck in draw_deck_pairs)
        if can_recurse:
            subgame_winner_n = self._play_subgame(draw_deck_pairs)
            winning_draw, winning_deck = mi.one(filter(lambda p: p[1].n == subgame_winner_n, draw_deck_pairs))
            losing_draw, _losing_deck = mi.one(filter(lambda p: p[1].n != subgame_winner_n, draw_deck_pairs))
            to_put_on_bottom = [winning_draw, losing_draw]
            winning_deck.put_on_bottom(*to_put_on_bottom)
        else:
            _winning_draw, winning_deck = max(draw_deck_pairs)
            to_put_on_bottom = sorted((n for n, _deck in draw_deck_pairs), reverse=True)
            winning_deck.put_on_bottom(*to_put_on_bottom)
        self._round_n += 1

    def _play_subgame(self, draw_deck_pairs):
        # copy first n cards of each deck where n was that player's draw
        subdecks = [deck.subdeck(n) for n, deck in draw_deck_pairs]
        subgame = RecursiveCombatGame(subdecks)
        subgame.play()
        return subgame.winning_deck().n

    def winning_deck(self):
        assert self._is_done()
        return self.decks[0] if self.loop else super().winning_deck()

    def _is_done(self):
        return self.loop or super()._is_done()


def part_1(txt):
    g = CombatGame.parse(txt)
    g.play()
    return g.winner_score()


def part_2(txt):
    g = RecursiveCombatGame.parse(txt)
    g.play()
    return g.winner_score()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
