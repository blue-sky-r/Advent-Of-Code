#!/usr/bin/env python

__motd__ = '--- Day 11: Radioisotope Thermoelectric Generators ---'

__url__ = 'http://adventofcode.com/2016/day/11'

import datetime

# vebosity options
#
ver_level = 0x01
ver_limit = 0x02
ver_move  = 0x04
ver_depth = 0x08
ver_map   = 0x10
ver_sol   = 0x20
ver_stat  = 0x40

# set verbosity
#
verbose = ver_limit | ver_sol | ver_stat
#verbose = ver_move | ver_depth | ver_map | ver_sol | ver_stat
#verbose = ver_map


def print_msg(level, *msg, **kwargs):
    " print msg if verbosity level is enabled "
    if level & verbose:
        for m in msg:
            print m,
        if not kwargs.get('nocr', False): print


class Cache:
    " remeber visited state -> level "

    def __init__(self):
        self.mem = {}

    def state_to_key(self, state):
        " state is dictionary - make it a string "
        return repr(state)

    def store_level_state(self, level, state):
        " write to cache state -> level entry "
        key = self.state_to_key(state)
        self.mem[key] = level

    def get_level_for_state(self, state):
        " read from cache level for state "
        key = self.state_to_key(state)
        return self.mem.get(key)

    def update_level_state(self, level, state):
        " update/store level in cache "
        key = self.state_to_key(state)
        if self.mem.get(key, 9999) <= level: return
        self.mem[key] = level

    def __len__(self):
        " cache size for final stats "
        return len(self.mem.keys())


class RtgBuilding:
    " puzzle building "

    def __init__(self, floors=4, elevator='E', maxdepth=100):
        " init building with rtg items, number of floors, elevator symbol and max. depth limit for recursion "
        # building 1 .. floors
        self.floors = 4
        # ASCII symbol for elevator
        self.elevator = elevator
        # init map of list of items for each floor
        self.startstate = dict( [ (f+1,[]) for f in range(self.floors) ] )
        # initial conditions
        self.reset(maxdepth)

    def all_items(self):
        " get full list of sorted items for all the floors - used only for showing the map "
        l = []
        for floor,items in self.startstate.items():
            l += items
        # remove elevator (we want it at first place)
        l.remove(self.elevator)
        # sort and add elevator
        sl = [self.elevator] + sorted(l)
        return sl

    def reset(self, maxdepth=100):
        " reset/init all internal variables (cache, solution) "
        # max depth to traverse
        self.maxdepth = maxdepth
        # visited states level->[state]
        self.memory = Cache()
        # solution steps
        self.solution = []

    def set_floors(self, lst):
        " set floors map from list tupples (floor, items) "
        # floors
        for floor, items in lst:
            self.set_floor(floor, items)
        # set of all items
        return self

    def set_floor(self, floor, items):
        " put items on floor "
        # set item(s) list on floor
        self.startstate[floor] = items
        return self

    def min_moves_togo(self, state):
        " quickly estimate min. moves required to move all items on map to top floor "
        # elevator floor, elevator floor items
        ef = self.elevator_floor(state)
        eitems = state[self.elevator_floor(state)]
        # this overestimates if there is only one item on elevator floor. we handle that later
        rides = 1 if len(eitems) <= 3 else 1+2*(len(eitems)-3)
        # moves needed from elevator floor
        m = (self.floors-ef) * rides
        # can transport only 1 item from non-elevator floors
        m += sum([ 2*(self.floors - floor) * len(items) for floor, items in state.items() if self.elevator not in items and floor != self.floors ])
        # result is valid if there are two and more items on elevator floor (3 and more with elevator)
        if len(eitems) >= 3: return m
        # elevator is not full, we can get another item
        # calc distance->floor for floors with some items left
        distd = dict([ (ef-floor,floor) for floor,items in state.items() if len(items)>0 ])
        # take 2nd item from the floor with max distance to save the most moves
        floor = distd[max(distd)]
        # there will be no rides from elevator floor as we go to the selected floor to pickup 2nd item
        m = m - (self.floors-ef) + max(distd) - (self.floors - floor)
        return m

    def set_visited(self, level, state):
        " remeber (cache) visited state at depth level "
        self.memory.update_level_state(level, state)

    def was_visited_on_upper_level(self, level, state):
        " check if state was already visited on this or upper level "
        lvl =  self.memory.get_level_for_state(state)
        return False if lvl is None else lvl <= level

    def copy_state(self, astate=None):
        " create a new copy of state astate "
        # deep copy - creates new dictionary
        state = astate if astate else self.startstate
        return dict([ (floor,items[:]) for floor,items in state.items() ])

    def show_map(self, level=None, state={}, force=False):
        " show ASCII map of all floors "
        # only if vebose_map is active, use force to override
        if not force and not (verbose & ver_map): return
        # show map
        if not state: state = self.startstate
        print "Level:",level,"est.moves to go:",self.min_moves_togo(state)
        for fl in range(self.floors, 0, -1):
            # floor number
            print "F%d" % fl,
            # floor items
            items = state[fl]
            for el in self.all_items():
                sym = el if el in items else '.'
                print "%-3s" % sym,
            print

    def find_min(self, limit=100, start=None):
        " find minimal number of steps "
        if start is None: start = self.min_moves_togo(self.startstate)
        # try max.depth from start up to the limit
        for mx in range(start, limit):
            self.reset(mx)
            print_msg(ver_limit, "Solving up to the limit:",mx,"@",str(datetime.datetime.now().time()))
            # return number of movers if solution was found
            if self.solve(): return mx

    def solve(self, state=None, level=0):
        " recurs. iterate all moves up to max.depth "
        if state is None: state = self.startstate
        # solution found
        if self.solved(state):
            return True
        # limit depth level
        if level > self.maxdepth:
            print_msg(ver_depth, "MAX depth",self.maxdepth,"reached !")
            return False
        # end recursion if we need more moves than left at this level
        if self.min_moves_togo(state) > (self.maxdepth - level):
            print_msg(ver_depth, "LIMIT depth reached !")
            return False
        # indicate we are in level ...
        print_msg(ver_level, level, nocr=True)
        # save to cache
        self.set_visited(level, state)
        # try all possible moves
        for newstate in self.possible_moves(state):
            # skip if we have been there already
            if self.was_visited_on_upper_level(level, newstate): continue
            # display optional ASCII map
            self.show_map(level, newstate)
            # recurs one level deeper
            if self.solve(newstate, level+1):
                # rebuild solution map of steps
                self.solution.insert(0, newstate)
                # instert start state at level 0 to have complete map of moves
                if level == 0: self.solution.insert(0, state)
                # we have solution
                return True
        # solution not found
        return False

    def solved(self, state):
        " solved if all items are on top floor = all other floors are empty "
        #topfloor = state[self.floors]
        return all( [ state[f] == [] for f in state if f != self.floors ] )

    def possible_moves(self, state):
        " generator returns newstate "
        floornum = self.elevator_floor(state)
        # items we can move, except elevator
        items = state[floornum]
        # try pairs (itema,itemb) build form items
        for itema in items:
            for itemb in items:
                # cannot take the same item twice
                if itema == itemb: continue
                # we are goping to move this items
                move_items = []
                # elevator  means do not take item
                if itema != self.elevator: move_items.append(itema)
                if itemb != self.elevator: move_items.append(itemb)
                # move up (+1) or down (-1)
                for updown in [+1,-1]:
                    # ok if we are within building floors
                    if 1 <= floornum+updown <= self.floors:
                        # calc new state
                        newstate = self.move_items_to_floor(move_items, (floornum,updown), state)
                        # check safety
                        if not self.is_state_ok(newstate):
                            print_msg(ver_move, "mchip fried !")
                            continue
                        # return only safe new state
                        print_msg(ver_move, "OK")
                        yield newstate


    def move_items_to_floor(self, items, (floornum,updown), astate):
        " move items on floornum up/down and return new state "
        # verbose output
        print_msg(ver_move, "move items:", items, "floor:", floornum, "up/down:", updown, nocr=True)
        # create new state dictionary
        state = self.copy_state(astate)
        # remove elevator from source floor
        state[floornum].remove(self.elevator)
        # remove items from source floor
        for item in items:
            state[floornum].remove(item)
        # move items and elevator to the destination floor
        state[floornum+updown].extend(items + [self.elevator])
        # new state
        return state

    def elevator_floor(self, state):
        " which floor is the elevator on "
        for num,items in state.items():
            if 'E' in items: return num

    def is_state_ok(self, state):
        " check is state is OK = all floors are OK "
        return all([ self.is_floor_ok(num, items) for num,items in state.items() ])

    def is_floor_ok(self, num, items):
        " floor is OK if all chips are connected or there is no generator on the floor "
        return all([ self.mchip_connected(items, chip) for chip in self.mchip_on_floor(items) ]) \
               or not self.gen_on_floor(items)

    def mchip_connected(self, items, chip):
        " check if mchip is conneted to its generator within items "
        gen = chip[:-1] + 'G'
        return gen in self.gen_on_floor(items)

    def mchip_on_floor(self, items):
        " return only mchips from items "
        return [ e for e in items if self.is_mchip(e) ]

    def gen_on_floor(self, items):
        " return only generators from items "
        return [ e for e in items if self.is_gen(e) ]

    def is_mchip(self, id):
        " check if item id is microchip "
        return id.endswith('M')

    def is_gen(self, id):
        " check if item id is generator "
        return id.endswith('G')


