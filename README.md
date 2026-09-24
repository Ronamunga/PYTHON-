# CopperGate Minerals

A web-based mineral and commodities trading platform for managing mineral products, catalogue information, and administrator access.

## Overview

CopperGate Minerals is a web application designed to provide a structured catalogue of minerals and commodities available for qualified buyers.

The system contains detailed information about products such as:

* Copper
* Gold
* Silver
* Cobalt
* Lithium
* Coltan / Tantalite
* Tin
* Manganese
* Iron
* Nickel
* Zinc
* Graphite
* Bauxite
* Bitumen

Each mineral can contain information such as its grade, purity, origin, minimum order quantity, unit of measurement, Incoterms, pricing notes, and sales volume.

## Features

### Mineral Catalogue

The application provides a catalogue of mineral products with detailed specifications, including:

* Product name
* Category
* Product code
* Description
* Grade
* Purity
* Origin
* Minimum order quantity
* Unit
* Incoterms
* Pricing information
* Sales volume
* Featured products
* Best-selling products

### Administrator Account

The application supports an administrator account that can be created using environment variables.

The administrator can be configured with:

* Name
* Company
* Email
* Phone number
* Password
* Administrator role

### Catalogue Seeding

The application includes a seed process that automatically adds missing mineral products to the database.

Existing catalogue records are not overwritten during normal application startup. An optional update mode can be used when the catalogue needs to be synchronised with the seed data.

## Mineral Categories

The catalogue includes several categories:

* Copper
* Bitumen
* Precious Metals
* Battery Minerals
* Critical Minerals
* Industrial Minerals
* Ferrous Minerals
* Base Metals

## Technologies

The project uses Python and a database layer built around SQLAlchemy/Flask-style models.

Key components shown in the seed system include:

* Python
* Flask
* SQLAlchemy
* Database models
* Environment variables

## Project Structure

A typical project structure may look like:

```text
CopperGate-Minerals/
│
├── models.py
├── extensions.py
├── seed.py
├── ...
│
├── templates/
├── static/
│
└── README.md
```

## Database Seeding

The catalogue can be populated using the `seed_catalogue()` function.

By default, existing products are preserved so that changes made through the administrator dashboard are not accidentally overwritten.

```python
seed_catalogue(update_existing=False)
```

When synchronisation with the source catalogue is required:

```python
seed_catalogue(update_existing=True)
```

## Administrator Setup

The administrator can be configured using environment variables:

```text
ADMIN_EMAIL
ADMIN_PASSWORD
ADMIN_NAME
ADMIN_COMPANY
ADMIN_PHONE
```

For example:

```text
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your_secure_password
ADMIN_NAME=CopperGate Administrator
ADMIN_COMPANY=CopperGate Minerals
ADMIN_PHONE=+254XXXXXXXXX
```


## Purpose

The project demonstrates how a mineral trading platform can organise commodity information, manage product catalogues, and provide controlled administrator access.

Ronald Munga

