# -*- coding: utf-8 -*-
{
    "name": "Custom Placeholder Color",

    "summary": """
        This Module Allows you to Placeholder Font Color Brighter in Odoo v16.""",

    "description": """
        This Module Allows you to Placeholder Font Color Brighter in Odoo v16.
    """,

    "author": "Ceres IT Solution",
    "website": "http://www.ceresitsolution.com",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Extra Rights",
    "version": "0.1",

    # any module necessary for this one to work correctly
    "depends": ["base"],
    "images":["static/description/placeholder.png"],
    # always loaded
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "custom_placeholder_color/static/src/css/main.scss",

        ], },
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
