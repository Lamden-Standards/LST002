# Required
metadata = Hash()

@construct
def seed(vk: str):
    #Define metadata values
    metadata['key1'] = 'some value'
    metadata['key2'] = 'some value'
    metadata['key3'] = 'some value'

    # Optional: needed if metadata values are intended to be mutable
    metadata['operator'] = vk

# Optional: needed if metadata values are intended to be mutable
@export
def change_meta(key: str, value: Any):
    assert ctx.caller == metadata['operator'], 'Only operator can set metadata!'
    metadata[key] = value