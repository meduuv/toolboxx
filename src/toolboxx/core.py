def keys(mapping): return sorted(mapping)
def apply(mapping, updates):
    result=dict(mapping);result.update(updates);return result
