from dotenv import load_dotenv
load_dotenv()

# we need to load_dotenv() beore importing aocd
from aocd import data, submit  # noqa
