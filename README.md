# UpBank client
This project is a collection of experience and an attempt to make a fully typed extensible asynchronous library based on generated openapi models with a subsequent abstraction perspective for any api 

based on [JargeZ/au-open-banking-client](https://github.com/JargeZ/au-open-banking-client)

---
### ⚠️ DRAFT warning
### This project is a work in progress and is not yet ready for use.
This project will probably not be maintained, but serves as a basis for creating extensible abstract clients based on openapi

### Usage
You can use endpoints directly

```python
from upbank_client.client.async_client import AsyncClient

client = AsyncClient() # token from env: UPBANK_TOKEN
client = AsyncClient(token="up:demo:Yj3rbF53jhwj") # token directly

await client.api.transactions.transactions_id_get("{uuid}")
```

OR with some wrappers\
(you can also inherit and add you own helper methods)

```python
async for transaction in client.get_all_transactions():
    details = await client.get_transaction_details(transaction.id)
    print(f"\n\n"
          f"- {transaction.attributes.description} -\n"
          f"| {transaction.attributes.amount.value} {transaction.attributes.amount.currency_code}\n"
          f"| {details.json()}")
```
---
go-task install (modern make replacement)
```shell
# macOS
brew install go-task

# windows
choco install go-task

# linux
npm install -g @go-task/cli
# + reffer to https://taskfile.dev/#/installation
```

### Problems and TODOs:
- [x] Automatic generation and tailoring
- [x] Transparent models overwriting
- [ ] Nested models overwriting
- [ ] Session management wrapping
- [ ] sync client as wrapped async
