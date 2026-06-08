# MISTAKE 1: Using mutable class variables (lists, dicts)
class Team:
    members = []   # ❌ DANGEROUS! Shared mutable list

    def add_member(self, name):
        self.members.append(name)  # Modifies the SHARED list!

t1 = Team()
t2 = Team()
t1.add_member("Alice")
t2.add_member("Bob")

print(t1.members)  # ['Alice', 'Bob'] ← t2's member is here too! 😱
print(t2.members)  # ['Alice', 'Bob'] ← same list!

# FIX: Use instance variables for mutable data
class Team:
    def __init__(self):
        self.members = []   # ✅ Each team gets its OWN list

    def add_member(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add_member("Alice")
t2.add_member("Bob")
print(t1.members)  # ['Alice']  ✅
print(t2.members)  # ['Bob']    ✅

# MISTAKE 2: Accessing class variable via instance when it can shadow
class Config:
    debug = False

c = Config()
c.debug = True       # Creates INSTANCE variable, not changing class variable!
print(Config.debug)  # False — class variable unchanged!