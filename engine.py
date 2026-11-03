from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        return (
            all(fact in self.facts for fact in rule.antecedents)
            and rule.consequent not in self.facts
        )

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        
        while True:
            fired = False;

            for rule in sorted(
                self.rules,
                key=lambda r: r.priority,
                reverse=True
            ):
                if  self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "consequent": rule.consequent
                    })

                    fired = True
                    break
            if not fired:
                break


    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""
        recommendations = []
        specs = []
        other = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact)
            elif fact.startswith("spec:"):
                specs.append(fact)
            else:
                other.append(fact)

        return {
            "recommendations": recommendations,
            "specs": specs,
            "other": other
        }
