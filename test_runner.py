from llm_parser import parse_test_case
from executor import run_steps

def normalize_steps(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "actions" in data:
        return data["actions"]
    return [data] if isinstance(data, dict) else []

if __name__ == "__main__":
    test_case = "Verify login at the-internet with tomsmith and SuperSecretPassword!"
    
    print("\n🧠 Parsing test case...")
    raw_output = parse_test_case(test_case)
    steps = normalize_steps(raw_output)

    if not steps:
        print("❌ NO STEPS GENERATED")
        exit()

    print(f"\n🌐 Running {len(steps)} steps...")
    error = run_steps(steps)

    print("\n================ QA REPORT ================")
    if error:
        print(f"❌ FINAL RESULT: FAILED")
        print(f"Details: {error}")
    else:
        print(f"✅ FINAL RESULT: PASSED")