
def search4prepositions_zhs(phrase: str) -> set:
    """Return any prepositions found in a supplied phrase."""

    vowels = set('临乎与为共冲到兜于即从以似假去让诸及往迆连迎道遵对导寻将当叫吃合同向和问如尽打执把投拦按捉洎给维缘在因惟就比照较方爿暨拿替望朝爰直由率被用繇齐至管自起趁践跟')
    return vowels.intersection(set(phrase))

def search4letters(phrase: str, letters: str='临乎与为共冲到兜于即从以似假去让诸及往迆连迎道遵对导寻将当叫吃合同向和问如尽打执把投拦按捉洎给维缘在因惟就比照较方爿暨拿替望朝爰直由率被用繇齐至管自起趁践跟') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
