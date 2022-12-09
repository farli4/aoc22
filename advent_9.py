class Coord():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Rope():
    def __init__(self, num_knots: int) -> None:
        self.knots = []
        self.knots.append(Head())
        for _ in range(1, num_knots):
            self.knots.append(Tail(self.knots[-1]))

    def move(self, step):
        self.knots[0].move(step)
        for knot in self.knots[1:]:
            knot.move()


class Knot():
    def __init__(self) -> None:
        pass

    def move():
        pass


class Head(Knot):
    def __init__(self):
        self.position = Coord(0, 0)
        self.previous_position = Coord(0, 0)

    def move(self, step: str):
        self.previous_position = Coord(self.position.x, self.position.y)
        if step == 'R':
            self.position.x += 1
        if step == 'L':
            self.position.x -= 1
        if step == 'U':
            self.position.y += 1
        if step == 'D':
            self.position.y -= 1


class Tail(Knot):
    def __init__(self, parent: Knot):
        self.position = Coord(0, 0)
        self.trail_history = [Coord(0, 0)]
        self.parent = parent

    def move(self):
        x_dif = self.parent.position.x - self.position.x
        y_dif = self.parent.position.y - self.position.y

        if abs(x_dif) >= 2 or abs(y_dif) >= 2:
            if abs(x_dif) > 0:
                self.position.x += int(x_dif/abs(x_dif))
            if abs(y_dif) > 0:
                self.position.y += int(y_dif/abs(y_dif))
            self.trail_history.append(Coord(self.position.x, self.position.y))


def read_file(fname):
    route = []
    with open(fname) as f:
        for line in f:
            char, num = line.strip().split(' ')
            for _ in range(int(num)):
                route.append(char)
    return route


if __name__ == '__main__':
    steps = read_file('9_input.txt')
    rope = Rope(10)
    for step in steps:
        rope.move(step)

    print(f'task 1 solution: {len(set(rope.knots[1].trail_history))}')
    print(f'task 2 solution: {len(set(rope.knots[-1].trail_history))}')
