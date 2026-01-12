def validate(refined_prompt):
    if not refined_prompt["product_intent"]:
        return False, "Missing product intent"

    if len(refined_prompt["core_features"]) == 0:
        return False, "No features specified"

    return True, "Valid"
