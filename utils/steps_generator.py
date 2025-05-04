def generate_step(description: str, result: bool):
    print(f"STEP: {description} - {'PASSED' if result else 'FAILED'}")
