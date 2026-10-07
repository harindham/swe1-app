from django import template

register = template.Library()


@register.filter
def vote_percent(votes, total):
    """Returns the percentage of votes for a choice, given the total votes."""
    if total == 0:
        return 0
    return round((votes / total) * 100)
