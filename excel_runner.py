import pandas as pd
from playwright.sync_api import sync_playwright
from executor import run_steps

FILE = "test_cases.xlsx"


def run_agent():

    # ================= LOAD EXCEL SAFELY =================
    df = pd.read_excel(FILE)

    if "Status" not in df.columns:
        df["Status"] = ""

    if "ErrorDetails" not in df.columns:
        df["ErrorDetails"] = ""

    df["Status"] = df["Status"].astype(str)
    df["ErrorDetails"] = df["ErrorDetails"].astype(str)

    with sync_playwright() as p:
        print("🌐 Launching browser...")

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ================= LOGIN =================
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        print("🔐 Login successful")

        # ================= RUN TESTS =================
        for i, row in df.iterrows():

            test_id = str(row["TestID"]).strip()

            print(f"\n🧪 RUNNING: {test_id}")

            # ================= TC002 =================
            if test_id == "TC002":
                steps = [
                    {"action": "click", "target": "backpack"}
                ]

            # ================= TC003 =================
            elif test_id == "TC003":
                steps = [
                    {"action": "click", "target": "cart"}
                ]

            # ================= TC004 (FINAL FIXED FLOW) =================
            elif test_id == "TC004":
                steps = [
                    {"action": "click", "target": "cart"},
                    {"action": "click", "target": "checkout"},
                    {"action": "type", "target": "first", "value": "John"},
                    {"action": "type", "target": "last", "value": "Doe"},
                    {"action": "type", "target": "zip", "value": "12345"},
                    {"action": "click", "target": "continue"},
                    {"action": "click", "target": "finish"},
                ]

            else:
                continue

            error = run_steps(page, steps)

            df.at[i, "Status"] = "FAIL" if error else "PASS"
            df.at[i, "ErrorDetails"] = error if error else ""

        df.to_excel(FILE, index=False)

        print("\n✅ ALL TESTS FINISHED")

        browser.close()


if __name__ == "__main__":
    run_agent()