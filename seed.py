"""Initial catalogue and administrator seeding for CopperGate Minerals."""

import os
from decimal import Decimal

from extensions import db
from models import Mineral, User


MINERALS = [
    {
        "slug": "copper-cathodes",
        "name": "Copper Cathodes",
        "category": "Copper",
        "code": "CU-CATH",
        "short_description": "LME Grade A copper cathodes for cable, manufacturing and industrial buyers.",
        "description": (
            "High-purity copper cathodes supplied against agreed inspection, assay and export "
            "documentation. Suitable for cable manufacturing, electrical applications, alloying "
            "and verified commodity trading programmes. Lot photographs, packing information and "
            "shipping documentation are provided during transaction verification."
        ),
        "grade": "LME Grade A",
        "purity": "99.99% Cu",
        "origin": "Africa / Global",
        "minimum_order": Decimal("20"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Commercial quote based on LME reference, volume and delivery terms",
        "sales_volume": Decimal("18450"),
        "is_best_seller": True,
        "is_featured": True,
        "is_active": True,
        "accent": "copper",
    },
    {
        "slug": "copper-concentrate",
        "name": "Copper Concentrate",
        "category": "Copper",
        "code": "CU-CONC",
        "short_description": "Copper concentrate for smelters, processors and qualified bulk buyers.",
        "description": (
            "Specification-led copper concentrate supply for smelting and further processing. "
            "Final grade, moisture, deleterious elements, treatment charges, penalties and payable "
            "terms are agreed against a representative assay and signed transaction contract."
        ),
        "grade": "Cu 20–30%",
        "purity": "Assay dependent",
        "origin": "Central & Southern Africa",
        "minimum_order": Decimal("100"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR",
        "price_note": "Payable terms issued after assay and specification review",
        "sales_volume": Decimal("12100"),
        "is_best_seller": True,
        "is_featured": True,
        "is_active": True,
        "accent": "umber",
    },
    {
        "slug": "copper-wire-rod",
        "name": "Copper Wire Rod",
        "category": "Copper",
        "code": "CU-WR",
        "short_description": "High-conductivity copper wire rod for cable and electrical manufacturing.",
        "description": (
            "Electrolytic tough-pitch copper wire rod supplied for wire drawing, power cable, "
            "telecommunications and electrical manufacturing. Coil weight, diameter, conductivity "
            "and applicable production standards are confirmed in the commercial specification."
        ),
        "grade": "ETP Copper Wire Rod",
        "purity": "99.90%–99.99% Cu",
        "origin": "Africa / Global",
        "minimum_order": Decimal("20"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Quote based on specification, LME reference and delivery basis",
        "sales_volume": Decimal("9100"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "copper",
    },
    {
        "slug": "bitumen-60-70",
        "name": "Bitumen 60/70",
        "category": "Bitumen",
        "code": "BIT-6070",
        "short_description": "Penetration-grade road bitumen for asphalt and infrastructure projects.",
        "description": (
            "Bitumen 60/70 supplied in agreed bulk, steel drum or jumbo-bag formats for asphalt "
            "production, highways and infrastructure projects. Product certification, packaging "
            "availability and loading schedules are confirmed for each shipment."
        ),
        "grade": "Penetration 60/70",
        "purity": "ASTM / EN specification",
        "origin": "Middle East / Africa",
        "minimum_order": Decimal("100"),
        "unit": "MT",
        "incoterms": "FOB, CFR, CIF",
        "price_note": "Quote depends on packaging, loading port and shipment size",
        "sales_volume": Decimal("8900"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "carbon",
    },
    {
        "slug": "bitumen-80-100",
        "name": "Bitumen 80/100",
        "category": "Bitumen",
        "code": "BIT-80100",
        "short_description": "Road-construction bitumen suited to selected climates and mix designs.",
        "description": (
            "Bitumen 80/100 for paving and industrial applications where a softer penetration "
            "grade is specified. Packaging, testing requirements, loading window and delivery "
            "schedule are aligned before contract execution."
        ),
        "grade": "Penetration 80/100",
        "purity": "ASTM / EN specification",
        "origin": "Middle East / Africa",
        "minimum_order": Decimal("100"),
        "unit": "MT",
        "incoterms": "FOB, CFR, CIF",
        "price_note": "Quote depends on packaging, loading port and shipment size",
        "sales_volume": Decimal("6200"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "slate",
    },
    {
        "slug": "gold-dore",
        "name": "Gold Doré",
        "category": "Precious Metals",
        "code": "AU-DORE",
        "short_description": "Gold doré supply for licensed and compliance-approved buyers.",
        "description": (
            "Gold doré enquiries are handled only with licensed, verified counterparties and "
            "appropriate KYC, beneficial-ownership, source, export and assay documentation. Final "
            "purity, payable content, refinery procedure and settlement terms are transaction-specific."
        ),
        "grade": "Refinery feed / assay dependent",
        "purity": "Confirmed by independent assay",
        "origin": "Africa",
        "minimum_order": Decimal("1"),
        "unit": "KG",
        "incoterms": "By agreement",
        "price_note": "Available only to licensed and approved counterparties",
        "sales_volume": Decimal("120"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "gold",
    },
    {
        "slug": "gold-bullion",
        "name": "Gold Bullion",
        "category": "Precious Metals",
        "code": "AU-BULL",
        "short_description": "Assayed gold bullion for licensed institutional and wholesale buyers.",
        "description": (
            "Gold bullion transactions are considered only after counterparty verification and "
            "review of assay, refinery, ownership, source-of-funds and export documentation. Bar "
            "weight, fineness, custody, inspection and settlement procedures are confirmed in contract."
        ),
        "grade": "Investment / wholesale bullion",
        "purity": "99.50%–99.99% Au",
        "origin": "Africa / Global",
        "minimum_order": Decimal("1"),
        "unit": "KG",
        "incoterms": "By agreement",
        "price_note": "Indicative pricing issued after compliance and document review",
        "sales_volume": Decimal("95"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "gold",
    },
    {
        "slug": "silver-bullion",
        "name": "Silver Bullion",
        "category": "Precious Metals",
        "code": "AG-BULL",
        "short_description": "High-purity silver bullion for industrial and wholesale buyers.",
        "description": (
            "Assayed silver bullion supplied to verified industrial, jewellery and institutional "
            "buyers. Refinery, bar weight, serialisation, fineness, inspection and delivery terms "
            "are confirmed against the final commercial offer."
        ),
        "grade": "Commercial bullion",
        "purity": "99.90%–99.99% Ag",
        "origin": "Africa / Global",
        "minimum_order": Decimal("50"),
        "unit": "KG",
        "incoterms": "EXW, FOB, CIF",
        "price_note": "Quote based on market reference, fineness and delivery terms",
        "sales_volume": Decimal("430"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "silver",
    },
    {
        "slug": "cobalt-hydroxide",
        "name": "Cobalt Hydroxide",
        "category": "Battery Minerals",
        "code": "CO-HYD",
        "short_description": "Cobalt hydroxide intermediate for qualified processors and refiners.",
        "description": (
            "Cobalt hydroxide supplied subject to buyer qualification, chain-of-custody, origin "
            "documentation and assay alignment. Commercial terms reflect cobalt content, moisture, "
            "impurities, payable percentage and delivery basis."
        ),
        "grade": "Co 20–35%",
        "purity": "Assay dependent",
        "origin": "Central Africa",
        "minimum_order": Decimal("20"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR",
        "price_note": "Payable terms issued after assay and compliance review",
        "sales_volume": Decimal("2700"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "blue",
    },
    {
        "slug": "lithium-spodumene",
        "name": "Lithium Spodumene Concentrate",
        "category": "Critical Minerals",
        "code": "LI-SC",
        "short_description": "Spodumene concentrate for lithium chemical and battery-material processors.",
        "description": (
            "Lithium-bearing spodumene concentrate supplied subject to final Li2O grade, moisture, "
            "particle size and impurity specifications. Representative assay, lot size, loading "
            "schedule and delivery programme are agreed before contracting."
        ),
        "grade": "SC5.0–SC6.0",
        "purity": "Li2O 5.0%–6.0%",
        "origin": "Africa",
        "minimum_order": Decimal("100"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Quote based on Li2O grade, impurities and delivery basis",
        "sales_volume": Decimal("1800"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "silver",
    },
    {
        "slug": "coltan-tantalite",
        "name": "Coltan / Tantalite Concentrate",
        "category": "Critical Minerals",
        "code": "TA-COLT",
        "short_description": "Tantalite-bearing concentrate for audited and qualified processors.",
        "description": (
            "Coltan and tantalite concentrate enquiries require verified origin, chain-of-custody, "
            "export eligibility and independent assay documentation. Ta2O5 content, niobium content, "
            "moisture, penalties and payable terms are agreed per lot."
        ),
        "grade": "Ta2O5 20%–40%",
        "purity": "Assay dependent",
        "origin": "Central & East Africa",
        "minimum_order": Decimal("5"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR",
        "price_note": "Available after origin, assay and responsible-sourcing review",
        "sales_volume": Decimal("640"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "slate",
    },
    {
        "slug": "tin-cassiterite",
        "name": "Cassiterite Tin Concentrate",
        "category": "Critical Minerals",
        "code": "SN-CASS",
        "short_description": "Cassiterite concentrate for licensed smelters and tin processors.",
        "description": (
            "Tin-bearing cassiterite concentrate supplied with origin, chain-of-custody and assay "
            "documentation. Tin content, moisture, particle size, deleterious elements and payable "
            "terms are confirmed for each lot before shipment."
        ),
        "grade": "Sn 60%–70%",
        "purity": "Assay dependent",
        "origin": "Central & East Africa",
        "minimum_order": Decimal("10"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR",
        "price_note": "Payable terms issued after assay and responsible-sourcing review",
        "sales_volume": Decimal("850"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "brown",
    },
    {
        "slug": "manganese-ore",
        "name": "Manganese Ore",
        "category": "Industrial Minerals",
        "code": "MN-ORE",
        "short_description": "Metallurgical manganese ore for alloy and steel production.",
        "description": (
            "Bulk manganese ore available to qualified industrial buyers. Grade, sizing, moisture, "
            "phosphorus, silica and other impurity thresholds are defined in the final specification "
            "sheet and commercial agreement."
        ),
        "grade": "Mn 35%–48%",
        "purity": "Assay dependent",
        "origin": "Africa",
        "minimum_order": Decimal("500"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Quote based on manganese grade, sizing and logistics",
        "sales_volume": Decimal("5100"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "brown",
    },
    {
        "slug": "iron-ore",
        "name": "Iron Ore",
        "category": "Ferrous Minerals",
        "code": "FE-ORE",
        "short_description": "Bulk iron ore for steel mills, traders and mineral processors.",
        "description": (
            "Iron ore fines or lump supplied against an agreed Fe grade, sizing, moisture and "
            "impurity profile. Silica, alumina, phosphorus, sulphur and loss-on-ignition limits are "
            "confirmed through representative assay and contract specifications."
        ),
        "grade": "Fe 58%–64%",
        "purity": "Assay dependent",
        "origin": "Africa",
        "minimum_order": Decimal("1000"),
        "unit": "MT",
        "incoterms": "FOB, CFR, CIF",
        "price_note": "Quote based on Fe grade, product form and shipment size",
        "sales_volume": Decimal("7800"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "umber",
    },
    {
        "slug": "nickel-ore",
        "name": "Nickel Ore",
        "category": "Base Metals",
        "code": "NI-ORE",
        "short_description": "Nickel-bearing ore for qualified smelters and processing facilities.",
        "description": (
            "Nickel ore supplied subject to final nickel grade, iron content, moisture, sizing and "
            "impurity specifications. Availability, loading method and payable terms are confirmed "
            "after assay and logistics review."
        ),
        "grade": "Ni 1.5%–2.0%",
        "purity": "Assay dependent",
        "origin": "Africa / Global",
        "minimum_order": Decimal("1000"),
        "unit": "MT",
        "incoterms": "FOB, CFR, CIF",
        "price_note": "Quote based on nickel content, moisture and destination",
        "sales_volume": Decimal("3200"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "slate",
    },
    {
        "slug": "zinc-ingots",
        "name": "Zinc Ingots",
        "category": "Base Metals",
        "code": "ZN-SHG",
        "short_description": "Special High Grade zinc ingots for galvanising and manufacturing.",
        "description": (
            "Special High Grade zinc ingots for galvanising, die casting, alloy production and "
            "industrial use. Producer brand, bundle weight, ingot dimensions and certification are "
            "confirmed with the final commercial offer."
        ),
        "grade": "Special High Grade",
        "purity": "99.995% Zn",
        "origin": "Global",
        "minimum_order": Decimal("25"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Quote based on LME reference, brand and delivery basis",
        "sales_volume": Decimal("3900"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "silver",
    },
    {
        "slug": "graphite-flakes",
        "name": "Natural Flake Graphite",
        "category": "Critical Minerals",
        "code": "C-GRAPH",
        "short_description": "Natural flake graphite for refractory, industrial and battery applications.",
        "description": (
            "Natural flake graphite supplied according to fixed-carbon content, flake-size "
            "distribution, moisture, ash and volatile-matter specifications. Purification level, "
            "packaging and application requirements are agreed with each buyer."
        ),
        "grade": "Medium / large flake",
        "purity": "94%–98% fixed carbon",
        "origin": "Africa",
        "minimum_order": Decimal("50"),
        "unit": "MT",
        "incoterms": "EXW, FOB, CFR, CIF",
        "price_note": "Quote based on carbon purity, flake size and packaging",
        "sales_volume": Decimal("2100"),
        "is_best_seller": False,
        "is_featured": True,
        "is_active": True,
        "accent": "carbon",
    },
    {
        "slug": "bauxite-ore",
        "name": "Bauxite Ore",
        "category": "Industrial Minerals",
        "code": "AL-BAUX",
        "short_description": "Metallurgical-grade bauxite for alumina and industrial processing.",
        "description": (
            "Bulk bauxite ore supplied against agreed alumina, reactive silica, total silica, iron "
            "oxide, moisture and sizing specifications. Shipment size and commercial terms are "
            "confirmed after representative assay and logistics review."
        ),
        "grade": "Metallurgical grade",
        "purity": "Al2O3 45%–55%",
        "origin": "Africa",
        "minimum_order": Decimal("1000"),
        "unit": "MT",
        "incoterms": "FOB, CFR, CIF",
        "price_note": "Quote based on alumina content, silica and shipment size",
        "sales_volume": Decimal("4600"),
        "is_best_seller": False,
        "is_featured": False,
        "is_active": True,
        "accent": "umber",
    },
]


def seed_catalogue(update_existing=False):
    """Insert missing catalogue products and optionally refresh existing ones.

    Normal application startup calls this with ``update_existing=False`` so
    changes made through the administrator dashboard are never overwritten.
    Maintenance commands can pass ``update_existing=True`` when the catalogue
    must be synchronised with this source file.
    """

    changed = 0

    try:
        for payload in MINERALS:
            product = Mineral.query.filter_by(slug=payload["slug"]).first()

            if product is None:
                db.session.add(Mineral(**payload))
                changed += 1
                continue

            if update_existing:
                for field, value in payload.items():
                    setattr(product, field, value)
                changed += 1

        if changed:
            db.session.commit()

    except Exception:
        db.session.rollback()
        raise

    return changed


def seed_admin():
    """Create the first administrator from environment variables."""

    email = (os.getenv("ADMIN_EMAIL") or "").strip().lower()
    password = os.getenv("ADMIN_PASSWORD") or ""

    if not email or not password:
        return False

    if User.query.filter_by(email=email).first():
        return False

    admin = User(
        full_name=(os.getenv("ADMIN_NAME") or "CopperGate Administrator").strip(),
        company=(os.getenv("ADMIN_COMPANY") or "CopperGate Minerals").strip(),
        email=email,
        phone=(os.getenv("ADMIN_PHONE") or "").strip(),
        role="admin",
        is_active=True,
    )
    admin.set_password(password)

    try:
        db.session.add(admin)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    return True
    end if 