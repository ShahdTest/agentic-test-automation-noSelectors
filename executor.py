def run_steps(page, steps):
    error = None

    try:
        for step in steps:
            action = step.get("action")
            target = str(step.get("target", "")).lower()
            value = step.get("value", "")

            print(f"   ▶ {action} | {target}")

            page.wait_for_load_state("domcontentloaded")

            # ================= ADD ITEM =================
            if action == "click" and target == "backpack":
                page.click("#add-to-cart-sauce-labs-backpack")

            # ================= CART =================
            elif action == "click" and target == "cart":
                page.click(".shopping_cart_link")
                page.wait_for_url("**/cart.html")
                page.wait_for_selector(".cart_item")

            # ================= CHECKOUT =================
            elif action == "click" and target == "checkout":
                page.click("#checkout")
                page.wait_for_url("**/checkout-step-one.html")

            elif action == "click" and target == "continue":
                page.click("#continue")
                page.wait_for_url("**/checkout-step-two.html")

            elif action == "click" and target == "finish":
                page.click("#finish")
                page.wait_for_selector(".complete-header")

            # ================= TYPE =================
            elif action == "type":

                if target == "first":
                    page.fill("#first-name", value or "John")

                elif target == "last":
                    page.fill("#last-name", value or "Doe")

                elif target == "zip":
                    page.fill("#postal-code", value or "12345")

            page.wait_for_timeout(700)

    except Exception as e:
        error = str(e)
        print("❌ Execution Error:", error)

    return error