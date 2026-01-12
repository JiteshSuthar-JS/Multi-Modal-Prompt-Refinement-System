def refine(ai_data, input_sources):
    refined = {}

    refined["product_intent"] = ai_data.get("product_intent", "")

    refined["target_user"] = ai_data.get("target_user", "Not specified")

    refined["core_features"] = ai_data.get("core_features", [])

    refined["technical_constraints"] = ai_data.get("technical_constraints", [])

    refined["expected_outputs"] = ai_data.get("expected_outputs", [])

    refined["input_sources"] = input_sources

    # Assumptions
    assumptions = []
    if refined["target_user"] == "Not specified":
        assumptions.append("Target user assumed as general users")

    refined["assumptions"] = assumptions

    # Missing information
    missing = []
    if not refined["expected_outputs"]:
        missing.append("Expected outputs not specified")

    refined["missing_information"] = missing

    # Confidence score
    score = 1.0
    if missing:
        score -= 0.3
    if not refined["core_features"]:
        score -= 0.3

    refined["confidence_score"] = max(score, 0.0)

    return refined
