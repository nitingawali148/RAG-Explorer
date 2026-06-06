"""Pre-chunked ShopSphere ecommerce knowledge base.

Documents are split into ~400-char paragraph chunks at import time
(pure string ops, < 1 ms). No ChromaDB, no Ollama, no network calls.
"""
from __future__ import annotations

_DOCS: dict[str, str] = {
    "faq.md": """How do I create an account? Go to shopsphere.com/signup and enter your email and password. Account creation is free and gives you faster checkout, order history, and saved addresses.

How do I reset my password? Visit shopsphere.com/account/reset and enter the email associated with your account. A reset link is valid for 30 minutes.

How do I enable two-factor authentication? After signing in, go to Settings > Security > Two-Factor Authentication. We support both authenticator apps (TOTP) and SMS.

Where can I see my order history? Sign in and go to My Orders. Orders older than 24 months are archived but still accessible by entering the order number.

Can I cancel an order after placing it? Yes, if it has not yet shipped. Go to My Orders, select the order, then Cancel. After shipment, you must use the returns process instead.

What payment methods are accepted? Visa, Mastercard, American Express, Discover, PayPal, Apple Pay, Google Pay, and ShopSphere Gift Cards. Cryptocurrency is not accepted.

Why was my card declined? Common reasons: insufficient funds, address mismatch, expired card, or fraud-prevention hold by your bank. Try a different card or contact your bank.

Do you offer financing? Yes — Affirm financing is available for orders over $100, with terms of 3, 6, or 12 months.

How do I contact support? Email: support@shopsphere.com (response within 24 hours on weekdays). Phone: 1-800-SHOPSPH, Mon-Fri 9am-7pm ET. Live chat: available on shopsphere.com Mon-Fri 9am-9pm ET, weekends 10am-6pm ET.

Is there a loyalty program? Yes — ShopSphere Plus. $9.99/month for free express shipping on every order, 5% back as store credit, and early access to sales.

Can I delete my account? Yes — email privacy@shopsphere.com from the email on file. Account and personal data are deleted within 30 days, except where retention is required by tax or accounting law.""",

    "refund_policy.md": """ShopSphere processes refunds within 7 business days of receiving the returned item at our warehouse in Edison, NJ.

What is refundable: Eligible products returned in their original condition with all packaging. Defective or damaged items at full purchase price including original shipping. Cancelled orders that have not yet shipped.

What is NOT refundable: Original shipping costs unless the return is due to a ShopSphere error. Digital downloads once they have been accessed. Final-sale items including clearance items below 60% of MSRP. Personalized or custom-engraved products.

How refunds are issued: Refunds go back to the original payment method. Credit-card refunds typically appear within 3-5 business days after processing. PayPal refunds typically appear within 1-2 business days. Gift-card purchases are refunded as ShopSphere store credit.

Partial refunds: ShopSphere may issue a partial refund of up to 50% if the item shows signs of use, has missing parts, or is returned without original packaging.

Disputes: For unresolved refund issues, contact billing@shopsphere.com or call 1-800-SHOPSPH within 60 days of the return.""",

    "return_policy.md": """You have 30 days from delivery to return most items for a refund or exchange. Item must be in original condition with tags attached. Original packaging is required. Proof of purchase (order number or email confirmation) is required.

Non-returnable items: Underwear, swimwear, and other intimate apparel. Personalized, monogrammed, or custom-built products. Final-sale items. Perishable goods such as food, plants, and fresh-baked items. Gift cards. Earbuds, in-ear headphones, and other items requiring direct skin contact for hygiene reasons.

Return shipping: Defective or wrong items — ShopSphere pays return shipping. Print a free label from the returns portal. Buyer's remorse — buyer pays return shipping, typically $5.99 via the prepaid label option. International returns — buyer is responsible for return shipping and customs documentation.

Holiday extension: Items purchased between November 1 and December 24 can be returned through January 31 of the following year.

Refund vs exchange: Default action is refund to original payment method. Exchanges for size or color of the same SKU ship free of additional charge. Exchanges for a different product are processed as a refund plus new order.

How to start a return: Go to shopsphere.com/returns and enter your order number. Select the items and reason. Print the prepaid label and drop the package at any USPS or UPS location. Track your return; refund is issued 7 business days after the item arrives at our warehouse.""",

    "shipping_policy.md": """ShopSphere ships from warehouses in Edison NJ (East), Reno NV (West), and Atlanta GA (South).

Domestic shipping US 50 states and DC: Standard shipping is free over $50, otherwise $4.99, and takes 5-7 business days. Express shipping costs $9.99 and takes 2-3 business days. Overnight shipping costs $24.99 and delivers the next business day if ordered before 12pm ET.

International shipping: Available to 38 countries. Cost calculated at checkout based on weight and destination. Delivery time is 10-14 business days. Customs duties, taxes, and import fees are the buyer's responsibility. Prohibited destinations: Russia, North Korea, Iran, Syria, Cuba.

Cut-off and handling: Orders placed before 12pm ET on a weekday ship the same day. Orders placed after 12pm ET ship the next business day. Weekend and federal-holiday orders ship on the next business day.

Tracking: A tracking number is emailed within 1 hour of shipment. Track your order at shopsphere.com/track or in the mobile app.

Lost or delayed packages: Standard shipping is considered delayed only after 10 business days with no movement. File a lost-package claim at shopsphere.com/claim within 30 days of expected delivery.

Address changes: Address changes are allowed only before shipment. After shipping, contact the carrier directly.""",

    "product_catalog.md": """SP-EARBUDS-01 ShopSphere Wireless Earbuds. Price: $79.00. Bluetooth 5.3, up to 30 hours total battery with charging case. Active noise cancellation. IPX4 sweat- and splash-resistant. USB-C charging, 10-min quick charge gives 2 hours playback. 1-year limited warranty. Note: earbuds are non-returnable for hygiene reasons.

SP-LAMP-LED ShopSphere LED Desk Lamp. Price: $39.00. 3 brightness levels and 3 color temperatures: 2700K, 4000K, 5500K. USB-C powered with cable included, adapter sold separately. Touch-sensitive base controls. 360 degree flexible gooseneck. 2-year limited warranty.

SP-CHARGER-30 30W Multi-port USB-C Charger. Price: $24.99. 2x USB-C, 1x USB-A. Fast-charge compatible with PD 3.0 and QC 4.0. Foldable plug for travel.

SP-HOODIE-CL ShopSphere Classic Hoodie. Price: $49.00. 80% cotton, 20% polyester fleece. Sizes XS through XXL. Colors: charcoal, oatmeal, navy, forest. Pre-shrunk, machine washable cold, tumble dry low.

SP-TEE-LOGO Logo Tee. Price: $22.00. 100% organic cotton, 180 GSM. Sizes XS through XXL.

SP-MUG-CER Ceramic Coffee Mug 12oz. Price: $14.00. Stoneware ceramic, matte glaze. Dishwasher- and microwave-safe. Sold individually or as a 4-pack for $49.

SP-CANDLE-VAN Vanilla Soy Candle 8oz. Price: $18.00. 100% soy wax, cotton wick. Approximately 45 hours burn time. Hand-poured in California.""",
}


def _chunk_text(text: str, source: str, size: int = 450) -> list[dict]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, buf, buf_start, idx = [], "", 0, 0
    for para in paragraphs:
        if buf and len(buf) + len(para) + 2 > size:
            chunks.append({
                "id": f"{source}-{idx}",
                "source": source,
                "text": buf,
                "metadata": {"index": idx, "char_start": buf_start, "char_end": buf_start + len(buf)},
            })
            buf_start += len(buf)
            idx += 1
            buf = para
        else:
            buf = (buf + "\n\n" + para).strip() if buf else para
    if buf:
        chunks.append({
            "id": f"{source}-{idx}",
            "source": source,
            "text": buf,
            "metadata": {"index": idx, "char_start": buf_start, "char_end": buf_start + len(buf)},
        })
    return chunks


CHUNKS: list[dict] = []
for _src, _txt in _DOCS.items():
    CHUNKS.extend(_chunk_text(_txt, _src))

STATS = {
    "collection": "shopsphere-bm25",
    "chunks": len(CHUNKS),
    "sources": {},
}
for _c in CHUNKS:
    STATS["sources"][_c["source"]] = STATS["sources"].get(_c["source"], 0) + 1
