# LST002 - Adding Metadata to Smart Contracts
Not all smart contracts require metadata but there are some types, particularly tokens, that would benefit from some discoverable properties located on the blockchain.
This is not an attempt to standardize any one type of contract metadata but merely an effort to define variables and methods that can be used to do so.

## Inputs
`none`

## Variables

### **metadata**
- Type: `Hash`
    - no default value
- Required: `True`

``` python
metadata = Hash()
```

### **seed**
This standard takes into account that metadata can be mutable. 
In cases where that is the intention it is required that an `operator` be set in the `metadata` Hash using the contract's constructor.

- Decorator: @construct
- Public: `False` 
- Required: `False`
    - only needed to allow metadata to be mutable
- arguments:
    - `vk`
        - type: `string`
        - description: An account to grant the ability to change values in the `metadata` Hash
- state changes: `1`
- assertions: `none`
- return: `void`

``` python
@construct
def seed(vk: str):
    metadata['operator'] = vk
```

### **change_meta**
changing/adding values to the metadata of a smart contract

- Decorator: @export
- Public: `True` 
- Required: `False`
    - only needed if metadata is intended to be mutable
- Requirements
    - requires an `operator` metadata value set in the constructor during submission
- arguments:
    - `key`
        - type: `string`
        - description: The key to lookup in the `metadata` Hash.
    - `value`
        - type: `Any`
        - description: Any value to assign to the `key` in Hash.
- state changes: `1`
- assertions:
    - assert `caller` is equal to `metadata['operator']`
- return: `void`

``` python
@export
def change_meta(key: str, value: Any):
    assert ctx.caller == metadata['operator'], 'Only operator can set metadata!'
    metadata[key] = value
```