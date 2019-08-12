# Terra-py

Python library for Terra Core

## Installation

todo

## Usage

```python
from terra import msg

m = msg.StdTx(
    fee=msg.Fee('10000', [msg.Amount('2000', 'uluna')]),
    memo='test transaction',
    msg=[
        msg.MsgSend(
            amount=[msg.Amount('10', 'uluna')],
            from_address='terra7wwemlk5j73artt5t6j8am08ql3qv1ptdx6akgk',
            to_address='terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv',
        ),
    ],
)

m.to_json()
```

## Develop

Install poetry

```bash
pip install --user poetry
```

Install dependencies

```bash
poetry install
```

Run tests

```bash
poetry run coverage run --source terra -m pytest -v
```
