# core/stats.rpy — relationship points / characteristics (TECHNICAL_PLAN.md §4)
#
# Data-driven: stats are keys in player.stats, no per-stat variables.
# Episode 00 uses these only lightly (Vergeau hooks); modules use them fully.

init python:

    def stat(name):
        return player.stats.get(name, 0)

    def add_stat(name, amount):
        player.stats[name] = stat(name) + amount
        queue_sync()
