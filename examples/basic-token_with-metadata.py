# LST001
balances = Hash(default_value=0)

# LST002
meta = Hash()

@construct
def seed(vk: str):
    # LST001
    balances[vk] = 1_000_000

    # LST002
    meta['token_name'] = "TEST TOKEN"
    meta['token_symbol'] = "TST"
    meta['token_logo_url'] = 'https://some.token.url/test-token.png'
    meta['operator'] = vk

# LST002
@export
def change_meta(key: str, value: Any):
    assert ctx.caller == meta['operator'], 'Only operator can set meta!'
    meta[key] = value

# LST001
@export
def transfer(amount: float, to: str):
    assert amount > 0, 'Cannot send negative balances!'
    assert balances[ctx.caller] >= amount, 'Not enough coins to send!'

    balances[ctx.caller] -= amount
    balances[to] += amount

# LST001
@export
def balance_of(account: str):
    return balances[account]

# LST001
@export
def allowance(owner: str, spender: str):
    return balances[owner, spender]

# LST001
@export
def approve(amount: float, to: str):
    assert amount > 0, 'Cannot send negative balances!'
    balances[ctx.caller, to] += amount
    return balances[ctx.caller, to]

# LST001
@export
def transfer_from(amount: float, to: str, main_account: str):
    assert amount > 0, 'Cannot send negative balances!'
    assert balances[main_account, ctx.caller] >= amount, 'Not enough coins approved to send! You have {} and are trying to spend {}'\
        .format(balances[main_account, ctx.caller], amount)
    assert balances[main_account] >= amount, 'Not enough coins to send!'

    balances[main_account, ctx.caller] -= amount
    balances[main_account] -= amount
    balances[to] += amount