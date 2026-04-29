import pandas as pd

data = [
    {
        "TestID": "TC001",
        "TestCase": "Login with valid credentials",
        "Status": "",
        "ErrorDetails": ""
    },
    {
        "TestID": "TC002",
        "TestCase": "Add Sauce Labs Backpack to cart",
        "Status": "",
        "ErrorDetails": ""
    },
    {
        "TestID": "TC003",
        "TestCase": "Open cart and verify Sauce Labs Backpack",
        "Status": "",
        "ErrorDetails": ""
    },
    {
        "TestID": "TC004",
        "TestCase": "Checkout cart, enter user details, finish order and verify success message",
        "Status": "",
        "ErrorDetails": ""
    }
]

df = pd.DataFrame(data)
df.to_excel("test_cases.xlsx", index=False)

print("✅ Excel created")