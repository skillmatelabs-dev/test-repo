"""Test file with Stripe API usage that has breaking changes."""
import stripe

stripe.api_key = "sk_test_123"

# Old Stripe API - plan parameter (deprecated)
def create_subscription_old(customer_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        plan="price_123",  # BREAKING: plan renamed to items[0].price
        payment_behavior="default_incomplete",
        expand=["latest_invoice.payment_intent"]
    )
    return subscription

# Old Stripe API - subscription.current_period_start (deprecated)
def get_subscription_period(subscription):
    # BREAKING: current_period_start moved to subscription.items.data[0].current_period_start
    return subscription.current_period_start

# Old Stripe API - source parameter for payment methods
def create_payment_intent_old(amount):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        source="tok_visa",  # BREAKING: source renamed to payment_method
        payment_method_types=["card"]
    )
    return intent

# Old Stripe API - billing address fields
def create_customer_old(email):
    customer = stripe.Customer.create(
        email=email,
        source="tok_visa",  # BREAKING: source deprecated
        billing_address={  # BREAKING: billing_address renamed to address
            "line1": "123 Main St",
            "city": "San Francisco"
        }
    )
    return customer# Added test function
# test change to trigger webhook
# stripe test
# final test
