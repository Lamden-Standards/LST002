# Required
meta = Hash()

@construct
def seed(vk: str):
    #Define meta values
    meta['key1'] = 'some value'
    meta['key2'] = 'some value'
    meta['key3'] = 'some value'

    # Optional: needed if meta values are intended to be mutable
    meta['operator'] = vk

# Optional: needed if meta values are intended to be mutable
@export
def change_meta(key: str, value: Any):
    assert ctx.caller == meta['operator'], 'Only operator can set meta!'
    meta[key] = value