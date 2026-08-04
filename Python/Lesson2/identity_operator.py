# is operator is used to check whether both are pointing yo same object or not
a = 5
b = 5
# In Python, integers are immutable objects. Python often uses integer caching, where small integers (commonly -5 to 256, depending on implementation) are stored once and reused.

print(a is b)


# Small integers may share the same object because of Python's caching behavior.

c = [1,2]
d = [1,2]
# Same values, but different objects in memory.
print(c==d)
print(c is d)