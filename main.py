from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")

    budget = input("Budget (low/medium/high): ").lower()

    if budget == "low":
        facts.append("budget_low")
    elif budget == "medium":
        facts.append("budget_medium")
    elif budget == "high":
        facts.append("budget_high")

    if input("Will you use this laptop for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Will you do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Will you mainly do office work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")

    os_pref = input("Preferred OS (windows/macos/linux): ").lower()

    if os_pref == "windows":
        facts.append("pref_os_windows")
    elif os_pref == "macos":
        facts.append("pref_os_macos")
    elif os_pref == "linux":
        facts.append("pref_os_linux")

    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you want a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")

    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)

    engine = ForwardChainingEngine(rules)

    facts = collect_initial_facts()

    engine.assert_facts(facts)

    engine.run()

    results = engine.conclusions()

    print("\nRecommendations:")
    for recommendation in results["recommendations"]:
        print(" -", recommendation)

    print("\nSpecifications:")
    for spec in results["specs"]:
        print(" -", spec)

    print("\nFired Rules:")
    for step in engine.trace:
        print(f" - {step['rule']}")

if __name__ == "__main__":
    main()