def testcase(input, result):
    " testcase verifies if input returns result "
    print "TestCase",
    print "for input:",input,"\t expected result:",result,
    f = RtgBuilding()
    f.set_floors(input)
    f.show_map()
    r = f.find_min()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose:
        print_msg(ver_stat, "Memory:",len(f.memory))
        print_msg(ver_stat, "Solution steps:",len(f.solution)-1)
        if verbose & ver_sol:
            for idx,st in enumerate(f.solution):
                f.show_map(idx, st, force=True)
            print
    print

# ========
#  Task A
# ========

# test cases
tdata = [ (1, ['E','HM','LM']), (2, ['HG']), (3, ['LG']) ]
testcase(tdata, 11)

data = [ (1, ['E', 'PoG', 'ThG', 'ThM', 'PrG', 'RuG', 'RuM', 'CoG', 'CoM' ]), (2, ['PoM', 'PrM']) ]
b = RtgBuilding()
b.set_floors(data)
b.show_map()
# 47 (cca 11min)
r = b.find_min()
#
print 'Task A input file:','Result:',r
if verbose:
    print "Solution steps:", len(b.solution)
    if verbose & ver_sol:
        for idx, st in enumerate(b.solution):
            b.show_map(idx, st, force=True)
        print
print

# ========
#  Task B
# ========

data = [ (1, ['E', 'PoG', 'ThG', 'ThM', 'PrG', 'RuG', 'RuM', 'CoG', 'CoM', 'ElG', 'ElM', 'DiG', 'DiM' ]), (2, ['PoM', 'PrM']) ]
b = RtgBuilding()
b.set_floors(data)
b.show_map()
#
r = b.find_min()
#
print 'Task B input file:','Result:',r
if verbose:
    print "Solution steps:", len(b.solution)
    if verbose & ver_sol:
        for idx, st in enumerate(b.solution):
            b.show_map(idx, st, force=True)
        print
print
